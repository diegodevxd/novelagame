"""
Motor gráfico y renderización con Pygame
"""
import os
import pygame
from config import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS, COLOR_BLACK, COLOR_WHITE,
    FONT_SIZE_TITLE, FONT_SIZE_TEXT, FONT_SIZE_SMALL
)


class Screen:
    """Maneja la pantalla y renderización básica"""
    
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Fernando's Gacha Reality")
        self.clock = pygame.time.Clock()
        # Aumentar tamaño de fuentes
        self.font_title = pygame.font.Font(None, 64)  # Aumentado de 48
        self.font_text = pygame.font.Font(None, 32)   # Aumentado de 24
        self.font_small = pygame.font.Font(None, 20)  # Aumentado de 16
        self.running = True
        
        # Cargar imagen del cuadro de selección
        self.choice_box_image = None
        try:
            self.choice_box_image = pygame.image.load("Fondos/cuadrodeseleccion.png")
            self.choice_box_image = pygame.transform.scale(self.choice_box_image, (650, 230))
        except Exception as e:
            print(f"Advertencia: No se pudo cargar la imagen del cuadro: {e}")
        
        # Cargar imagen del chat/burbuja de diálogo
        self.chat_bubble_image = None
        try:
            self.chat_bubble_image = pygame.image.load("Fondos/chatburbujas.png")
            # Escalar a tamaño apropiado para 1280x720: 1200 ancho x 200 alto
            self.chat_bubble_image = pygame.transform.scale(self.chat_bubble_image, (1200, 200))
        except Exception as e:
            print(f"Advertencia: No se pudo cargar la imagen del chat: {e}")
        
        # Cargar sprites de personajes
        self.character_sprites = {}
        self.load_character_sprites()
    
    def clear(self, color=COLOR_BLACK):
        """Limpia la pantalla con un color"""
        self.display.fill(color)
    
    def update(self):
        """Actualiza la pantalla"""
        pygame.display.flip()
        self.clock.tick(FPS)
    
    def load_character_sprites(self):
        """Carga los sprites de los personajes"""
        # Cargar sprites de la Jefa (Ale)
        try:
            ale_hablando = pygame.image.load("personajes/alehablando.png")
            ale_sin_hablar = pygame.image.load("personajes/alesinhablar.png")
            
            # Escalar a un tamaño apropiado (altura ~400 píxeles)
            height = 400
            width = int(ale_hablando.get_width() * (height / ale_hablando.get_height()))
            ale_hablando = pygame.transform.scale(ale_hablando, (width, height))
            ale_sin_hablar = pygame.transform.scale(ale_sin_hablar, (width, height))
            
            self.character_sprites["Jefa"] = {
                "hablando": ale_hablando,
                "sin_hablar": ale_sin_hablar
            }
        except Exception as e:
            print(f"Advertencia: No se pudieron cargar sprites de Jefa: {e}")
        
        # Cargar sprites del Compañero
        try:
            compa_hablando = pygame.image.load("personajes/compahablando.png")
            compa_sin_hablar = pygame.image.load("personajes/compasinhablar.png")
            
            # Escalar al mismo tamaño que la Jefa (altura ~400 píxeles)
            height = 400
            width = int(compa_hablando.get_width() * (height / compa_hablando.get_height()))
            compa_hablando = pygame.transform.scale(compa_hablando, (width, height))
            compa_sin_hablar = pygame.transform.scale(compa_sin_hablar, (width, height))
            
            self.character_sprites["Compañero"] = {
                "hablando": compa_hablando,
                "sin_hablar": compa_sin_hablar
            }
        except Exception as e:
            print(f"Advertencia: No se pudieron cargar sprites de Compañero: {e}")
    
    def render_character_sprite(self, character_name, is_speaking=False, position_x=50):
        """Renderiza el sprite del personaje en una posición específica.
        
        Args:
            character_name: nombre del personaje
            is_speaking: True si está hablando, False si está callado
            position_x: posición X en pantalla (50 = izquierda, 650 = derecha)
        """
        if character_name not in self.character_sprites:
            return
        
        sprites = self.character_sprites[character_name]
        sprite_key = "hablando" if is_speaking else "sin_hablar"
        
        if sprite_key in sprites:
            sprite = sprites[sprite_key]
            # Posicionar en X especificada, centrado verticalmente
            x = position_x
            y = (WINDOW_HEIGHT - sprite.get_height()) // 2
            self.display.blit(sprite, (x, y))
    
    def render_all_scene_characters(self, characters_info):
        """Renderiza todos los personajes de la escena con diferentes estados de iluminación.
        
        characters_info: lista de tuplas (character_name, is_speaking, position_x)
        Ejemplo: [("Jefa", True, 50), ("Compañero1", False, 600)]
        Si position_x no se proporciona, usa posición izquierda por defecto.
        """
        # Posiciones predeterminadas según cantidad de personajes
        positions = {
            1: [50],  # Un personaje: izquierda
            2: [50, 600],  # Dos personajes: izquierda y derecha
            3: [50, 350, 650]  # Tres personajes: izq, centro, der
        }
        
        num_chars = len(characters_info)
        pos_list = positions.get(num_chars, [50] * num_chars)
        
        for idx, (character_name, is_speaking) in enumerate(characters_info):
            position_x = pos_list[idx] if idx < len(pos_list) else 50
            self.render_character_sprite(character_name, is_speaking, position_x)
    
    def quit(self):
        """Cierra pygame"""
        pygame.quit()
        self.running = False
    
    def render_text_with_outline(self, text, font, color, x, y):
        """Renderiza texto con contorno negro"""
        # Renderizar contorno (negro alrededor)
        for adj_x in [-2, -1, 0, 1, 2]:
            for adj_y in [-2, -1, 0, 1, 2]:
                if adj_x != 0 or adj_y != 0:
                    outline_surface = font.render(text, True, COLOR_BLACK)
                    self.display.blit(outline_surface, (x + adj_x, y + adj_y))
        
        # Renderizar texto principal encima
        text_surface = font.render(text, True, color)
        self.display.blit(text_surface, (x, y))
    
    def render_text(self, text, font_type="text", color=COLOR_WHITE, x=640, y=360):
        """Renderiza un texto centrado con contorno"""
        font_map = {
            "title": self.font_title,
            "text": self.font_text,
            "small": self.font_small,
        }
        font = font_map.get(font_type, self.font_text)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        
        # Renderizar con contorno
        center_x = x - text_rect.width // 2
        center_y = y - text_rect.height // 2
        self.render_text_with_outline(text, font, color, center_x, center_y)
        
        return text_rect
    
    def render_dialog_box(self, character, text, y_pos=500):
        """Renderiza un cuadro de diálogo con degradado azul monocromático"""
        box_x = 40
        box_y = y_pos
        box_width = WINDOW_WIDTH - 80
        box_height = 180
        
        # Crear superficie con fondo degradado (azules monocromáticos)
        dialog_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        
        # Parte superior: Azul marino oscuro (50 píxeles)
        for y in range(50):
            # Degradado de azul marino oscuro a azul marino claro
            r = int(10 + (y / 50) * 40)  # 10 a 50
            g = int(40 + (y / 50) * 60)  # 40 a 100
            b = int(80 + (y / 50) * 80)  # 80 a 160
            pygame.draw.line(dialog_surface, (r, g, b, 255), (0, y), (box_width, y))
        
        # Centro: Degradado hacia azul más claro (80 píxeles)
        for y in range(50, 130):
            progress = (y - 50) / 80  # 0 a 1
            r = int(50 + progress * 70)   # 50 a 120
            g = int(100 + progress * 80)  # 100 a 180
            b = int(160 + progress * 60)  # 160 a 220
            pygame.draw.line(dialog_surface, (r, g, b, 255), (0, y), (box_width, y))
        
        # Parte inferior: Azul claro (50 píxeles)
        for y in range(130, box_height):
            progress = (y - 130) / 50  # 0 a 1
            r = int(120 + progress * 30)  # 120 a 150
            g = int(180 + progress * 20)  # 180 a 200
            b = int(220 - progress * 20)  # 220 a 200
            pygame.draw.line(dialog_surface, (r, g, b, 255), (0, y), (box_width, y))
        
        # Dibujar borde azul marino
        pygame.draw.rect(dialog_surface, (20, 60, 120, 255), dialog_surface.get_rect(), 3)
        
        # Blitear la superficie al display
        self.display.blit(dialog_surface, (box_x, box_y))
        
        # Nombre del personaje en la zona superior
        if character:
            self.render_text_with_outline(character, self.font_text, (100, 200, 255), 60, y_pos + 18)
        
        # Texto del diálogo en la zona central/inferior
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            current_line.append(word)
            line_text = " ".join(current_line)
            if self.font_text.size(line_text)[0] > WINDOW_WIDTH - 120:
                lines.append(" ".join(current_line[:-1]))
                current_line = [word]
        lines.append(" ".join(current_line))
        
        # Mostrar texto en múltiples líneas si es necesario
        for i, line in enumerate(lines[:2]):  # Máximo 2 líneas
            self.render_text_with_outline(line, self.font_text, COLOR_WHITE, 60, y_pos + 85 + i * 38)
    
    def render_choice_box(self, text, y_pos):
        """Renderiza un cuadro bonito para las opciones de selección"""
        # Crear cuadro con borde
        box_width = 600
        box_height = 60
        box_x = (WINDOW_WIDTH - box_width) // 2
        
        # Fondo del cuadro
        box_rect = pygame.Rect(box_x, y_pos, box_width, box_height)
        pygame.draw.rect(self.display, (30, 30, 60), box_rect)
        pygame.draw.rect(self.display, (100, 150, 255), box_rect, 3)
        
        return box_rect
    
    def render_choices(self, choices, selected_index=0):
        """Renderiza opciones de elección sobre la imagen del cuadro"""
        start_y = 280
        box_width = 650
        box_height = 230
        box_x = (WINDOW_WIDTH - box_width) // 2
        box_y = start_y - 30
        
        # Renderizar imagen del cuadro si existe
        if self.choice_box_image:
            self.display.blit(self.choice_box_image, (box_x, box_y))
        else:
            # Fallback si no existe la imagen
            box_rect = pygame.Rect(box_x, box_y, box_width, box_height)
            pygame.draw.rect(self.display, (60, 60, 100), box_rect)
            pygame.draw.rect(self.display, (100, 150, 255), box_rect, 3)
        
        # Renderizar opciones sobre la imagen
        for i, (text, _) in enumerate(choices):
            color = (255, 255, 0) if i == selected_index else COLOR_WHITE
            choice_text = f"→ {text}" if i == selected_index else f"  {text}"
            text_surface = self.font_text.render(choice_text, True, color)
            
            # Aplicar contorno
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    if dx*dx + dy*dy <= 4:
                        outline_surface = self.font_text.render(choice_text, True, (0, 0, 0))
                        self.display.blit(outline_surface, (640 - text_surface.get_width()//2 + dx, start_y + i * 70 + dy))
            
            # Texto principal centrado
            self.display.blit(text_surface, (640 - text_surface.get_width()//2, start_y + i * 70))
    
    def render_hud(self, day, money, gacha_spent):
        """Renderiza el HUD con información del jugador"""
        # Renderizar con contorno
        day_text = f"Día: {day}/7"
        money_text = f"Dinero: ${money:.2f}"
        spent_text = f"Gastado en Gacha: ${gacha_spent:.2f}"
        
        self.render_text_with_outline(day_text, self.font_small, COLOR_WHITE, 20, 20)
        self.render_text_with_outline(money_text, self.font_small, COLOR_WHITE, 20, 50)
        self.render_text_with_outline(spent_text, self.font_small, (255, 100, 100), 20, 80)


class BackgroundManager:
    """Gestiona los fondos del juego"""
    
    def __init__(self, fondos_path="Fondos"):
        self.backgrounds = {}
        self.current_bg = None
        self.load_backgrounds(fondos_path)
    
    def load_backgrounds(self, path):
        """Carga fondos desde la carpeta especificada"""
        try:
            if not os.path.exists(path):
                print(f"Advertencia: Carpeta '{path}' no encontrada")
                # Crear fondo de color por defecto
                self.backgrounds["default"] = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
                self.backgrounds["default"].fill(COLOR_BLACK)
                return
            
            file_count = 0
            for filename in os.listdir(path):
                if filename.endswith(('.png', '.jpg', '.jpeg')):
                    bg_name = filename.split('.')[0]
                    try:
                        img = pygame.image.load(os.path.join(path, filename))
                        img = pygame.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))
                        self.backgrounds[bg_name] = img
                        file_count += 1
                    except Exception as e:
                        print(f"Error loading {filename}: {e}")
            
            if file_count == 0:
                print(f"Advertencia: No se encontraron imágenes en '{path}'")
                self.backgrounds["default"] = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
                self.backgrounds["default"].fill(COLOR_BLACK)
            
        except Exception as e:
            print(f"Error loading backgrounds from {path}: {e}")
            # Crear un fondo de color por defecto
            self.backgrounds["default"] = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            self.backgrounds["default"].fill(COLOR_BLACK)
    
    def set_background(self, name):
        """Establece el fondo actual"""
        if name in self.backgrounds:
            self.current_bg = self.backgrounds[name]
        else:
            # Usar default si no existe
            self.current_bg = self.backgrounds.get("default")
    
    def render(self, surface):
        """Renderiza el fondo actual"""
        if self.current_bg:
            surface.blit(self.current_bg, (0, 0))
        else:
            surface.fill(COLOR_BLACK)
