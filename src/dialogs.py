"""
Motor de diálogos y narrativa para visual novel
"""
from enum import Enum


class DialogType(Enum):
    NORMAL = 1
    CHOICE = 2
    NARRATION = 3


class Dialog:
    """Representa un diálogo individual"""
    
    def __init__(self, character, text, dialog_type=DialogType.NORMAL, choices=None):
        self.character = character  # Nombre del personaje o None para narración
        self.text = text
        self.dialog_type = dialog_type
        self.choices = choices or []  # Para diálogos con opciones
    
    def __repr__(self):
        return f"Dialog({self.character}: {self.text[:30]}...)"


class DialogSequence:
    """Secuencia de diálogos para una escena"""
    
    def __init__(self, scene_name):
        self.scene_name = scene_name
        self.dialogs = []
        self.current_index = 0
    
    def add_dialog(self, dialog):
        """Añade un diálogo a la secuencia"""
        self.dialogs.append(dialog)
    
    def add_narration(self, text):
        """Añade una narración (sin personaje)"""
        self.dialogs.append(Dialog(None, text, DialogType.NARRATION))
    
    def add_choice(self, character, text, choices):
        """Añade un diálogo con opciones"""
        self.dialogs.append(Dialog(character, text, DialogType.CHOICE, choices))
    
    def get_current_dialog(self):
        """Obtiene el diálogo actual"""
        if self.current_index < len(self.dialogs):
            return self.dialogs[self.current_index]
        return None
    
    def next_dialog(self):
        """Pasa al siguiente diálogo"""
        if self.current_index < len(self.dialogs) - 1:
            self.current_index += 1
            return True
        return False
    
    def is_finished(self):
        """Verifica si la secuencia ha terminado"""
        return self.current_index >= len(self.dialogs) - 1
    
    def reset(self):
        """Reinicia la secuencia"""
        self.current_index = 0


class DialogManager:
    """Gestor central de diálogos del juego"""
    
    def __init__(self):
        self.sequences = {}
    
    def register_sequence(self, sequence):
        """Registra una secuencia de diálogos"""
        self.sequences[sequence.scene_name] = sequence
    
    def get_sequence(self, scene_name):
        """Obtiene una secuencia por nombre"""
        return self.sequences.get(scene_name)
    
    def create_day_intro(self, day):
        """Crea introducción del día"""
        seq = DialogSequence(f"day_{day}_intro")
        seq.add_narration(f"📅 Día {day}/7")
        seq.add_narration(f"Fernando se despierta a las 6 AM para ir al trabajo...")
        return seq
    
    def create_work_scene(self, day):
        """Crea escena de trabajo"""
        seq = DialogSequence(f"day_{day}_work")
        seq.add_narration(f"Fernando llega al gimnasio. Es otro día en la recepción...")
        seq.add_dialog(Dialog("Boss", "¡Fernando! ¿Dónde estabas? Limpia la entrada AHORA", DialogType.NORMAL))
        seq.add_dialog(Dialog("Fernando", "Acabo de llegar jefa...", DialogType.NORMAL))
        seq.add_dialog(Dialog("Coworker", "Jajaja, te va a explotar de trabajo", DialogType.NORMAL))
        seq.add_narration("Trabajas durante 9 horas. Ganas $8 USD.")
        return seq
    
    def create_transport_scene(self, day):
        """Crea escena de transporte a casa"""
        seq = DialogSequence(f"day_{day}_transport")
        seq.add_narration("Subes al transporte público de regreso a casa...")
        seq.add_narration("Miras tu teléfono. Tienes $8 USD más en tu cuenta bancaria.")
        seq.add_narration("Pero también ves publicidades de Gacha Games...")
        return seq
    
    def create_home_scene(self, day):
        """Crea escena en casa (punto de decisión)"""
        seq = DialogSequence(f"day_{day}_home")
        seq.add_narration("Llegas a casa. Es hora de decidir qué hacer.")
        choices = [
            ("Jugar Gacha (Gastar $2)", "play_gacha"),
            ("Descansar (Ahorrar dinero)", "rest"),
            ("Visitar a mamá en el hospital", "visit_mom"),
        ]
        seq.add_choice("Fernando", "¿Qué hago esta noche?", choices)
        return seq
    
    def create_gacha_scene(self, day):
        """Crea escena de juego gacha"""
        seq = DialogSequence(f"day_{day}_gacha")
        seq.add_narration("Fernando abre su app de Gacha...")
        seq.add_narration("'Solo un Lucky Block no hace daño', piensa...")
        return seq
    
    def create_mom_scene(self, day):
        """Crea escena visitando a la madre"""
        seq = DialogSequence(f"day_{day}_mom_visit")
        seq.add_narration("Llegas al hospital...")
        seq.add_narration("Tu madre está en la cama.")
        seq.add_dialog(Dialog("Mother", "¡Fernando! ¿Cómo estuvo tu día?", DialogType.NORMAL))
        seq.add_dialog(Dialog("Fernando", "Bien mamá, muy cansado en el trabajo...", DialogType.NORMAL))
        seq.add_dialog(Dialog("Mother", "Cuídate hijo. Espero pronto poder salir de aquí.", DialogType.NORMAL))
        return seq
