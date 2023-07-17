from kivy.uix.label import Label
from kivy.uix.popup import Popup


class EstoqueMissingPopup(Popup):
    """Popup Alerta de Estoque Faltando"""
    def __init__(self, invalidos, **kwargs):
        super().__init__(**kwargs)
        self.title = "Suplementação Indisponível"
        self.size_hint = (None, None)
        self.size = (400, 400)

        content = Label(text=", \n".join(invalidos), font_size=20, halign='left', color=[1,1,1,1]) #cor da fonte 
        self.content = content