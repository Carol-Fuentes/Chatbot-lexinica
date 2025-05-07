from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionConsultarLey(Action):
    def name(self):
        return "action_consultar_ley"

    def run(self, dispatcher, tracker, domain):
        # Aquí puedes agregar la lógica para leer el archivo y obtener la ley correspondiente
        ley = obtener_ley(tracker.get_slot('tema'))  # Función ficticia para obtener ley
        dispatcher.utter_message(text=f"La ley sobre {tracker.get_slot('tema')} establece que {ley}")
        return []

class ActionConsultarArticulo(Action):
    def name(self):
        return "action_consultar_articulo"

    def run(self, dispatcher, tracker, domain):
        # Lógica para buscar el artículo y devolverlo
        articulo = obtener_articulo(tracker.get_slot('numero_articulo'))  # Función ficticia
        dispatcher.utter_message(text=f"El artículo {tracker.get_slot('numero_articulo')} establece: {articulo}")
        return []