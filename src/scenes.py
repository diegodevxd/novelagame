"""
Gestor mejorado de estados y escenas del juego
"""
from enum import Enum
from src.dialogs import DialogSequence, Dialog, DialogType


class SceneState(Enum):
    """Estados dentro de una escena"""
    DIALOG = 1
    CHOICE = 2
    TRANSITION = 3
    FINISHED = 4


class DaySceneManager:
    """Gestor de escenas para cada día (trabajo, transporte, casa)"""
    
    def __init__(self, day_number):
        self.day = day_number
        self.current_scene = "intro"  # Comenzar con intro
        self.dialog_sequences = {}
        self.dialog_index = 0
        self.choice_selected = 0
        self.setup_day_sequences()
    
    def setup_day_sequences(self):
        """Configura todas las secuencias de diálogos del día"""
        
        # Intro del día
        intro = DialogSequence(f"day_{self.day}_intro")
        intro.add_narration(f"========= DÍA {self.day}/7 =========")
        intro.add_narration("6:00 AM - Fernando se despierta para ir al trabajo...")
        self.dialog_sequences["intro"] = intro
        
        # Escena de trabajo - varía según el día
        work = DialogSequence(f"day_{self.day}_work")
        work.add_narration("Fernando llega al gimnasio como recepcionista...")
        
        if self.day == 1:
            work.add_dialog(Dialog("Jefa", "¡Fernando! ¿Dónde estabas? Mueve ese trasero", DialogType.NORMAL))
            work.add_dialog(Dialog("Fernando", "(Internamente: Ya llegué hace 5 minutos...)", DialogType.NORMAL))
            work.add_dialog(Dialog("Compañero", "Jajaja, la jefa está de malas hoy", DialogType.NORMAL))
            work.add_narration("Es tu primer día y la jefa ya te está acosando.")
            work.add_narration("Este trabajo promete ser tan emocionante como una clase de pilates aburrida.")
        elif self.day == 2:
            work.add_dialog(Dialog("Compañero", "Oye Fernando, ¿viste el evento gacha de hoy?", DialogType.NORMAL))
            work.add_dialog(Dialog("Fernando", "No, ¿qué tiene?", DialogType.NORMAL))
            work.add_dialog(Dialog("Compañero", "¡Hay un personaje legendario! Solo 0.3% de probabilidad.", DialogType.NORMAL))
            work.add_narration("Los compañeros no hablan de nada más que de gacha...")
            work.add_narration("Te das cuenta de que estás siendo influenciado.")
        elif self.day == 3:
            work.add_dialog(Dialog("Jefa", "Fernando, ¿terminaste de limpiar la zona de pesas?", DialogType.NORMAL))
            work.add_dialog(Dialog("Fernando", "Ya casi, jefa...", DialogType.NORMAL))
            work.add_dialog(Dialog("Jefa", "¿'Ya casi'? Tienes que ser más rápido.", DialogType.NORMAL))
            work.add_narration("La jefa nunca está satisfecha.")
            work.add_narration("Trabajas más rápido, pero te duelen los pies.")
        elif self.day == 4:
            work.add_dialog(Dialog("Compañero", "Fernando, te veo cansado, hermano", DialogType.NORMAL))
            work.add_dialog(Dialog("Fernando", "Mi mamá está en el hospital. Esto es estresante.", DialogType.NORMAL))
            work.add_dialog(Dialog("Compañero", "Uff, lo siento. Espero que se mejore.", DialogType.NORMAL))
            work.add_narration("Por un momento, alguien en el trabajo muestra empatía.")
            work.add_narration("Pero la realidad sigue siendo dura.")
        elif self.day == 5:
            work.add_dialog(Dialog("Miembro", "¡Oye! ¿Por qué no hay toallas limpias?", DialogType.NORMAL))
            work.add_dialog(Dialog("Fernando", "Las acabo de cambiar hace 30 minutos...", DialogType.NORMAL))
            work.add_narration("Los miembros del gimnasio son imposibles de complacer.")
            work.add_narration("Te prometes a ti mismo que nunca serás así de exigente.")
        elif self.day == 6:
            work.add_dialog(Dialog("Compañero", "Oye, salimos del trabajo temprano hoy. ¿Vienes a tomar algo?", DialogType.NORMAL))
            work.add_dialog(Dialog("Fernando", "No puedo, tengo que ahorrar cada centavo...", DialogType.NORMAL))
            work.add_narration("Mientras tus compañeros salen a divertirse, tú sigues aquí.")
            work.add_narration("Empiezas a sentir que te estás perdiendo la vida.")
        else:  # Día 7
            work.add_dialog(Dialog("Jefa", "Fernando, hoy es tu último día aquí.", DialogType.NORMAL))
            work.add_dialog(Dialog("Fernando", "¿Qué? ¿Me estás despidiendo?", DialogType.NORMAL))
            work.add_dialog(Dialog("Jefa", "El negocio está mal. Tengo que reducir personal.", DialogType.NORMAL))
            work.add_narration("¡No lo puedo creer! Justo cuando más lo necesitabas...")
            work.add_narration("Este es tu último día de trabajo. Sin ingreso, solo lo que ahorres.")
        
        work.add_narration("Trabajas 9 horas sin descanso adecuado...")
        work.add_narration("Atiendes miembros molestos, limpias, haces tareas administrativas...")
        work.add_narration("3:00 PM - Tu turno termina. Ganas $8 USD.")
        self.dialog_sequences["work"] = work
        
        # Transporte - varía según el día
        transport = DialogSequence(f"day_{self.day}_transport")
        transport.add_narration("3:15 PM - Subes al transporte público de regreso a casa...")
        
        if self.day <= 2:
            transport.add_narration("Estás exhausto. Miras tu teléfono.")
            transport.add_narration("Tu cuenta bancaria ahora tiene más dinero.")
            transport.add_narration("Pero también ves un anuncio: 'GACHA PREMIUM - ¡Gana personajes épicos ahora!'")
        elif self.day == 3:
            transport.add_narration("En el transporte, una persona juega gacha frente a ti.")
            transport.add_narration("'¡Legendario!' grita emocionado.")
            transport.add_narration("Ves cómo la gente se vuelve adicta a este juego...")
            transport.add_narration("Y te das cuenta de que tú también empiezas a serlo.")
        elif self.day == 4:
            transport.add_narration("Escuchas a dos personas hablando:")
            transport.add_narration("'Gasté $500 el mes pasado en gacha y no tengo dinero para comer'")
            transport.add_narration("La otra persona solo ríe. 'Bienvenido al club.'")
            transport.add_narration("Te pones a pensar si realmente necesitas ese dinero para tu mamá...")
        elif self.day == 5:
            transport.add_narration("Ves a un niño en el transporte jugando gacha.")
            transport.add_narration("Su madre le quita el teléfono: 'Ya gastaste el dinero de la comida'")
            transport.add_narration("El niño llora. Te sientes mal.")
            transport.add_narration("¿Será que eso será Fernando en el futuro?")
        elif self.day == 6:
            transport.add_narration("Apenas tienes energía para moverte.")
            transport.add_narration("Tu cuerpo está destruido de trabajar.")
            transport.add_narration("Solo quieres llegar a casa y descansar...")
            transport.add_narration("Pero el teléfono sigue tentándote.")
        else:  # Día 7
            transport.add_narration("Es tu último día trabajando. No sabes qué hacer con tu vida.")
            transport.add_narration("Mirás tus ahorros: $X USD")
            transport.add_narration("Piensas en tu mamá. Piensas en los personajes que no tienes.")
            transport.add_narration("Piensas en tus decisiones.")
        
        transport.add_narration("Sientes la tentación...")
        self.dialog_sequences["transport"] = transport
        
        # Escena del teléfono - Ver la pantalla del celular
        phone = DialogSequence(f"day_{self.day}_phone")
        phone.add_narration("Fernando saca su teléfono del bolsillo...")
        
        if self.day == 1:
            phone.add_narration("Ve notificaciones: 10 nuevas en la app de gacha")
            phone.add_narration("'¡Evento especial! Personaje limitado esta semana'")
            phone.add_narration("Su corazón late rápido. Solo por una vez...")
        elif self.day == 2:
            phone.add_narration("La app muestra: 'Han pasado 24 horas'")
            phone.add_narration("'¡Lucky block gratis disponible! Haz clic aquí'")
            phone.add_narration("Fernando piensa: 'Bueno, es gratis...'")
            phone.add_narration("Pero no es totalmente gratis. La primera es siempre gratis para enganchar.")
        elif self.day == 3:
            phone.add_narration("Ve que un amigo compartió su colección de personajes épicos")
            phone.add_narration("15 personajes legendarios. Fernando tiene 2.")
            phone.add_narration("Se siente inferior. Se siente perdedor.")
            phone.add_narration("¿Cuánto habrá gastado ese tipo?")
        elif self.day == 4:
            phone.add_narration("La app sugiere: 'Compra $20 de gemas ahora - 50% de descuento'")
            phone.add_narration("Fernando mira su saldo. Tiene $28 USD.")
            phone.add_narration("Sería solo $10. Apenas notaría la diferencia...")
            phone.add_narration("Pero su mamá está en el hospital. Necesita ese dinero.")
        elif self.day == 5:
            phone.add_narration("Fernando ve su colección. Ha gastado $10 en total.")
            phone.add_narration("Tiene 6 personajes únicos. Se siente bien.")
            phone.add_narration("Pero la app dice: 'Personaje nuevo + Rare. Solo hoy'")
            phone.add_narration("¿$2 más? ¿Qué daño puede hacer?")
        elif self.day == 6:
            phone.add_narration("Fernando mira cuánto ha gastado esta semana.")
            phone.add_narration("$14 USD. Una semana completa de trabajo casi se fue.")
            phone.add_narration("¿Y qué tiene que mostrar? Personajes de papel en una app.")
            phone.add_narration("La tentación sigue. Siempre sigue.")
        else:  # Día 7
            phone.add_narration("Fernando ve la notificación final:")
            phone.add_narration("'¡Personaje legendario! ÚLTIMAS HORAS'")
            phone.add_narration("Mira su saldo. Mira su colección.")
            phone.add_narration("Todo lo que hizo esta semana resume en este momento.")
        
        self.dialog_sequences["phone"] = phone
        
        # Casa (punto crítico de decisión)
        home = DialogSequence(f"day_{self.day}_home")
        home.add_narration("4:00 PM - Llegas a casa...")
        home.add_narration("Estás cansado pero todavía hay tiempo por delante.")
        home.add_narration("En tu mesita está tu teléfono parpadeando con notificaciones de gacha...")
        home.add_narration("También recibes un mensaje: 'Mamá - Hola hijo, ¿cómo estuvo tu día?'")
        home.add_choice("Fernando (Pensando)", "¿Qué hago esta noche?", [
            ("Jugar Gacha - Gastar $2 USD", "play_gacha"),
            ("Descansar y Ahorrar", "rest"),
            ("Visitar a mamá en el hospital", "visit_mom"),
        ])
        self.dialog_sequences["home"] = home
        
        # Escena gacha
        gacha = DialogSequence(f"day_{self.day}_gacha")
        gacha.add_narration("Fernando abre su aplicación de gacha...")
        gacha.add_narration("'Solo un Lucky Block no hace daño', piensa.")
        gacha.add_narration("$2 USD gastados...")
        gacha.add_narration("*Sound: Lucky Block abiéndose*")
        gacha.add_narration("¡Obtuviste un nuevo personaje!")
        gacha.add_narration("Fernando sonríe. Se siente bien por un momento.")
        gacha.add_narration("Pero luego piensa en su madre...")
        gacha.add_narration("Se va a dormir mirando su colección de personajes.")
        self.dialog_sequences["gacha"] = gacha
        
        # Escena visita a mamá
        mom_visit = DialogSequence(f"day_{self.day}_mom_visit")
        mom_visit.add_narration("Fernando toma un taxi al hospital (cuesta $3 USD).")
        mom_visit.add_narration("Llega a la habitación de su madre...")
        if self.day == 7:
            # Última visita - escena emotiva
            mom_visit.add_narration("Su madre está más débil de lo que la recuerda.")
            mom_visit.add_dialog(Dialog("Madre", "¡Fernando! Viniste...", DialogType.NORMAL))
            mom_visit.add_dialog(Dialog("Fernando", "Mamá, claro que vine. ¿Cómo te sientes?", DialogType.NORMAL))
            mom_visit.add_narration("Su madre toma su mano débilmente.")
            mom_visit.add_dialog(Dialog("Madre", "He estado muy preocupada por ti, hijo. Espero que no estés gastando dinero en esas cosas...", DialogType.NORMAL))
            mom_visit.add_dialog(Dialog("Fernando", "No mamá, estoy ahorrando. Pronto te sacaré de aquí.", DialogType.NORMAL))
            mom_visit.add_narration("(Es una mentira piadosa)")
        else:
            mom_visit.add_dialog(Dialog("Madre", "¡Mi hijo! ¿Cómo fue tu día en el trabajo?", DialogType.NORMAL))
            mom_visit.add_dialog(Dialog("Fernando", "Mamá, estuvo agotador. Pero aquí estoy contigo.", DialogType.NORMAL))
            mom_visit.add_narration("Pasen 2 horas juntos. Tu madre se ve más fuerte cuando hablan.")
        
        mom_visit.add_narration("Fernando sale del hospital con el corazón pesado.")
        self.dialog_sequences["mom_visit"] = mom_visit
        
        # Escena descansar - varía según el día
        rest = DialogSequence(f"day_{self.day}_rest")
        
        if self.day == 1:
            rest.add_narration("Fernando decide simplemente descansar.")
            rest.add_narration("Se relaja viendo películas, duerme bien.")
            rest.add_narration("Se ahorra el dinero y la energía emocional.")
        elif self.day == 2:
            rest.add_narration("Descansas en casa, pero sigues pensando en el gacha.")
            rest.add_narration("Ves videos de streamers abriéndolo y ganando personajes épicos.")
            rest.add_narration("La tentación nunca se va completamente.")
        elif self.day == 3:
            rest.add_narration("Duermes profundamente, es lo que necesitabas.")
            rest.add_narration("Soñás con tu mamá, sonriendo y sana.")
            rest.add_narration("Al despertar, recuerdas por qué estás ahorrando.")
        elif self.day == 4:
            rest.add_narration("Ves a tus amigos saliendo de fiesta.")
            rest.add_narration("Ellos no tienen que cuidar a nadie. Ellos solo disfrutan.")
            rest.add_narration("Pero tú tienes responsabilidades. Así que descansas solo.")
        elif self.day == 5:
            rest.add_narration("Tu cuerpo necesita recuperarse del cansancio extremo.")
            rest.add_narration("Duermes casi 12 horas sin despertar.")
            rest.add_narration("Es lo mejor que has hecho esta semana.")
        elif self.day == 6:
            rest.add_narration("Ya casi termina. Un poco más y llegarás al final de la semana.")
            rest.add_narration("Descansas sabiendo que mañana todo habrá acabado.")
            rest.add_narration("Pero, ¿qué habrá pasado para entonces?")
        else:  # Día 7
            rest.add_narration("Es tu último día. Descansas sabiendo que ya no habrá más ingresos.")
            rest.add_narration("Solo tienes lo que ahorraste.")
            rest.add_narration("Mañana tendrá que ser diferente.")
        
        self.dialog_sequences["rest"] = rest
    
    def get_current_sequence(self):
        """Obtiene la secuencia actual"""
        seq = self.dialog_sequences.get(self.current_scene)
        return seq
    
    def get_current_dialog(self):
        """Obtiene el diálogo actual"""
        seq = self.get_current_sequence()
        if seq:
            return seq.get_current_dialog()
        return None
    
    def get_scene_characters(self):
        """Obtiene todos los personajes únicos presentes en la escena actual"""
        seq = self.get_current_sequence()
        if not seq:
            return []
        
        characters = []
        for dialog in seq.dialogs:
            if dialog.character and dialog.character not in characters:
                characters.append(dialog.character)
        
        return characters
    
    def advance_dialog(self):
        """Avanza al siguiente diálogo"""
        seq = self.get_current_sequence()
        if seq:
            if not seq.next_dialog():
                # Si la secuencia terminó, pasar a la siguiente escena
                self.next_scene()
    
    def next_scene(self):
        """Pasa a la siguiente escena del día"""
        scene_order = ["intro", "work", "transport", "phone", "home"]
        try:
            current_idx = scene_order.index(self.current_scene)
            if current_idx < len(scene_order) - 1:
                self.current_scene = scene_order[current_idx + 1]
                self.dialog_index = 0
        except ValueError:
            pass
    
    def handle_choice(self, choice_action):
        """Maneja una decisión del jugador"""
        if choice_action == "play_gacha":
            self.current_scene = "gacha"
            return True
        elif choice_action == "rest":
            self.current_scene = "rest"
            return True
        elif choice_action == "visit_mom":
            self.current_scene = "mom_visit"
            return True
        return False
    
    def reset(self):
        """Reinicia el gestor de escenas"""
        self.current_scene = "start"
        self.dialog_index = 0
        self.choice_selected = 0


class EndingSequence:
    """Gestor de secuencias de final"""
    
    def __init__(self):
        self.sequences = {}
        self.setup_endings()
    
    def setup_endings(self):
        """Configura los finales del juego"""
        
        # Final Malo - Gacha addiction extrema
        bad = DialogSequence("bad_ending")
        bad.add_narration("========= FINAL: LA TRAGEDIA ==========")
        bad.add_narration("")
        bad.add_narration("Fernando pasó los 7 días perdido en el gacha.")
        bad.add_narration(f"Gastó demasiado dinero que no tenía...")
        bad.add_narration("")
        bad.add_narration("Un día recibe una llamada del hospital:")
        bad.add_dialog(Dialog("Doctor", "¿Eres Fernando? Lamento comunicarte que tu madre falleció hace una hora.", DialogType.NORMAL))
        bad.add_narration("")
        bad.add_narration("Su operación no se pudo pagar.")
        bad.add_narration("Murió sola en esa cama de hospital.")
        bad.add_narration("")
        bad.add_narration("Fernando mira su colección de personajes gacha.")
        bad.add_narration("Ninguno de ellos puede traerla de vuelta.")
        bad.add_narration("")
        bad.add_narration("La culpa es abrumadora.")
        self.sequences["bad"] = bad
        
        # Final Semi-bueno - Moderación
        semi_good = DialogSequence("semi_good_ending")
        semi_good.add_narration("========= FINAL: TIEMPO PERDIDO ==========")
        semi_good.add_narration("")
        semi_good.add_narration("Fernando logró frenar su adicción al gacha.")
        semi_good.add_narration("Jugó solo algunas veces, pero pasó tiempo con su madre.")
        semi_good.add_narration("")
        semi_good.add_narration("Cuando su madre falleció, al menos estaba a su lado.")
        semi_good.add_narration("Pudieron hablar, reír, llorar juntos.")
        semi_good.add_narration("")
        semi_good.add_narration("No la salvó, pero no estuvieron solos.")
        semi_good.add_narration("")
        semi_good.add_narration("Fernando aprende que ningún juego vale más que los momentos reales.")
        semi_good.add_narration("Y que la ludopatía puede destruir lo que más amas.")
        self.sequences["semi_good"] = semi_good
    
    def get_ending(self, ending_type):
        """Obtiene una secuencia de final"""
        return self.sequences.get(ending_type)
