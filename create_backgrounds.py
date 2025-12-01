"""
Script para generar fondos de ejemplo si no existen
"""
import pygame
import os

def create_example_backgrounds():
    """Crea fondos de ejemplo para pruebas"""
    pygame.init()
    
    # Crear carpeta Fondos si no existe
    if not os.path.exists("Fondos"):
        os.makedirs("Fondos")
    
    WIDTH, HEIGHT = 1280, 720
    colors = {
        "gym.png": (200, 100, 50),           # Marrón (gimnasio)
        "transport.png": (100, 100, 100),   # Gris (transporte)
        "home.png": (150, 100, 200),        # Púrpura (hogar)
        "hospital.png": (200, 200, 200),    # Gris claro (hospital)
        "phone.png": (50, 50, 100),         # Azul oscuro (pantalla de teléfono)
        "gacha.png": (100, 50, 150),        # Púrpura oscuro (gacha)
        "default.png": (30, 30, 50),        # Negro azulado (por defecto)
    }
    
    for filename, color in colors.items():
        if not os.path.exists(f"Fondos/{filename}"):
            surface = pygame.Surface((WIDTH, HEIGHT))
            surface.fill(color)
            pygame.image.save(surface, f"Fondos/{filename}")
            print(f"✓ Creado: Fondos/{filename}")
        else:
            print(f"✓ Ya existe: Fondos/{filename}")
    
    pygame.quit()
    print("\nFondos de ejemplo creados/verificados correctamente.")

if __name__ == "__main__":
    create_example_backgrounds()
