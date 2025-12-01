"""
Archivo principal del juego
"""
import sys
from src.game_engine import GameEngine


def main():
    """Función principal"""
    try:
        print("Iniciando Fernando's Gacha Reality...")
        game = GameEngine()
        print(f"Estado inicial: {game.current_state}")
        print(f"Día inicial: {game.current_day}")
        print("Entrando al loop principal...")
        game.run()
        print("Juego terminado correctamente")
    except KeyboardInterrupt:
        print("\nJuego interrumpido por el usuario.")
        sys.exit(0)
    except Exception as e:
        print(f"Error en el juego: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
