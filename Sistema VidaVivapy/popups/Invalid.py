from kivy.uix.popup import Popup
from kivy.uix.label import Label

class InvalidPopup(Popup):
    """Popup Para ser Aberto Quando Houver um Campo Invalido"""
    def __init__(self, invalidos, **kwargs):
        super().__init__(**kwargs)
        self.title = "Campos Inválidos"
        self.size_hint = (None, None)
        self.size = (400, 400)

        content = Label(text=", \n".join(invalidos), font_size=20, halign='left', color=[1,1,1,1]) #cor da fonte 
        self.content = content