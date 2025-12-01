# Fernando's Gacha Reality

## Descripción

Un videojuego visual novel estilo "Doki Doki Literature Club" pero enfocado en conciencia sobre la ludopatía con juegos gacha.

### Historia

Fernando es un recepcionista de gimnasio con un salario muy bajo y una jefa explotadora. Su madre está en el hospital y necesita una operación cara. Durante 7 días, Fernando debe decidir si ceder a la tentación de los juegos gacha o ahorrar dinero para ayudar a su madre.

### Mecánicas Principales

- **7 Días de gameplay**: Cada día Fernando trabaja de 6 AM a 3 PM ganando $8 USD
- **Sistema de Dinero**: Inicia con $20 USD, cada Lucky Block cuesta $2
- **Sistema Gacha**: Abre Lucky Blocks para obtener personajes coleccionables
- **Decisiones**: Cada tarde en casa, elige entre:
  - Jugar Gacha (gastar $2)
  - Descansar/Ahorrar dinero
  - Visitar a mamá en el hospital ($3 en taxi)
- **Finales múltiples**:
  - **Final Malo**: Si gastas mucho dinero en gacha, tu madre muere sin poder pagar la operación
  - **Final Semi-bueno**: Si jugas gacha moderadamente pero visitas a mamá, estarás a su lado cuando parta

## Instalación

### Requisitos
- Python 3.7+
- pip (gestor de paquetes Python)

### Pasos

1. Clona o descarga el proyecto:
```bash
cd novelagacha
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

### Modo Escritorio (Pygame)

Ejecuta el juego directamente:
```bash
python main.py
```

### Modo Web (HTML5 con Pygbag)

1. Asegúrate de tener pygbag instalado:
```bash
pip install pygbag
```

2. Ejecuta el juego en modo web:
```bash
pygbag main.py
```

3. Abre tu navegador en `http://localhost:8000`

## Controles

- **ESPACIO**: Avanza en los diálogos / Comienza el juego
- **ARRIBA/ABAJO**: Navega opciones de menú
- **ENTER**: Selecciona una opción
- **ESC**: Salir del juego

## Estructura del Proyecto

```
novelagacha/
├── main.py                 # Punto de entrada del juego
├── config.py              # Configuración general
├── requirements.txt       # Dependencias Python
├── README.md             # Este archivo
├── Fondos/               # Fondos/backgrounds del juego
├── assets/
│   ├── sprites/          # Sprites de personajes
│   ├── music/            # Música y sonidos
│   └── gacha_characters/ # Imágenes de personajes gacha
└── src/
    ├── graphics.py       # Motor gráfico y renderización
    ├── game_systems.py   # Sistema de dinero, gacha, inventario
    ├── dialogs.py        # Motor de diálogos
    ├── scenes.py         # Escenas y secuencias narrativas
    └── game_engine.py    # Motor principal del juego
```

## Contenido del Juego

### Personajes
- **Fernando**: Protagonista, recepcionista de gym
- **Jefa**: Personaje antagonista, explotadora
- **Compañeros**: Personajes secundarios, tóxicos
- **Madre**: Personaje central, motivación del jugador

### Personajes Gacha (Lucky Blocks)
- Elf Warrior (Común)
- Dark Mage (Raro)
- Holy Priest (Raro)
- Shadow Assassin (Épico)
- Celestial Dragon (Legendario)

### Escenas Diarias
1. **Introducción del día**
2. **Trabajo en el gym** (6 AM - 3 PM)
3. **Transporte a casa**
4. **Casa - Punto de decisión** (3 opciones)
5. **Consecuencias de la decisión**
6. **Final** (después de 7 días)

## Sistemas de Juego

### Sistema Financiero
- Salario diario: $8 USD
- Dinero inicial: $20 USD
- Costo Lucky Block: $2 USD
- Costo visitar mamá: $3 USD (taxi)

### Sistema de Finales
- **Final Malo**: Total gastado ≥ $5
- **Final Semi-bueno**: Total gastado < $5 AND visitas a mamá ≥ 1

### Temática
El juego explora:
- Adicción a juegos gacha
- Impacto de la ludopatía en relaciones personales
- Consecuencias financieras de las decisiones
- Importancia del tiempo con seres queridos
- Manipulación psicológica en videojuegos

## Desarrollo Futuro

Características planeadas:
- [ ] Sprites de personajes animados
- [ ] Sistema de música y sonido
- [ ] Más variedad en diálogos dinámicos
- [ ] Más personajes gacha
- [ ] Sistema de guardado/carga
- [ ] Más finales alternativos
- [ ] Modo sin censura con escenas más fuertes
- [ ] Localización a otros idiomas

## Notas para Contribuidores

El código está estructurado de forma modular:
- **game_systems.py**: Lógica de juego pura
- **dialogs.py**: Narrativa y diálogos
- **graphics.py**: Renderización
- **scenes.py**: Secuencias de escenas
- **game_engine.py**: Integración de todo

## Licencia

Este proyecto es de código abierto. Úsalo libremente.

## Autor

Creado como proyecto de conciencia sobre ludopatía en juegos gacha.

---

**Advertencia**: Este juego contiene temas sensibles como muerte, enfermedad, y adicción. Es principalmente educativo.
