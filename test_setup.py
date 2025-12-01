"""
Script de prueba para verificar que el proyecto está bien configurado
"""
import sys
import os

def test_structure():
    """Verifica la estructura del proyecto"""
    print("=" * 60)
    print("PRUEBA DE ESTRUCTURA DEL PROYECTO")
    print("=" * 60)
    
    required_files = [
        "main.py",
        "config.py",
        "requirements.txt",
        "README.md",
        "src/__init__.py",
        "src/game_engine.py",
        "src/game_systems.py",
        "src/graphics.py",
        "src/dialogs.py",
        "src/scenes.py",
    ]
    
    all_exist = True
    for file in required_files:
        exists = os.path.exists(file)
        status = "✓" if exists else "✗"
        print(f"{status} {file}")
        if not exists:
            all_exist = False
    
    print("\n" + "=" * 60)
    print("PRUEBA DE IMPORTACIONES")
    print("=" * 60)
    
    try:
        import pygame
        print("✓ pygame importado correctamente")
    except ImportError:
        print("✗ pygame no está instalado")
        all_exist = False
    
    try:
        from config import WINDOW_WIDTH, TOTAL_DAYS
        print("✓ config.py importado correctamente")
        print(f"  - Ancho de ventana: {WINDOW_WIDTH}")
        print(f"  - Total de días: {TOTAL_DAYS}")
    except ImportError as e:
        print(f"✗ Error importando config.py: {e}")
        all_exist = False
    
    try:
        from src.game_systems import PlayerWallet, GachaSystem
        wallet = PlayerWallet()
        print("✓ game_systems.py importado correctamente")
        print(f"  - Dinero inicial: ${wallet.gacha_money}")
    except ImportError as e:
        print(f"✗ Error importando game_systems.py: {e}")
        all_exist = False
    
    try:
        from src.graphics import Screen, BackgroundManager
        print("✓ graphics.py importado correctamente (sin inicializar)")
    except ImportError as e:
        print(f"✗ Error importando graphics.py: {e}")
        all_exist = False
    
    try:
        from src.dialogs import DialogManager
        print("✓ dialogs.py importado correctamente")
    except ImportError as e:
        print(f"✗ Error importando dialogs.py: {e}")
        all_exist = False
    
    try:
        from src.scenes import DaySceneManager, EndingSequence
        print("✓ scenes.py importado correctamente")
    except ImportError as e:
        print(f"✗ Error importando scenes.py: {e}")
        all_exist = False
    
    print("\n" + "=" * 60)
    
    if all_exist:
        print("✓ TODAS LAS PRUEBAS PASARON")
        print("\nPara ejecutar el juego:")
        print("  python main.py")
    else:
        print("✗ ALGUNAS PRUEBAS FALLARON")
        print("\nAsegúrate de:")
        print("  1. Instalar dependencias: pip install -r requirements.txt")
        print("  2. Ejecutar desde la carpeta raíz del proyecto")
    
    print("=" * 60)

if __name__ == "__main__":
    test_structure()
