from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import os


class RemoveMaterialWarningChoicePopup(Popup):
    """Popup Remover Material"""
    def __init__(self, material_file, material, callback=None,**kwargs):
        super().__init__(**kwargs)
        self.title = "Tem Certeza?"
        self.size_hint = (None, None)
        self.size = (600, 600)
        self.callback = callback

        layout = BoxLayout(orientation='vertical')

        text_label = Label(text=f"Todos os Dados do Material:\n\n{material}\n\nSerão Apagados PERMANENTEMENTE\nCaso Tenha Certeza Dessa Ação\nClique em No Botão Verde",
                         font_size=20, 
                         halign='left', 
                         color=[1,1,1,1]) #cor da fonte 
        
        buttons_layout = BoxLayout(orientation='horizontal',
                                   size_hint=(1, 0.2),
                                   spacing=350)
        
        cancel_button = Button(size_hint=(0.5, None),
                               height=50,
                               background_normal="images/botões/cancelar.png")
        cancel_button.bind(on_release=self.recuse_choice)

        confirm_button = Button(size_hint=(0.5, None),
                                height=50,
                                background_normal="images/botões/check_fundo_transparente.png")
        confirm_button.bind(on_release=lambda btn: self.confirm_choice(material_file=material_file))
        
        buttons_layout.add_widget(cancel_button)
        buttons_layout.add_widget(confirm_button)
        
        layout.add_widget(text_label)
        layout.add_widget(buttons_layout)
        self.content = layout

    def confirm_choice(self, material_file, *kwargs):
        os.remove(material_file)
        self.dismiss()
        if self.callback is not None:
            self.callback()
    
    def recuse_choice(self, *kwargs):
        self.dismiss()