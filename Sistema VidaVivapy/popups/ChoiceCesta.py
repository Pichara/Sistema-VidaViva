from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import os


class ChoiceCestaPopup(Popup):
    """Popup Escolher Itens Cesta Basica"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Itens da Cesta Basica"
        self.size_hint = (None, None)
        self.size = (700, 700) 
        
        layout_scrollview = BoxLayout(orientation='vertical', spacing=2, size_hint_y=None)
        layout_scrollview.bind(minimum_height=layout_scrollview.setter('height'))
        
        #pegando todos os suplementos
        file_estoque = os.listdir("data/estoque")
        lista_suplementos = []
        for suple in file_estoque:
            lista_suplementos.append(suple.replace(".txt", "").replace("-", "|"))
        
        #Criando botão para cada suplemento
        for suplemento in lista_suplementos:
            suplemento = suplemento.replace(".txt", "")
            button = Button(text=f"{suplemento}",
                            size_hint_y=None,
                            size_hint_x= 1,
                            font_size = 15,
                            color = (1,1,1,1),
                            height=20,
                            background_normal = "images/icones/fundo_azul_escuro_normal.png",
                            halign='left',
                            text_size= (300, None))
        
            button.bind(on_press=self.add_suplemento)
            layout_scrollview.add_widget(button)
          
        scrollview = ScrollView(pos_hint={"x": 0, "y": 0.5}, size_hint=(1, 0.5))
        scrollview.add_widget(layout_scrollview)
        self.selected_suplementos = []
        #Criando o Boy layout Inteiro e ja Adicionando o ScrollView
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(scrollview)

        #Criando Label Para Mostrar Os Já Definidos
        try:#Try caso Não haja Suplementos Setados
            with open("data/data/cesta_basica_set.txt", "r") as file:
                data = file.readlines()
                for i in range(len(data)):
                    data[i] = data[i].replace("\n", "")
            
            setados = "Padrão de Cesta Basica:\n\n"
            setados += ", ".join(data)
            label_setados = Label(text= setados,
                        text_size= (650, None),
                        halign='left',
                        color = (1,1,1,1))
            layout.add_widget(label_setados)
        except:
            None

        #Criando Label de Texto dos New Selecionados
        message = "Suplementos selecionados:\n\n"
        message += "\n".join(self.selected_suplementos)
        self.label = Label(text= message,
                      text_size= (650, None),
                      halign='left',
                      color = (1,1,1,1))

        #Criando Botão to save
        ok_button = Button(size_hint = (0.15, 0.15), 
                           pos_hint = {"x": 0.8, "y": 0},
                           background_normal = "images/botões/check_fundo_transparente.png")
        ok_button.bind(on_release=self.save_set)

        #Adicionando a Label Final e Setando no Pupup
        layout.add_widget(self.label)
        layout.add_widget(ok_button)
        self.content = layout
        
    def add_suplemento(self, button):
        if len(self.selected_suplementos) < 20:
            self.selected_suplementos.append(button.text)
        message = "Suplementos selecionados:\n\n"
        message += "\n".join(self.selected_suplementos)
        self.label.text = message

    def save_set(self, *args):
        if len(self.selected_suplementos) > 0:
            with open("data/data/cesta_basica_set.txt", "w") as file:
                for suplementos_of_cesta in self.selected_suplementos:
                    file.write(suplementos_of_cesta + "\n")
            self.dismiss()
        else:
            None