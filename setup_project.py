"""
Script de instalación y configuración del proyecto
Ejecuta: python setup_project.py
"""
import subprocess
import sys
import os

def install_dependencies():
    """Instala las dependencias del proyecto"""
    print("=" * 60)
    print("INSTALANDO DEPENDENCIAS")
    print("=" * 60)
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("\n✓ Dependencias instaladas correctamente")
        return True
    except subprocess.CalledProcessError:
        print("\n✗ Error al instalar dependencias")
        return False

def create_backgrounds():
    """Crea fondos de ejemplo"""
    print("\n" + "=" * 60)
    print("CREANDO FONDOS DE EJEMPLO")
    print("=" * 60)
    
    try:
        subprocess.check_call([sys.executable, "create_backgrounds.py"])
        print("✓ Fondos creados correctamente")
        return True
    except subprocess.CalledProcessError:
        print("✗ Error al crear fondos")
        return False
    except FileNotFoundError:
        print("✗ No se encontró create_backgrounds.py")
        return False

def verify_setup():
    """Verifica que todo esté bien configurado"""
    print("\n" + "=" * 60)
    print("VERIFICANDO CONFIGURACIÓN")
    print("=" * 60)
    
    try:
        subprocess.check_call([sys.executable, "test_setup.py"])
        return True
    except subprocess.CalledProcessError:
        print("✗ Error en la verificación")
        return False

def print_next_steps():
    """Imprime los siguientes pasos"""
    print("\n" + "=" * 60)
    print("SIGUIENTE PASOS")
    print("=" * 60)
    print("\n1. Para jugar en escritorio:")
    print("   python main.py\n")
    print("2. Para jugar en navegador (requiere Pygbag):")
    print("   pip install pygbag")
    print("   pygbag main.py")
    print("   Luego abre http://localhost:8000 en tu navegador\n")
    print("3. Para más información, lee README.md")
    print("\n" + "=" * 60)

def main():
    """Ejecuta el setup completo"""
    print("\n" + "=" * 60)
    print("SETUP DEL PROYECTO: Fernando's Gacha Reality")
    print("=" * 60 + "\n")
    
    # Cambiar al directorio raíz del proyecto
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Ejecutar pasos
    success = True
    
    if not install_dependencies():
        success = False
    
    if not create_backgrounds():
        print("Advertencia: Puede que necesites crear fondos manualmente")
    
    if not verify_setup():
        success = False
    
    if success:
        print_next_steps()
        print("✓ Setup completado exitosamente")
    else:
        print("\n✗ Hubo problemas durante el setup")
        print("Por favor, revisa los errores anteriores")

if __name__ == "__main__":
    main()
