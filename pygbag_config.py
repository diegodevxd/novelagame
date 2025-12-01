"""
Configuración específica para Pygbag (compilación a WebAssembly)
Este archivo se usa automáticamente cuando ejecutas: pygbag main.py
"""

# Pygbag es una herramienta que compila Pygame a WebAssembly
# Permitiendo que el juego se ejecute en navegadores web

# Para más información sobre Pygbag:
# https://github.com/pygame-web/pygbag

# Características:
# - Convierte código Python a WebAssembly
# - Soporta la mayoría de funcionalidades de Pygame
# - Se ejecuta localmente en el navegador (sin servidor)
# - Compatible con Chrome, Firefox, Safari, Edge

# El compilador de Pygbag genera automáticamente:
# 1. HTML wrapper
# 2. JavaScript glue code
# 3. WebAssembly binaries
# 4. Asset loader

# Notas importantes:
# - El primer build puede tomar varios minutos
# - Asegúrate de tener los fondos en la carpeta Fondos/
# - Si añades archivos nuevos, reinicia Pygbag
