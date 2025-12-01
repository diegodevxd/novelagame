"""
Ejemplos de Extensión - Cómo añadir contenido a Fernando's Gacha Reality
"""

# =============================================================================
# 1. AÑADIR NUEVOS PERSONAJES GACHA
# =============================================================================

# Abre config.py y modifica la lista GACHA_CHARACTERS:

"""
GACHA_CHARACTERS = [
    {"name": "Elf Warrior", "rarity": "common", "weight": 40},
    {"name": "Dark Mage", "rarity": "rare", "weight": 30},
    {"name": "Holy Priest", "rarity": "rare", "weight": 20},
    {"name": "Shadow Assassin", "rarity": "epic", "weight": 7},
    {"name": "Celestial Dragon", "rarity": "legendary", "weight": 3},
    
    # AÑADE AQUÍ:
    {"name": "Fire Knight", "rarity": "rare", "weight": 25},
    {"name": "Frost Mage", "rarity": "epic", "weight": 8},
    {"name": "Time Guardian", "rarity": "legendary", "weight": 2},
]

# weight: probabilidad (de 100). Los pesos se normalizan automáticamente
# rarity: common, rare, epic, legendary (solo visual)
"""

# =============================================================================
# 2. CAMBIAR DINERO Y COSTOS
# =============================================================================

# config.py:

"""
INITIAL_GACHA_MONEY = 30.0  # Más dinero inicial
DAILY_SALARY = 10.0         # Mejor salario
LUCKY_BLOCK_COST = 1.5      # Gacha más barato
HIGH_SPENDING_THRESHOLD = 10 # Más tolerancia antes del final malo
"""

# =============================================================================
# 3. AÑADIR NUEVAS ESCENAS O DIÁLOGOS
# =============================================================================

# src/scenes.py, función setup_day_sequences():

"""
def setup_day_sequences(self):
    # ... código existente ...
    
    # Añadir nueva escena:
    lunch = DialogSequence(f"day_{self.day}_lunch")
    lunch.add_narration("Fernando se toma su descanso de 1 hora...")
    lunch.add_dialog(Dialog("Jefa", "¿Que ya te vas? Ni 30 minutos pasó!", DialogType.NORMAL))
    self.dialog_sequences["lunch"] = lunch
    
    # Modificar flujo en home para incluir lunch
    # (ver game_engine.py, método render_day_scene)
"""

# =============================================================================
# 4. CREAR FINALES ALTERNATIVOS
# =============================================================================

# src/scenes.py, clase EndingSequence:

"""
def setup_endings(self):
    # ... code ...
    
    # Nuevo final: mejor final donde salvas a tu madre
    best = DialogSequence("best_ending")
    best.add_narration("========= FINAL: SALVADOR ==========")
    best.add_narration("Fernando logró no gastar dinero en gacha.")
    best.add_narration("Trabajó y ahorró cada centavo.")
    best.add_narration("Su madre se recuperó completamente.")
    best.add_narration("Y juntos empezaron una vida nueva,")
    best.add_narration("lejos de la tentación de los videojuegos.")
    self.sequences["best"] = best
"""

# Luego en game_engine.py, determine_ending():

"""
def determine_ending(self):
    total_spent = self.player_wallet.spent_on_gacha
    
    # Final mejor
    if total_spent == 0.0:
        self.current_ending_sequence = self.ending_sequence.get_ending("best")
    # ... resto de lógica ...
"""

# =============================================================================
# 5. AÑADIR MÚSICA Y SONIDOS
# =============================================================================

# Primero: Coloca archivos .mp3 o .ogg en assets/music/

# Luego, crea src/audio.py:

"""
import pygame
import os

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.music_path = "assets/music"
        self.load_music()
    
    def load_music(self):
        for filename in os.listdir(self.music_path):
            if filename.endswith(('.mp3', '.ogg', '.wav')):
                key = filename.replace('.mp3', '').replace('.ogg', '').replace('.wav', '')
                self.sounds[key] = os.path.join(self.music_path, filename)
    
    def play(self, sound_name):
        if sound_name in self.sounds:
            sound = pygame.mixer.Sound(self.sounds[sound_name])
            sound.play()
    
    def play_music(self, track_name, loops=-1):
        if track_name in self.sounds:
            pygame.mixer.music.load(self.sounds[track_name])
            pygame.mixer.music.play(loops)

# En game_engine.py:
# self.audio_manager = AudioManager()
# self.audio_manager.play_music("menu_theme")
"""

# =============================================================================
# 6. AÑADIR SPRITES DE PERSONAJES
# =============================================================================

# Coloca imágenes en assets/sprites/

# Luego crea una clase SpriteManager en src/graphics.py:

"""
class SpriteManager:
    def __init__(self, sprites_path="assets/sprites"):
        self.sprites = {}
        self.load_sprites(sprites_path)
    
    def load_sprites(self, path):
        if os.path.exists(path):
            for filename in os.listdir(path):
                if filename.endswith(('.png', '.jpg')):
                    sprite_name = filename.split('.')[0]
                    img = pygame.image.load(os.path.join(path, filename))
                    self.sprites[sprite_name] = img
    
    def render_sprite(self, surface, sprite_name, x, y):
        if sprite_name in self.sprites:
            surface.blit(self.sprites[sprite_name], (x, y))
"""

# =============================================================================
# 7. SISTEMA DE GUARDADO Y CARGA
# =============================================================================

# Crea src/save_system.py:

"""
import json
import os

class SaveSystem:
    def __init__(self):
        self.save_dir = "saves"
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
    
    def save_game(self, filename, game_engine):
        save_data = {
            "day": game_engine.current_day,
            "money": game_engine.player_wallet.gacha_money,
            "spent": game_engine.player_wallet.spent_on_gacha,
            "gacha_count": game_engine.gacha_uses_count,
            "mom_visits": game_engine.mom_visits,
            "decisions": game_engine.decision_log,
        }
        
        with open(os.path.join(self.save_dir, filename + ".json"), "w") as f:
            json.dump(save_data, f, indent=2)
    
    def load_game(self, filename):
        with open(os.path.join(self.save_dir, filename + ".json"), "r") as f:
            return json.load(f)
"""

# =============================================================================
# 8. MODIFICAR PALETA DE COLORES
# =============================================================================

# config.py:

"""
# Tema oscuro/ciberpunk
COLOR_PRIMARY = (255, 0, 255)   # Magenta
COLOR_SECONDARY = (0, 255, 255) # Cian
COLOR_BG = (20, 20, 40)         # Azul muy oscuro

# O tema pastel
COLOR_PRIMARY = (255, 182, 193)   # Rosa pastel
COLOR_SECONDARY = (173, 216, 230) # Azul pastel
COLOR_BG = (240, 248, 255)        # Alice blue
"""

# =============================================================================
# 9. SISTEMA DE ESTADÍSTICAS
# =============================================================================

# Añade a src/game_systems.py:

"""
class GameStats:
    def __init__(self):
        self.total_playtime = 0
        self.endings_reached = {}
        self.times_played = 0
    
    def record_ending(self, ending_type):
        if ending_type not in self.endings_reached:
            self.endings_reached[ending_type] = 0
        self.endings_reached[ending_type] += 1
    
    def get_stats_summary(self):
        return f"Total juegos: {self.times_played}\\n"
               f"Finales alcanzados: {len(self.endings_reached)}"
"""

# =============================================================================
# 10. TESTEAR TUS CAMBIOS
# =============================================================================

# Siempre ejecuta antes de cambios grandes:

"""
python test_setup.py  # Verifica que no hay errores de importación
python main.py        # Prueba el juego completo
"""

# =============================================================================
# REFERENCIA RÁPIDA DE ARCHIVOS
# =============================================================================

"""
config.py              - Constantes y configuración global
src/game_systems.py    - Dinero, gacha, inventario
src/dialogs.py         - Motor de diálogos
src/scenes.py          - Escenas y narrativa del juego
src/graphics.py        - Renderización y gráficos
src/game_engine.py     - Loop principal y lógica del juego
main.py                - Punto de entrada
"""

# =============================================================================
# ESTRUCTURA RECOMENDADA PARA NUEVAS CARACTERÍSTICAS
# =============================================================================

"""
1. Planifica qué necesitas (ej: sistema de logros)
2. Crea un nuevo módulo (ej: src/achievements.py)
3. Implementa las clases/funciones
4. Importa en game_engine.py
5. Integra en el loop principal (game_engine.py)
6. Prueba y depura
7. Comenta bien tu código
8. Actualiza README.md si es necesario
"""

# =============================================================================
# TIPS DE DESARROLLO
# =============================================================================

"""
- Usa nombres descriptivos para variables y funciones
- Comenta código complejo
- Mantén funciones pequeñas y enfocadas
- Usa enums para estados (como se hace con GameState)
- Centraliza configuración en config.py
- Evita hardcoding de números mágicos
- Estructura el código de forma modular
- Prueba cambios incrementalmente
- Usa git para versionado (opcional pero recomendado)
"""
