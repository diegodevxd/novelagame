"""
Escenas principales del juego (Estados del juego)
"""
import pygame
from enum import Enum
from config import WINDOW_WIDTH, WINDOW_HEIGHT, TOTAL_DAYS
from src.game_systems import PlayerWallet, GachaSystem, PlayerInventory
from src.dialogs import DialogManager
from src.graphics import Screen, BackgroundManager
from src.scenes import DaySceneManager, EndingSequence


class GameState(Enum):
    INTRO = 0
    PLAYING_DAY = 1
    DETERMINING_ENDING = 2
    SHOWING_ENDING = 3


class GameEngine:
    """Motor principal del juego"""
    
    def __init__(self):
        self.screen = Screen()
        self.background_manager = BackgroundManager("Fondos")
        self.player_wallet = PlayerWallet()
        self.player_inventory = PlayerInventory()
        self.gacha_system = GachaSystem()
        
        self.current_state = GameState.INTRO
        self.current_day = 1
        self.choice_selected = 0
        self.game_running = True
        self.intro_shown = False  # Controla si ya se mostró la intro
        
        # Gestores de escenas
        self.day_scene_manager = None
        self.ending_sequence = EndingSequence()
        self.current_ending_sequence = None
        self.ending_dialog_index = 0
        
        # Rastreo de decisiones
        self.gacha_uses_count = 0
        self.mom_visits = 0
        self.days_with_gacha = []  # Días en que usó gacha
        self.days_rested = []
        self.decision_log = {}
        
        # Cargar música de fondo
        self.load_background_music()
    
    def load_background_music(self):
        """Carga y reproduce la música de fondo"""
        try:
            pygame.mixer.music.load("music/principal.mp3")
            pygame.mixer.music.set_volume(0.5)  # Volumen al 50%
            pygame.mixer.music.play(-1)  # -1 para reproducción en loop
            print("Música de fondo cargada correctamente")
        except Exception as e:
            print(f"Advertencia: No se pudo cargar la música: {e}")
    
    def start_new_day(self):
        """Inicia un nuevo día"""
        self.day_scene_manager = DaySceneManager(self.current_day)
        # Añadir salario del día anterior si no es el primer día
        if self.current_day > 1:
            self.player_wallet.add_daily_salary(self.current_day, 8.0)
    
    def handle_events(self):
        """Maneja eventos de entrada"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_running = False
                elif event.key == pygame.K_F1:
                    # F1 para mostrar coordenadas del mouse
                    mouse_pos = pygame.mouse.get_pos()
                    print(f"Coordenadas del mouse: x={mouse_pos[0]}, y={mouse_pos[1]}")
                elif event.key == pygame.K_SPACE:
                    self.advance_dialog()
                elif event.key == pygame.K_UP:
                    self.choice_selected = max(0, self.choice_selected - 1)
                elif event.key == pygame.K_DOWN:
                    seq = self.day_scene_manager.get_current_sequence()
                    if seq and seq.get_current_dialog():
                        dialog = seq.get_current_dialog()
                        if dialog.dialog_type.name == "CHOICE":
                            self.choice_selected = min(len(dialog.choices) - 1, self.choice_selected + 1)
                elif event.key == pygame.K_RETURN:
                    self.select_choice()
    
    def advance_dialog(self):
        """Avanza al siguiente diálogo"""
        if self.current_state == GameState.INTRO:
            self.current_state = GameState.PLAYING_DAY
            self.start_new_day()
            self.intro_shown = True
        
        elif self.current_state == GameState.PLAYING_DAY:
            if not self.day_scene_manager:
                return
            
            current_seq = self.day_scene_manager.get_current_sequence()
            if not current_seq:
                return
            
            # Si estamos en una escena de elección, no avanzamos
            current_dialog = current_seq.get_current_dialog()
            if current_dialog and current_dialog.dialog_type.name == "CHOICE":
                return
            
            # Avanzar al siguiente diálogo
            if not current_seq.next_dialog():
                # La secuencia actual terminó, pasar a la siguiente escena
                current_scene = self.day_scene_manager.current_scene
                
                # Determinar la siguiente escena
                scene_order = ["intro", "work", "transport", "phone", "home"]
                
                if current_scene in scene_order:
                    current_idx = scene_order.index(current_scene)
                    if current_idx < len(scene_order) - 1:
                        self.day_scene_manager.current_scene = scene_order[current_idx + 1]
                        self.day_scene_manager.dialog_index = 0
                    else:
                        # Ya terminaron todas las escenas estándar
                        # Esperar decisión en home
                        pass
                elif current_scene in ["gacha", "rest", "mom_visit"]:
                    # Después de una decisión, pasar al siguiente día
                    self.move_to_next_day()
        
        elif self.current_state == GameState.SHOWING_ENDING:
            if self.current_ending_sequence:
                if self.ending_dialog_index < len(self.current_ending_sequence.dialogs) - 1:
                    self.ending_dialog_index += 1
                else:
                    # Final completado
                    self.game_running = False
    
    def select_choice(self):
        """Selecciona una opción del menú"""
        seq = self.day_scene_manager.get_current_sequence()
        if seq:
            dialog = seq.get_current_dialog()
            if dialog and dialog.dialog_type.name == "CHOICE" and self.choice_selected < len(dialog.choices):
                _, action = dialog.choices[self.choice_selected]
                
                # Log de decisión
                self.decision_log[self.current_day] = action
                
                # Procesar decisión
                if action == "play_gacha":
                    self.gacha_uses_count += 1
                    self.days_with_gacha.append(self.current_day)
                    self.player_wallet.spend_on_gacha(2.0)
                    char = self.gacha_system.pull_lucky_block()[0]
                    self.player_inventory.add_character(char)
                    self.day_scene_manager.current_scene = "gacha"
                    self.day_scene_manager.dialog_index = 0  # Resetear índice de diálogo
                
                elif action == "rest":
                    self.days_rested.append(self.current_day)
                    self.day_scene_manager.current_scene = "rest"
                    self.day_scene_manager.dialog_index = 0  # Resetear índice de diálogo
                
                elif action == "visit_mom":
                    self.mom_visits += 1
                    self.player_wallet.gacha_money -= 3.0  # Costo del taxi
                    if self.player_wallet.gacha_money < 0:
                        self.player_wallet.gacha_money = 0
                    self.day_scene_manager.current_scene = "mom_visit"
                    self.day_scene_manager.dialog_index = 0  # Resetear índice de diálogo
                
                self.choice_selected = 0
    
    def move_to_next_day(self):
        """Pasa al siguiente día o al final"""
        if self.current_day < TOTAL_DAYS:
            self.current_day += 1
            self.start_new_day()
            self.choice_selected = 0
        else:
            # Juego terminado, determinar final
            self.determine_ending()
            self.current_state = GameState.SHOWING_ENDING
    
    def determine_ending(self):
        """Determina qué final se mostrará"""
        total_spent = self.player_wallet.spent_on_gacha
        
        # Final malo: si gastó mucho dinero
        if total_spent >= 5.0:
            self.current_ending_sequence = self.ending_sequence.get_ending("bad")
        # Final semi-bueno: si jugó gacha moderadamente y visitó a mamá
        elif self.gacha_uses_count <= 2 and self.mom_visits >= 1:
            self.current_ending_sequence = self.ending_sequence.get_ending("semi_good")
        # Otro caso: si pasó los 7 días sin hacer nada (poco realista, pero contemplado)
        else:
            self.current_ending_sequence = self.ending_sequence.get_ending("bad")
        
        self.ending_dialog_index = 0
    
    def update(self):
        """Actualiza la lógica del juego"""
        self.handle_events()
        self.render()
        self.screen.update()
    
    def render(self):
        """Renderiza el estado actual"""
        self.screen.clear()
        self.background_manager.render(self.screen.display)
        self.screen.render_hud(self.current_day, self.player_wallet.gacha_money, self.player_wallet.spent_on_gacha)
        
        if self.current_state == GameState.INTRO:
            self.render_intro()
        elif self.current_state == GameState.PLAYING_DAY:
            self.render_day_scene()
        elif self.current_state == GameState.SHOWING_ENDING:
            self.render_ending()
    
    def render_intro(self):
        """Renderiza escena de introducción"""
        self.background_manager.set_background("default")
        self.screen.render_text("Fernando's Gacha Reality", "title", x=WINDOW_WIDTH//2, y=150)
        self.screen.render_text("Una historia sobre ludopatía y sus consecuencias", "text", x=WINDOW_WIDTH//2, y=250)
        self.screen.render_text("", "text", x=WINDOW_WIDTH//2, y=320)
        self.screen.render_text("Fernando es un recepcionista de gimnasio con mal salario.", "small", x=WINDOW_WIDTH//2, y=370)
        self.screen.render_text("Su madre está en el hospital y necesita una operación cara.", "small", x=WINDOW_WIDTH//2, y=400)
        self.screen.render_text("¿Podrá ahorrar dinero o caerá en la trampa del gacha?", "small", x=WINDOW_WIDTH//2, y=430)
        self.screen.render_text("", "text", x=WINDOW_WIDTH//2, y=500)
        self.screen.render_text("Presiona ESPACIO para comenzar", "small", x=WINDOW_WIDTH//2, y=600)
    
    def render_day_scene(self):
        """Renderiza las escenas del día"""
        if not self.day_scene_manager:
            return
        
        # Obtener diálogo actual
        current_dialog = self.day_scene_manager.get_current_dialog()
        
        if not current_dialog:
            self.move_to_next_day()
            return
        
        # Renderizar fondo según la escena
        scene_bg_map = {
            "intro": "default",
            "work": "Fondo",  # Fondo.png es el gym
            "transport": "Transporte",  # Transporte.png es el transporte
            "phone": "Fondo_telefono",  # Fondo_telefono.png es cuando ve el celular
            "home": "Cuarto",  # Cuarto.png es la casa/cuarto
            "gacha": "Gacha sin nombre",  # Gacha sin nombre.png es la pantalla del juego
            "rest": "Cuarto",  # Descansar en casa
            "mom_visit": "Hospital fija",  # Hospital fija.png es la escena final
        }
        bg_name = scene_bg_map.get(self.day_scene_manager.current_scene, "default")
        self.background_manager.set_background(bg_name)
        
        # Renderizar todos los personajes de la escena
        # El personaje que habla se ilumina, los otros se oscurecen
        scene_characters = self.day_scene_manager.get_scene_characters()
        characters_info = []
        for char in scene_characters:
            # Solo iluminar al que está hablando actualmente
            is_speaking = (char == current_dialog.character) and (current_dialog.dialog_type.name != "CHOICE")
            characters_info.append((char, is_speaking))
        
        self.screen.render_all_scene_characters(characters_info)
        
        # Renderizar diálogo
        if current_dialog.character:
            self.screen.render_dialog_box(
                current_dialog.character,
                current_dialog.text,
                y_pos=500
            )
        else:
            # Narración también en cuadro, solo sin nombre de personaje
            self.screen.render_dialog_box(
                None,  # Sin personaje
                current_dialog.text,
                y_pos=500
            )
        
        # Renderizar opciones si corresponde
        if current_dialog.dialog_type.name == "CHOICE":
            self.screen.render_choices(current_dialog.choices, self.choice_selected)
        
        # Indicador de continuar
        if current_dialog.dialog_type.name == "NORMAL" or current_dialog.dialog_type.name == "NARRATION":
            self.screen.render_text("(Presiona ESPACIO para continuar)", "small", x=WINDOW_WIDTH//2, y=680)
    
    def render_ending(self):
        """Renderiza la secuencia de final"""
        if not self.current_ending_sequence:
            return
        
        self.background_manager.set_background("default")
        
        if self.ending_dialog_index < len(self.current_ending_sequence.dialogs):
            current_dialog = self.current_ending_sequence.dialogs[self.ending_dialog_index]
            
            # Renderizar sprite del personaje si existe
            if current_dialog.character:
                self.screen.render_character_sprite(current_dialog.character, True)
            
            if current_dialog.character:
                self.screen.render_dialog_box(
                    current_dialog.character,
                    current_dialog.text,
                    y_pos=500
                )
            else:
                # Narración también en cuadro en el ending
                self.screen.render_dialog_box(
                    None,  # Sin personaje
                    current_dialog.text,
                    y_pos=500
                )
        
        self.screen.render_text("(Presiona ESPACIO para continuar)", "small", x=WINDOW_WIDTH//2, y=680)
    
    def run(self):
        """Loop principal del juego"""
        try:
            print("Iniciando loop de juego...")
            while self.game_running:
                try:
                    self.update()
                except Exception as e:
                    print(f"Error en update: {e}")
                    import traceback
                    traceback.print_exc()
                    break
            print("Loop terminado")
        finally:
            print("Cerrando pygame...")
            self.screen.quit()
            print("Pygame cerrado")


if __name__ == "__main__":
    game = GameEngine()
    game.run()
