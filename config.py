# Configuración general del juego
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60
TITLE = "Fernando's Gacha Reality"

# Colores
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (128, 128, 128)
COLOR_DARK_GRAY = (64, 64, 64)
COLOR_LIGHT_GRAY = (200, 200, 200)

# Sistema financiero
INITIAL_GACHA_MONEY = 20.0  # USD
DAILY_SALARY = 8.0  # USD ganados por día de trabajo
LUCKY_BLOCK_COST = 2.0  # USD por Lucky Block

# Mecánica de días
TOTAL_DAYS = 7
WORK_START_HOUR = 6  # 6 AM
WORK_END_HOUR = 15  # 3 PM

# Umbrales de gasto para determinar final
HIGH_SPENDING_THRESHOLD = 5  # USD gastados = final malo (madre muere)
MODERATE_SPENDING_THRESHOLD = 2  # USD gastados = final semi-bueno (visita madre)

# Personajes gacha posibles
GACHA_CHARACTERS = [
    {"name": "Elf Warrior", "rarity": "common", "weight": 40},
    {"name": "Dark Mage", "rarity": "rare", "weight": 30},
    {"name": "Holy Priest", "rarity": "rare", "weight": 20},
    {"name": "Shadow Assassin", "rarity": "epic", "weight": 7},
    {"name": "Celestial Dragon", "rarity": "legendary", "weight": 3},
]

# Fonts
FONT_SIZE_TITLE = 48
FONT_SIZE_TEXT = 24
FONT_SIZE_SMALL = 16
