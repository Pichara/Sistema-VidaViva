import os
import shutil
from collections import Counter
from unidecode import unidecode
import re
from datetime import datetime
import pyautogui
import keyboard
from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Ellipse

#CONFIGURAÇÕES DO KIVY:
Config.set('kivy', 'window_icon', 'images/icones/VidaVivaIcon.png')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'width', '1300')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'borderless', False)

#POS-IMPORTS (Evitar Bug de Resolução + Visualização):
from kivy.core.window import Window

from popups.Invalid import InvalidPopup

from popups.EstoqueMissing import EstoqueMissingPopup

from popups.RemovePacienteWarningChoice import RemovePacienteWarningChoicePopup

from popups.RemoveFPacienteWarningChoice import RemoveFPacienteWarningChoicePopup

from popups.RemoveMaterialWarningChoice import RemoveMaterialWarningChoicePopup

#Classe Puxada pelo Arquivo .kv
from popups.ChoiceCesta import ChoiceCestaPopup 

class CadastrosWindow(Screen):
    def __init__(self, **kwargs):
        super(CadastrosWindow, self).__init__(**kwargs)

        # Criar ScrollView
        self.scroll_view = ScrollView(pos_hint={"x": 0.2586605080831409, "y": 0}, size_hint=(0.743, 0.7998))

        # Criar BoxLayout para adicionar os botões dentro do ScrollView
        box_layout = BoxLayout(orientation='vertical', spacing=2, size_hint_y=None)
        box_layout.bind(minimum_height=box_layout.setter('height'))

        # Adicionar botões ao BoxLayout
        file_pacientes = 'data/pacientes/'
        for paciente in os.listdir(file_pacientes):
            #pegando o nome do paciente
            with open(f"data/pacientes/{paciente}", "r") as file:
                info_paciente = file.readlines()
                paciente_nome = info_paciente[0]
                paciente_nome = paciente_nome.replace("\n", "")

            button = Button(text=f"{paciente_nome}",
                            color = (1,1,1,1),
                            size_hint_y=None,
                            size_hint_x= 1,
                            font_size = 25,
                            height=40,
                            background_normal = "images/icones/Fundo_gradiente.png",
                            halign='left',
                            text_size= (900, None))
          
            #gambiarra para tirar todas as infos a partir do nome
            button.bind(on_release=self.abrir_janela_paciente)
            box_layout.add_widget(button)

        falecidos = os.listdir('data/falecidos/')
        if len(falecidos) > 0:
            image_falecidos = Image(source = "images/icones/paciente_falecido.png",
                                    size_hint_y = None,
                                    size_hint_x =0.22,
                                    height = 50,
                                    pos_hint = {"x": 0, "y": 0},
                                    allow_stretch = False,
                                    keep_ratio = False)
            box_layout.add_widget(image_falecidos)
        
        for falecido in falecidos:
            #pegando o nome do falecido
            with open(f"data/falecidos/{falecido}", "r") as file:
                info_falecido = file.readlines()
                falecido_nome = info_falecido[0]
                falecido_nome = falecido_nome.replace("\n", "")
        
            button_falecidos = Button(text=f"{falecido_nome}",
                                color = (1,1,1,0.4),
                                size_hint_y=None,
                                size_hint_x= 1,
                                font_size = 25,
                                height=40,
                                background_normal = "images/icones/Fundo_gradiente.png",
                                halign='left',
                                text_size= (900, None))
            
            button_falecidos.bind(on_release=self.abrir_janela_paciente_falecido)
            box_layout.add_widget(button_falecidos)
        # Adicionar BoxLayout ao ScrollView
        self.scroll_view.add_widget(box_layout)

        # Adicionar ScrollView à tela
        self.add_widget(self.scroll_view)

    def update_pacientes(self):
        """Fazer a Verificação no Banco de Dados de Quais Pacientes estão no Sistema e Apresenta-los no ScrollView"""

        #Apagar o ScrollView
        self.scroll_view.clear_widgets()
        # Criar ScrollView
        self.scroll_view = ScrollView(pos_hint={"x": 0.2586605080831409, "y": 0}, size_hint=(0.743, 0.7998))

        # Criar BoxLayout para adicionar os botões dentro do ScrollView
        box_layout = BoxLayout(orientation='vertical', spacing=2, size_hint_y=None)
        box_layout.bind(minimum_height=box_layout.setter('height'))

        # Adicionar botões ao BoxLayout
        file_pacientes = 'data/pacientes/'
        for paciente in os.listdir(file_pacientes):
            #pegando o nome do paciente
            with open(f"data/pacientes/{paciente}", "r") as file:
                info_paciente = file.readlines()
                paciente_nome = info_paciente[0]
                paciente_nome = paciente_nome.replace("\n", "")

            button = Button(text=f"{paciente_nome}",
                            color = (1,1,1,1),
                            size_hint_y=None,
                            size_hint_x= 1,
                            font_size = 25,
                            height=40,
                            background_normal = "images/icones/Fundo_gradiente.png",
                            halign='left',
                            text_size= (900, None))
          
            #gambiarra para tirar todas as infos a partir do nome
            button.bind(on_release=self.abrir_janela_paciente)
            box_layout.add_widget(button)

        falecidos = os.listdir('data/falecidos/')
        if len(falecidos) > 0:
            image_falecidos = Image(source = "images/icones/paciente_falecido.png",
                                    size_hint_y = None,
                                    size_hint_x =0.22,
                                    height = 50,
                                    pos_hint = {"x": 0, "y": 0},
                                    allow_stretch = False,
                                    keep_ratio = False)
            box_layout.add_widget(image_falecidos)
        
        for falecido in falecidos:
            #pegando o nome do falecido
            with open(f"data/falecidos/{falecido}", "r") as file:
                info_falecido = file.readlines()
                falecido_nome = info_falecido[0]
                falecido_nome = falecido_nome.replace("\n", "")
        
            button_falecidos = Button(text=f"{falecido_nome}",
                                color = (1,1,1,0.4),
                                size_hint_y=None,
                                size_hint_x= 1,
                                font_size = 25,
                                height=40,
                                background_normal = "images/icones/Fundo_gradiente.png",
                                halign='left',
                                text_size= (900, None))
            
            button_falecidos.bind(on_release=self.abrir_janela_paciente_falecido)
            box_layout.add_widget(button_falecidos)
        # Adicionar BoxLayout ao ScrollView
        self.scroll_view.add_widget(box_layout)

        # Adicionar ScrollView à tela
        self.add_widget(self.scroll_view)

    def to_cadastrar_novo(self):
        self.manager.switch_to(CadastrarWindow(name="cadastrar"))

    def to_suple(self):
        self.manager.switch_to(SuplementaçãoWindow(name="suplementação"))
    
    def to_materiais(self):
        self.manager.switch_to(MateriaisWindow(name="materiais"))
    
    def to_info(self):
        self.manager.switch_to(InfoWindow(name="info"))

    def filter_pacientes(self):
        """Fazer a Função de Filtrar os Pacientes que Serão Apresentados no ScrollView
        OBS: Deve ser usado como "on_text" """

        #Pegar todos os tipos de Filter e Amplilos
        filter = self.ids.pacientes_filter.text
        if filter == "":
            self.update_pacientes()
            return
        filter1 = filter.upper()
        filter2 = filter.lower()

        #remover o widget para colocar de novo
        self.remove_widget(self.scroll_view)
        
        # Criar ScrollView
        self.scroll_view = ScrollView(pos_hint={"x": 0.2586605080831409, "y": 0}, size_hint=(0.743, 0.7998))

        # Criar BoxLayout para adicionar os botões dentro do ScrollView
        box_layout = BoxLayout(orientation='vertical', spacing=2, size_hint_y=None)
        box_layout.bind(minimum_height=box_layout.setter('height'))

        # Adicionar botões ao BoxLayout
        file_pacientes = 'data/pacientes'
        for paciente in os.listdir(file_pacientes):
            #Aplicar o Filtro
            if filter in paciente or filter1 in paciente or filter2 in paciente:
                #pegando o nome do paciente
                with open(f"data/pacientes/{paciente}", "r") as file:
                    info_paciente = file.readlines()
                    paciente_nome = info_paciente[0]
                    paciente_nome = paciente_nome.replace("\n", "")

                button = Button(text=f"{paciente_nome}",
                                color = (1,1,1,1),
                                size_hint_y=None,
                                size_hint_x= 1,
                                font_size = 25,
                                height=40,
                                background_normal = "images/icones/Fundo_gradiente.png",
                                halign='left',
                                text_size= (900, None))
                
                #gambiarra para tirar todas as infos a partir do nome
                button.bind(on_release=self.abrir_janela_paciente)
                box_layout.add_widget(button)

        # Adicionar BoxLayout ao ScrollView
        self.scroll_view.add_widget(box_layout)

        # Adicionar ScrollView à tela
        self.add_widget(self.scroll_view)

    def abrir_janela_paciente(self, button):
        """Uma Gambiarra Feita para Abrir a Screen(PacienteWindow) com os Dados Referentes
        Usando Apenas o Nome do Paciente"""
        
        #Abrindo o arquivo e retirando a data como list
        name = button.text
        file_name = name.replace(" ", "_")
        try: 
            with open(f"data/pacientes/{file_name}.txt", "r") as file:
                data = file.readlines()
        except:
            self.__init__()
            return
        
        #importando a data do file
        nome = data[0]
        conjugue = data[1]
        cpf = data[2]
        sus = data[3]
        dependentes = data[4]
        data_de_nascimento = data[5]
        telefone = data[6]
        telefone_fixo = data[7]
        ca = data[8]
        endereço = f"{data[10]}, {data[9]}, {data[12]} | {data[11]}"
        data_de_cadastro = data[13]
        n_tratamento = data[14].count("|")
        list_tratamento = []
        if "acompanhamento" in data[14]:
            list_tratamento.append("Acompanhamento")
        if "cirurgia" in data[14]:
            list_tratamento.append("Cirurgia")
        if "quimioterapia" in data[14]:
            list_tratamento.append("Quimioterapia")
        if "radioterapia" in data[14]:
            list_tratamento.append("Radioterapia")
        tratamento = ""
        n0_tratamento = 0
        for i in list_tratamento:
            n0_tratamento += 1
            tratamento += i
            if n0_tratamento != n_tratamento:
                tratamento += ", "
        
        #retirando os \n
        nome = nome.replace("\n", "")
        conjugue = conjugue.replace("\n", "")
        cpf = cpf.replace("\n", "")
        sus = sus.replace("\n", "")
        tratamento = tratamento.replace("\n", "")
        telefone = telefone.replace("\n", "")
        telefone_fixo = telefone_fixo.replace("\n", "")
        dependentes = dependentes.replace("\n", "")
        data_de_nascimento = data_de_nascimento.replace("\n", "")
        ca = ca.replace("\n", "")
        endereço = endereço.replace("\n", "")
        data_de_cadastro = data_de_cadastro.replace("\n", "")
        
        #acessando a screem paciente da screem cadastro
        paciente_screen = sm.get_screen('paciente')
        
        #inputando as informações retiradas no arquivo nas labels
        paciente_screen.ids.label_nome.text = nome
        paciente_screen.ids.label_conjugue.text = conjugue
        paciente_screen.ids.label_cpf.text = cpf
        paciente_screen.ids.label_data_de_nascimento.text = data_de_nascimento
        paciente_screen.ids.label_dependentes.text = dependentes
        paciente_screen.ids.label_telefone.text = telefone
        paciente_screen.ids.label_telefone_fixo.text = telefone_fixo
        paciente_screen.ids.label_endereço.text = endereço
        paciente_screen.ids.label_sus.text = sus
        paciente_screen.ids.label_ca.text = ca
        paciente_screen.ids.label_data_de_cadastro.text = data_de_cadastro
        paciente_screen.ids.label_tratamento.text = tratamento
        self.manager.current = "paciente"

    def abrir_janela_paciente_falecido(self, button):
        """Uma Gambiarra Feita para Abrir a Screen(PacienteFalecidoWindow) com os Dados Referentes
        Usando Apenas o Nome do Paciente"""

        name = button.text
        file_name = name.replace(" ", "_")
        
        #abrindo o arquivo e retirando a data como list
        try: 
            with open(f"data/falecidos/{file_name}.txt", "r") as file:
                data = file.readlines()
        except:
            self.__init__()
            return

        #importando a data do file
        nome = data[0]
        conjugue = data[1]
        cpf = data[2]
        sus = data[3]
        dependentes = data[4]
        data_de_nascimento = data[5]
        telefone = data[6]
        telefone_fixo = data[7]
        ca = data[8]
        endereço = f"{data[10]}, {data[9]}, {data[12]} | {data[11]}"
        data_de_cadastro = data[13]
        n_tratamento = data[14].count("|")
        list_tratamento = []
        if "acompanhamento" in data[14]:
            list_tratamento.append("Acompanhamento")
        if "cirurgia" in data[14]:
            list_tratamento.append("Cirurgia")
        if "quimioterapia" in data[14]:
            list_tratamento.append("Quimioterapia")
        if "radioterapia" in data[14]:
            list_tratamento.append("Radioterapia")
        tratamento = ""
        n0_tratamento = 0
        for i in list_tratamento:
            n0_tratamento += 1
            tratamento += i
            if n0_tratamento != n_tratamento:
                tratamento += ", "
        
        #retirando os \n
        nome = nome.replace("\n", "")
        conjugue = conjugue.replace("\n", "")
        cpf = cpf.replace("\n", "")
        sus = sus.replace("\n", "")
        tratamento = tratamento.replace("\n", "")
        telefone = telefone.replace("\n", "")
        telefone_fixo = telefone_fixo.replace("\n", "")
        dependentes = dependentes.replace("\n", "")
        data_de_nascimento = data_de_nascimento.replace("\n", "")
        ca = ca.replace("\n", "")
        endereço = endereço.replace("\n", "")
        data_de_cadastro = data_de_cadastro.replace("\n", "")
        
        #acessando a screem paciente da screem cadastro
        paciente_screen = self.manager.get_screen('pacientefalecido')
        
        #inputando as informações retiradas no arquivo nas labels
        paciente_screen.ids.label_fnome.text = nome
        paciente_screen.ids.label_fconjugue.text = conjugue
        paciente_screen.ids.label_fcpf.text = cpf
        paciente_screen.ids.label_fdata_de_nascimento.text = data_de_nascimento
        paciente_screen.ids.label_fdependentes.text = dependentes
        paciente_screen.ids.label_ftelefone.text = telefone
        paciente_screen.ids.label_ftelefone_fixo.text = telefone_fixo
        paciente_screen.ids.label_fendereço.text = endereço
        paciente_screen.ids.label_fsus.text = sus
        paciente_screen.ids.label_fca.text = ca
        paciente_screen.ids.label_fdata_de_cadastro.text = data_de_cadastro
        paciente_screen.ids.label_ftratamento.text = tratamento
        self.manager.current = "pacientefalecido"

class SuplementaçãoWindow(Screen):
    def __init__(self, **kwargs):
        super(SuplementaçãoWindow, self).__init__(**kwargs)

        # Criar ScrollView
        scroll_view = ScrollView(pos_hint={"x": 0.2586605080831409, "y": 0}, size_hint=(0.743, 0.73))

        # Criar BoxLayout para adicionar os botões dentro do ScrollView
        box_layout = BoxLayout(orientation='vertical', spacing=2, size_hint_y=None)
        box_layout.bind(minimum_height=box_layout.setter('height'))
        
        # Adicionar botões ao BoxLayout
        file_estoque = 'data/estoque'
        
        for suplementação in os.listdir(file_estoque):
            suple_file = f"data/estoque/{suplementação}"
            with open(f"{suple_file}", "r") as file:
                info_estoque = file.readlines()
                suplementação_nome = info_estoque[0]
                suplementação_quantidade = info_estoque[1]
                suplementação_icon = info_estoque[2].replace("\n", "")

            item_layout = RelativeLayout(size_hint_y=None, height=50)
            
            suple_text_label = Label(text=f"{suplementação_nome}", #Nome da suplementação
                                        color = (1,1,1,1),
                                        size_hint_y= 0.45,
                                        size_hint_x= 1.12,
                                        font_size = 25,
                                        halign='left',
                                        text_size= (940, None))
            
            suple_entire_image = Image(source = "images/icones/fundo_azul_escuro_add_remove.png", #Imagem de fundo
                                       size_hint_x = 1,
                                       size_hint_y = None,
                                       height = 50, 
                                       allow_stretch = True,
                                       keep_ratio = False)
            
            suple_icon_image = Image(source = suplementação_icon, #Icone da suplementação
                                     size_hint_y= 0.9,
                                     size_hint_x= 0.05,
                                     allow_stretch = True,
                                     keep_ratio = True,
                                     pos_hint = {"x": 0.01, "y": 0.05})
            
            suple_number_label = Label(text=f"{suplementação_quantidade}", #Quantidade suplementação
                                        color = (1,1,1,1),
                                        size_hint_y= 0.45,
                                        size_hint_x= 2.58,
                                        font_size = 25,
                                        halign='left',
                                        text_size= (940, None))
            
            suple_add_button = Button(text = f"{suple_file}",
                                      color = (0,0,0,0), #Botão adicionar suple
                                      background_color = (0,0,0,0),
                                      size_hint_y= 0.7,
                                      size_hint_x= 0.04,
                                      pos_hint = {"x": 0.7487, "y": 0.15})

            suple_add_button.bind(on_release=self.adicionar_quantidade)

            suple_remove_button = Button(text = f"{suple_file}",
                                        color = (0,0,0,0), #Botão remover suple
                                        background_color = (0,0,0,0),
                                        size_hint_y= 0.7,
                                        size_hint_x= 0.04,
                                        pos_hint = {"x": 0.8487, "y": 0.15})

            suple_remove_button.bind(on_release=self.remover_quantidade)

            suple_delete_button = Button(text = f"{suple_file}",
                                        color = (0,0,0,0), #Botão Delete Suple
                                        background_color = (0,0,0,0),
                                        size_hint_y= 0.6,
                                        size_hint_x= 0.03,
                                        pos_hint = {"x": 0.965, "y": 0.2})
            
            suple_delete_button.bind(on_release=self.delete_suple)

            item_layout.add_widget(suple_entire_image)
            item_layout.add_widget(suple_text_label)
            item_layout.add_widget(suple_icon_image)
            item_layout.add_widget(suple_add_button)
            item_layout.add_widget(suple_remove_button)
            item_layout.add_widget(suple_number_label)
            item_layout.add_widget(suple_delete_button)

            #suple_icon_image = Image icon da suplementação que vai ficar atras do texto
            #suple_entire_image = Image imagem de fundo padrão para cada material
            #suple_number_label = Numero quantidade 
            #suple_text_label = Label Texto que vai ficar em cima da imagem
            #suple_add_button = Button Botão bindado adicionar uma quantidade de suplementação
            #suple_remove_button = Button Botão bindado para remover uma quantidade de suplementação
            #suple_delete_button = Button de deletar o suplemento

            box_layout.add_widget(item_layout)

        # Adicionar BoxLayout ao ScrollView
        scroll_view.add_widget(box_layout)

        # Adicionar ScrollView à tela
        self.add_widget(scroll_view)

    def to_cadastro(self):
        self.manager.switch_to(CadastrosWindow(name="cadastro"))
    def to_materiais(self):
        self.manager.switch_to(MateriaisWindow(name="materiais"))
    def to_info(self):
        self.manager.switch_to(InfoWindow(name="info"))
    def to_enviar_suplementação(self):
        self.manager.switch_to(EnviarSuplementaçãoWindow(name="enviarsuplementação"))
    def to_adicionar_estoque(self):
        self.manager.switch_to(AdicionarEstoqueWindow(name="adicionarestoque"))

    def adicionar_quantidade(self, button):
        """Adiciona o Valor de 1 Unidade no Banco de Dados da Suplementação e da um Refresh no ScrollView"""

        suple_file = button.text
        with open(suple_file, "r+") as file:
            info_estoque = file.readlines()
            quantidade = int(info_estoque[1].strip()) + 1
            info_estoque[1] = str(quantidade) + "\n"
            file.seek(0)
            file.writelines(info_estoque)
            file.truncate()
        self.manager.switch_to(SuplementaçãoWindow())

    def remover_quantidade(self, button):
        """Retira o Valor de 1 Unidade no Banco de Dados da Suplementação e da um Refresh no ScrollView"""

        suple_file = button.text
        with open(suple_file, "r+") as file:
            info_estoque = file.readlines()
            quantidade = int(info_estoque[1].strip()) - 1
            if quantidade < 0:
                quantidade = 0
            info_estoque[1] = str(quantidade) + "\n"
            file.seek(0)
            file.writelines(info_estoque)
            file.truncate()
        self.manager.switch_to(SuplementaçãoWindow())

    def delete_suple(self, button):
        """Deleta o Suplemento do Banco de Dados"""
        try:
            os.remove(button.text)
            self.manager.switch_to(SuplementaçãoWindow())
        except:
            None

class MateriaisWindow(Screen):
    def __init__(self, **kwargs):
        super(MateriaisWindow, self).__init__(**kwargs)

        # Criar ScrollView
        scroll_view = ScrollView(pos_hint={"x": 0.21622024634334104, "y": 0},
                                    size_hint=(0.7845, 0.809))

        # Criar BoxLayout para adicionar os botões dentro do ScrollView
        box_layout = BoxLayout(orientation='vertical', spacing=2, size_hint_y=None)
        box_layout.bind(minimum_height=box_layout.setter('height'))

        # Adicionar botões ao BoxLayout
        file_materiais = 'data/materiais'
        for material in os.listdir(file_materiais):
            #pegando o nome do paciente
            with open(f"data/materiais/{material}", "r") as file:
                info_materiais = file.readlines()
                material_type = info_materiais[0].replace("\n", "")
                material_donator = info_materiais[1].replace("\n", "")
                material_preservation = info_materiais[2]
                if "perfeito.png" in material_preservation:
                    material_preservation = "Perfeito"
                if "ok.png" in material_preservation:
                    material_preservation = "Ok"
                if "péssimo.png" in material_preservation:
                    material_preservation = "Péssimo"
                material_reception = info_materiais[3].replace("\n", "")
                material_reception_to_file = material_reception.replace("/", "_")
                emprestado = info_materiais[4].replace("\n", "").replace(" ", "_")
                #Sistema Para Verificar Se o Material Possui Dono e Se Não Tiver Retira-lo
                if emprestado + ".txt" in os.listdir("data/pacientes/"):
                    opacity = 1
                else:
                    opacity = 0
                    info_materiais[4] = "\n"
                    with open(f"data/materiais/{material}", "w") as file:
                        for line in info_materiais:
                            file.write(line)

            material_layout = RelativeLayout(size_hint_y=None, height=50)
            
            material_text_label = Label(text=f"{material_type}",
                                        color = (1,1,1,1),
                                        size_hint_y= 0.8,
                                        size_hint_x= 0.95,
                                        font_size = 25,
                                        halign='left',
                                        text_size= (940, None))

            material_entire_button = Button(text = f"data/materiais/{material_type}_{material_preservation}_{material_donator}_{material_reception_to_file}.txt",
                                      color = (0,0,0,0),
                                      background_normal = "images/icones/Fundo_gradiente.png",
                                      size_hint_y= 1,
                                      size_hint_x= 1,
                                      pos_hint = {"x": 0, "y": 0})
            material_entire_button.bind(on_release=self.open_material_descrição)
            
            material_ocupado_image = Image(source = "images\icones\ocupado_icone.png",
                                           size_hint_x = 1.5,
                                            size_hint_y = 0.8,
                                            opacity=1 if opacity == 1 else 0,
                                            allow_stretch = False,
                                            keep_ratio = False)
            

            material_layout.add_widget(material_entire_button)
            material_layout.add_widget(material_ocupado_image)
            material_layout.add_widget(material_text_label)

            box_layout.add_widget(material_layout)

        # Adicionar BoxLayout ao ScrollView
        scroll_view.add_widget(box_layout)

        # Adicionar ScrollView à tela
        self.add_widget(scroll_view)

    def to_cadastro(self):
        self.manager.switch_to(CadastrosWindow(name="cadastro"))

    def to_suple(self):
        self.manager.switch_to(SuplementaçãoWindow(name="suplementação"))
    
    def to_info(self):
        self.manager.switch_to(InfoWindow(name="info"))

    def to_adicionar_material(self):
        self.manager.switch_to(AdicionarMaterialWindow(name="adicionarmaterial"))

    def open_material_descrição(self, button):
        """Faz uma Gambiarra para Abrir a screen(MaterialWindow).
         Pegando o text do Botão do Material e Importando os Dados Referente ao Material Especifico"""
        
        file_name = button.text

        #abrindo o arquivo e retirando a data como list
        try:
            with open(f"{file_name}", "r") as file:
                data = file.readlines()
                material_type = data[0].replace("\n", "")
                material_donator = data[1].replace("\n", "")
                material_preservation = data[2]
                if "perfeito.png" in material_preservation:
                    material_preservation = "perfeito"
                if "ok.png" in material_preservation:
                    material_preservation = "ok"
                if "péssimo.png" in material_preservation:
                    material_preservation = "péssimo"
                material_reception = data[3].replace("\n", "")
                material_owner = data[4].replace("\n", "")
            
            material_descrição_screen = self.manager.get_screen('descriçãomateriais')
            
            #inputando as informações retiradas no arquivo nas labels
            material_descrição_screen.ids.label_material_nome.text = material_type
            material_descrição_screen.ids.label_material_doador.text = material_donator
            material_descrição_screen.ids.label_material_conservação.text = material_preservation
            material_descrição_screen.ids.label_material_recepção.text = material_reception
            material_descrição_screen.ids.label_material_emprestado.text = material_owner
            self.manager.current = "descriçãomateriais"
        except:
            self.__init__()
            return

class InfoWindow(Screen):
    def __init__(self, *args, **kwargs):
        super(InfoWindow, self).__init__(*args, **kwargs)
        #GRAFICO LOCALIZAÇÔES
        localizações = []
        for paciente in os.listdir("data/pacientes"):
            with open(f"data/pacientes/{paciente}", "r") as file:
                data = file.readlines()
                localização = data[11].replace("\n", "")
                localizações.append(localização)
        if localizações != []:
            Cg = localizações.count("Campos Gerais")/len(localizações)*360
            Cm = localizações.count("Campo do Meio")/len(localizações)*360
            Zr = localizações.count("Zona Rural")/len(localizações)*360

        with self.canvas:
            Color(1, 0.5, 0)
            Ellipse(pos=(self.center_x + Window.width * 0.25, self.center_y + Window.height * 0.4), size=(250, 250), angle_start=0, angle_end=Cg)

            Color(0.5, 1, 0)
            Ellipse(pos=(self.center_x + Window.width * 0.25, self.center_y + Window.height * 0.4), size=(250, 250), angle_start=Cg, angle_end=Cg + Cm)

            Color(0, 0.5, 1)
            Ellipse(pos=(self.center_x + Window.width * 0.25, self.center_y + Window.height * 0.4), size=(250, 250), angle_start=Cg + Cm, angle_end=Cg + Cm + Zr)

            self.add_widget(Label(text=f'Campos Gerais - {int(Cg/3.6):.1f}%', color=(1, 0.5, 0, 1), pos_hint={'center_x': 0.57, 'center_y': 0.7}, font_size=30, halign = "left"))
            self.add_widget(Label(text=f'Campo do Meio - {int(Cm/3.6):.1f}%', color=(0.5, 1, 0, 1), pos_hint={'center_x': 0.574, 'center_y': 0.65}, font_size=30, halign = "left"))
            self.add_widget(Label(text=f'Zona Rural - {int(Zr/3.6):.1f}%', color=(0, 0.5, 1, 1), pos_hint={'center_x': 0.55, 'center_y': 0.6}, font_size=30, halign = "left"))

        #DATA MATERIAIS DISPONIVEIS E EMPRESTADOS
        materiais = {
            'Cadeira de Banho': {'disponivel': 0, 'emprestado': 0},
            'Cadeira de Roda': {'disponivel': 0, 'emprestado': 0},
            'Cama': {'disponivel': 0, 'emprestado': 0},
            'Muleta': {'disponivel': 0, 'emprestado': 0},
            'Peruca': {'disponivel': 0, 'emprestado': 0},
            'Andador': {'disponivel': 0, 'emprestado': 0}}

        for material in os.listdir("data/materiais"):
            with open(f"data/materiais/{material}") as file:
                data = file.readlines()
                E = data[4]
                if E != "\n":
                    for k, v in materiais.items():
                        if k in material:
                            v['emprestado'] += 1
                else:
                    for k, v in materiais.items():
                        if k in material:
                            v['disponivel'] += 1
        
        self.add_widget(Label(text=f'{materiais["Cadeira de Roda"]["disponivel"]}   {materiais["Cadeira de Roda"]["emprestado"]}', color=(1, 1, 1, 1), pos_hint = {"x": 0.444,"y": 0.25}, font_size=20))
        self.add_widget(Label(text=f'{materiais["Cadeira de Banho"]["disponivel"]}   {materiais["Cadeira de Banho"]["emprestado"]}', color=(1, 1, 1, 1), pos_hint = {"x": 0.444,"y": 0.185}, font_size=20))
        self.add_widget(Label(text=f'{materiais["Muleta"]["disponivel"]}   {materiais["Muleta"]["emprestado"]}', color=(1, 1, 1, 1), pos_hint = {"x": 0.444,"y": 0.115}, font_size=20))
        self.add_widget(Label(text=f'{materiais["Peruca"]["disponivel"]}   {materiais["Peruca"]["emprestado"]}', color=(1, 1, 1, 1), pos_hint = {"x": 0.444,"y": 0.055}, font_size=20))
        self.add_widget(Label(text=f'{materiais["Cama"]["disponivel"]}   {materiais["Cama"]["emprestado"]}', color=(1, 1, 1, 1), pos_hint = {"x": 0.444,"y": -0.01}, font_size=20))
        self.add_widget(Label(text=f'{materiais["Andador"]["disponivel"]}   {materiais["Andador"]["emprestado"]}', color=(1, 1, 1, 1), pos_hint = {"x": 0.444,"y": -0.0715}, font_size=20))
    

        #DATA PACIENTES ATIVOS
        pacientes_ativos = len(os.listdir("data/pacientes"))
        #DATA PACIENTES PALECIDOS
        paciente_falecidos = len(os.listdir("data/falecidos"))
        #DATA CESTA BASICAS DOADAS
        with open(f"data/data/info.txt", "r") as file:
            data = file.readlines()
            cesta_basicas_doadas = data[0].replace("\n", "")
        #DATA SUPLEMENTAÇÔES UNICAS DOADAS
        with open("data/data/info.txt", "r") as file:
            data = file.readlines()
            suplementação_unicas_doadas = data[1].replace('\n', "")
        
        Scroll_View = ScrollView(pos_hint={"x": 0.2155504234026174, "y": 0}, size_hint= (0.7845, 0.38))

        box_layout = BoxLayout(orientation='vertical', spacing=1, size_hint_y=None)
        box_layout.bind(minimum_height=box_layout.setter('height'))
        
        
        pacientes_ativos_layout = RelativeLayout(size_hint_y=None, height=50) #PACIENTES ATIVOS
        pacientes_ativos_image = Image(source = "images/icones/pacientes_ativos.png", 
                                       size_hint_x = 1,
                                       size_hint_y = None,
                                       height = 50, 
                                       allow_stretch = True,
                                       keep_ratio = False)
        pacientes_ativos_label = Label(text=f"{pacientes_ativos}",
                                        color = (1,1,1,1),
                                        size_hint_y= 1,
                                        size_hint_x= 2.375,
                                        font_size = 25,
                                        halign='left',
                                        text_size= (940, None))
        pacientes_ativos_layout.add_widget(pacientes_ativos_image)
        pacientes_ativos_layout.add_widget(pacientes_ativos_label)

        pacientes_falecidos_layout = RelativeLayout(size_hint_y=None, height=50) #PACIENTES FALECIDOS
        pacientes_falecidos_image = Image(source = "images/icones/pacientes_falecidos.png", 
                                       size_hint_x = 1,
                                       size_hint_y = None,
                                       height = 50, 
                                       allow_stretch = True,
                                       keep_ratio = False)
        pacientes_falecidos_label = Label(text=f"{paciente_falecidos}",
                                        color = (1,1,1,1),
                                        size_hint_y= 1,
                                        size_hint_x= 2.375,
                                        font_size = 25,
                                        halign='left',
                                        text_size= (940, None))
        pacientes_falecidos_layout.add_widget(pacientes_falecidos_image)
        pacientes_falecidos_layout.add_widget(pacientes_falecidos_label)

        cesta_basicas_doadas_layout = RelativeLayout(size_hint_y=None, height=50) #CESTA BASICA DONATIONS
        cesta_basicas_doadas_image = Image(source = "images/icones/cesta_basicas_doadas.png", 
                                       size_hint_x = 1,
                                       size_hint_y = None,
                                       height = 50, 
                                       allow_stretch = True,
                                       keep_ratio = False)
        cesta_basicas_doadas_label = Label(text=f"{cesta_basicas_doadas}",
                                        color = (1,1,1,1),
                                        size_hint_y= 1,
                                        size_hint_x= 2.375,
                                        font_size = 25,
                                        halign='left',
                                        text_size= (940, None))
        cesta_basicas_doadas_layout.add_widget(cesta_basicas_doadas_image)
        cesta_basicas_doadas_layout.add_widget(cesta_basicas_doadas_label)

        suplementações_doadas_layout = RelativeLayout(size_hint_y=None, height=50) #SUPLE UNICA DONATIONS
        suplementações_doadas_image = Image(source = "images/icones/suplementações_doadas.png", 
                                       size_hint_x = 1,
                                       size_hint_y = None,
                                       height = 50, 
                                       allow_stretch = True,
                                       keep_ratio = False)
        suplementações_doadas_label = Label(text=f"{suplementação_unicas_doadas}",
                                        color = (1,1,1,1),
                                        size_hint_y= 1,
                                        size_hint_x= 2.375,
                                        font_size = 25,
                                        halign='left',
                                        text_size= (940, None))
        suplementações_doadas_layout.add_widget(suplementações_doadas_image)
        suplementações_doadas_layout.add_widget(suplementações_doadas_label)

        faixa_ca = Image(source = "images\icones\porcentagem_tipos_ca.png", #Faixa Porcentagem dos tipos
                                       size_hint_x = 1,
                                       size_hint_y = None,
                                       height = 50, 
                                       allow_stretch = True,
                                       keep_ratio = False)
        
        box_layout.add_widget(pacientes_ativos_layout)
        box_layout.add_widget(pacientes_falecidos_layout)
        box_layout.add_widget(cesta_basicas_doadas_layout)
        box_layout.add_widget(suplementações_doadas_layout)
        box_layout.add_widget(faixa_ca)
        
        ca_list = []
        #DATA TIPO DE CA CADASTRADO
        for pacientes in os.listdir("data/pacientes"):
            with open(f"data/pacientes/{pacientes}", "r") as file:
                data = file.readlines()
                ca = data[8].replace("\n", "").capitalize() #Tirar os \n e Padronizar letra maiucula
                ca = unidecode(ca) #Tirar os acentos para pradonizar ainda mais
                ca_list.append(ca)

        #Arruma a Lista tirando as Virgulas no Meio e tirando os espações no final para Cada Valor o mais compacto possivel
        nova_ca_list = []
        for valor in ca_list:
            valores_split = valor.split(",")
            nova_ca_list.extend([v.strip() for v in valores_split])

        frequencias = Counter(nova_ca_list)
        total_valores = len(nova_ca_list)

        # Exibe o número de ocorrências, a porcentagem e o valor correspondente para cada item
        for valor, frequencia in frequencias.items():
            porcentagem = (frequencia / total_valores) * 100
            ca_layout = RelativeLayout(size_hint_y=None, height=50) #CADA CA
            ca_image = Image(source = "images/icones/faixa_ca.png", 
                                       size_hint_x = 1,
                                       size_hint_y = None,
                                       height = 50, 
                                       allow_stretch = True,
                                       keep_ratio = False)
            ca_ca_label = Label(text=f"{valor}:",
                                        color = (1,1,1,1),
                                        size_hint_y= 1,
                                        size_hint_x= 1.5,
                                        font_size = 25,
                                        halign='left',
                                        text_size= (940, None))
            ca_porcentagem_label = Label(text=f"{frequencia} = {porcentagem:.2f}%",
                                        color = (1,1,1,1),
                                        size_hint_y= 1,
                                        size_hint_x= 2.3,
                                        font_size = 25,
                                        halign='left',
                                        text_size= (940, None))
            ca_layout.add_widget(ca_image)
            ca_layout.add_widget(ca_ca_label)
            ca_layout.add_widget(ca_porcentagem_label)
            box_layout.add_widget(ca_layout)
        
        Scroll_View.add_widget(box_layout)
        self.add_widget(Scroll_View)


    def to_cadastro(self):
        self.manager.switch_to(CadastrosWindow(name="cadastro"))
    def to_suple(self):
        self.manager.switch_to(SuplementaçãoWindow(name="suplementação"))
    def to_materiais(self):
        self.manager.switch_to(MateriaisWindow(name="materiais"))

class CadastrarWindow(Screen):
    def to_cadastro(self):
        self.manager.switch_to(CadastrosWindow(name="cadastro"))

    def change_to_cadastro(self):
        self.manager.switch_to(CadastrosWindow())

    def change_button(self, image_id, image_name):
        """Uma Genialidade para Modificar a Imagem do Botão Deixando-o "Ativo" """

        if image_id.source == f'images/botões/botão {image_name} off.png':
            image_id.source = f'images/botões/botão {image_name}.png'
        else:
            image_id.source = f'images/botões/botão {image_name} off.png'
    
    def sus_limit_mask(self):
        """Define um Limite de Caracteres para o TextInput "sus" """
        sus = self.ids.sus.text
        if len(sus) > 15:
            sus = sus[:15]
        self.ids.sus.text = sus

    def formatar_number(self):
        """Define um Limite de Caracteres para o TextInput "telefone" """

        telefone = self.ids.telefone.text

        if len(telefone) > 11:
            telefone = telefone[:11]

        self.ids.telefone.text = telefone
    
    def formatar_fnumber(self):
        """Define um Limite de Caracteres para o TextInput "telefone_fixo" """

        telefone_fixo = self.ids.telefone_fixo.text

        if len(telefone_fixo) > 8:
            telefone_fixo = telefone_fixo[:8]

        self.ids.telefone_fixo.text = telefone_fixo

    def datan_mask(self):
        """Define um Limite de Caracteres e um padrão de escrita para o TextInput "data_de_nascimento" """

        text = self.ids.data_de_nascimento.text
        data = text.replace("/", "").replace(" ", "")
        count = len(data)
        pattern = "  /  /  "
        if data.isnumeric():
                if count == 1:
                    pattern = f"{data[0]} /  /  "
                    self.ids.data_de_nascimento.text = pattern
                if count == 2:
                    pattern = f"{data[0]}{data[1]}/  /  "
                    self.ids.data_de_nascimento.text = pattern
                    if not keyboard.is_pressed('backspace'):
                        pyautogui.press('right') #pular linha aqui
                if count == 3:
                    pattern = f"{data[0]}{data[1]}/{data[2]} /  "
                    self.ids.data_de_nascimento.text = pattern
                if count == 4:
                    pattern = f"{data[0]}{data[1]}/{data[2]}{data[3]}/  "
                    self.ids.data_de_nascimento.text = pattern
                    if not keyboard.is_pressed('backspace'):
                        pyautogui.press('right') #pular linha aqui    
                if count == 5:
                    pattern = f"{data[0]}{data[1]}/{data[2]}{data[3]}/{data[4]} "
                    self.ids.data_de_nascimento.text = pattern
                if count == 6:
                    pattern = f"{data[0]}{data[1]}/{data[2]}{data[3]}/{data[4]}{data[5]}"
                    self.ids.data_de_nascimento.text = pattern
                if count > 6:
                    self.ids.data_de_nascimento.text = text[:8]
        else:
            self.ids.data_de_nascimento.text = ""
    
    def datac_mask(self):
        """Define um Limite de Caracteres e um padrão de escrita para o TextInput "data_de_cadastro" """

        text = self.ids.data_de_cadastro.text
        data = text.replace("/", "").replace(" ", "")
        count = len(data)
        pattern = "  /  /  "
        if data.isnumeric():
                if count == 1:
                    pattern = f"{data[0]} /  /  "
                    self.ids.data_de_cadastro.text = pattern
                if count == 2:
                    pattern = f"{data[0]}{data[1]}/  /  "
                    self.ids.data_de_cadastro.text = pattern
                    if not keyboard.is_pressed('backspace'):
                        pyautogui.press('right') #pular linha aqui
                if count == 3:
                    pattern = f"{data[0]}{data[1]}/{data[2]} /  "
                    self.ids.data_de_cadastro.text = pattern
                if count == 4:
                    pattern = f"{data[0]}{data[1]}/{data[2]}{data[3]}/  "
                    self.ids.data_de_cadastro.text = pattern
                    if not keyboard.is_pressed('backspace'):
                        pyautogui.press('right') #pular linha aqui    
                if count == 5:
                    pattern = f"{data[0]}{data[1]}/{data[2]}{data[3]}/{data[4]} "
                    self.ids.data_de_cadastro.text = pattern
                if count == 6:
                    pattern = f"{data[0]}{data[1]}/{data[2]}{data[3]}/{data[4]}{data[5]}"
                    self.ids.data_de_cadastro.text = pattern
                if count > 6:
                    self.ids.data_de_cadastro.text = text[:8]
        else:
            self.ids.data_de_cadastro.text = ""

    def cpf_limit_mask(self):
        cpf = self.ids.cpf.text
        if not "." in cpf:
            if len(cpf) > 11:
                cpf = cpf[:11]
                self.ids.cpf.text = cpf
            
            else:
                self.ids.cpf.text = cpf

    def cpf_mask(self):
        """Define um Limite de Caracteres e um padrão de escrita para o TextInput "cpf" """

        cpf = self.ids.cpf.text
        if len(cpf) == 11:
             self.ids.cpf.text = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        if len(cpf) == 14:
            cpf2 = cpf.replace(".", "")
            cpf3 = cpf2.replace("-", "")
            self.ids.cpf.text = cpf3

    def insert_today_date(self):
        """Utiliza da Biblioteca Datetime para Importar a Data Atual do Dispositivo"""

        data_atual = datetime.now()
        data_formatada = data_atual.strftime('%d/%m/%y')
        self.ids.data_de_cadastro.text = data_formatada
    
    def save_data(self):
        """Salva Todos os Dados Referentes aos TextInputs da Pagina e Compila eles Dentro do Banco de Dados"""

        datas = []
        invalidos = []
        tratamento = []
        cpf_pattern = re.compile("[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}")
        date_pattern = re.compile("[0-9]{2}/[0-9]{2}/[0-9]{2}")

        nome = self.ids.nome.text
        if nome != "":
            datas.append(nome)
            
        else:
            invalidos.append("Nome")

        conjugue = self.ids.conjugue.text
        if conjugue != "":
            datas.append(conjugue)
        else:
            invalidos.append("Conjugue")

        cpf = self.ids.cpf.text
        if re.fullmatch(cpf_pattern, cpf) != None:
            datas.append(cpf)
        else:
            invalidos.append("CPF")
        
        sus = self.ids.sus.text
        if len(sus) == 15:
            datas.append(sus)
        else:
            invalidos.append("SUS")

        dependentes = self.ids.dependentes.text
        if dependentes != "":
            datas.append(dependentes)
        else:
            invalidos.append("Dependentes")

        data_de_nascimento = self.ids.data_de_nascimento.text
        if re.fullmatch(date_pattern, data_de_nascimento) != None:
            datas.append(data_de_nascimento)
        else:
            invalidos.append("Data de Nascimento")

        telefone = self.ids.telefone.text
        if len(telefone) >= 8:
            datas.append(telefone)
        else:
            invalidos.append("Telefone")

        telefone_fixo = self.ids.telefone_fixo.text
        if len(telefone_fixo) == 8:
            datas.append(telefone_fixo)
        else:
            invalidos.append("Telefone Fixo")

        ca = self.ids.ca.text
        if ca != "":
            datas.append(ca)
        else:
            invalidos.append("ca")

        rua = self.ids.rua.text
        if rua != "":
            datas.append(rua)
        else:
            invalidos.append("Rua")

        bairro = self.ids.bairro.text
        if bairro != "":
            datas.append(bairro)
        else:
            invalidos.append("Bairro")

        cidade = self.ids.cidade.text
        if cidade != "Selecione...":
            datas.append(cidade)
        else:
            invalidos.append("Cidade")

        numero = self.ids.numero.text
        if numero != "":
            datas.append(numero)
        else:
            invalidos.append("Numero")

        data_de_cadastro = self.ids.data_de_cadastro.text
        if re.fullmatch(date_pattern, data_de_cadastro) != None:
            datas.append(data_de_cadastro)
        else:
            invalidos.append("Data de Cadastro")

        if not "off" in self.ids.acompanhamento_image.source:
            tratamento.append(self.ids.acompanhamento_image.source)
            if invalidos == []:
                self.ids.acompanhamento_image.source = "images/botões/botão acompanhamento off.png"
        if not "off" in self.ids.cirurgia_image.source:
            tratamento.append(self.ids.cirurgia_image.source)
            if invalidos == []:
                self.ids.cirurgia_image.source = "images/botões/botão cirurgia off.png"
        if not "off" in self.ids.quimioterapia_image.source:
            tratamento.append(self.ids.quimioterapia_image.source)
            if invalidos == []:
                self.ids.quimioterapia_image.source = "images/botões/botão quimioterapia off.png"
        if not "off" in self.ids.radioterapia_image.source:
            tratamento.append(self.ids.radioterapia_image.source)
            if invalidos == []:
                self.ids.radioterapia_image.source = "images/botões/botão radioterapia off.png"
        datas.append(tratamento)

        #Esquema para Tirar as Variaveis Que não Podem em um Arquivo
        file_name = nome.replace(" ", "_").replace("\t", "")
        if invalidos == []:
            #Gambiarra para apagar o File Antigo Caso Isso Seja Uma Moficação No Arquivo
            if self.ids.reference_to_modify_file.text != "":
                old_file_name = f"{self.ids.reference_to_modify_file.text}"
                os.remove(old_file_name)
            
            #Criar o Arquivo De paciente
            with open(f"data/pacientes/{file_name}.txt", "w") as file:
                for data in datas:
                    if isinstance(data, list):
                        for dat in data:
                            file.write(dat + " | ")
                        file.write("\n")
                    else:
                        file.write(data + "\n")
            
            self.ids.data_de_cadastro.text = ""
            self.ids.numero.text = ""
            self.ids.cidade.text = "Selecione..."
            self.ids.bairro.text = ""
            self.ids.rua.text = ""
            self.ids.ca.text = ""
            self.ids.telefone_fixo.text = ""
            self.ids.telefone.text = ""
            self.ids.data_de_nascimento.text = ""
            self.ids.dependentes.text = ""
            self.ids.sus.text = ""
            self.ids.cpf.text = ""
            self.ids.conjugue.text = ""
            self.ids.nome.text = ""
            sm.add_widget(CadastrosWindow(name="cadastro"))
            self.manager.switch_to(CadastrosWindow())

        else:
            InvalidPopup(invalidos=invalidos).open()

class PacienteWindow(Screen):
    def remover_paciente(self, *args):
        RemovePacienteWarningChoicePopup(f"{self.ids.label_nome.text}", callback=self.on_confirm_exclusao).open()
    
    def paciente_to_cadastro(self):
        sm.add_widget(PacienteWindow(name="paciente"))
        self.manager.switch_to(CadastrosWindow(name="cadastro"))

    def on_confirm_exclusao(self):
        #Adicionando Novamente a Tela ao SM, pois o sm quando Usado em sequencia de current no mesmo arquivo, apaga a tela do SM
        sm.add_widget(PacienteWindow(name="paciente"))
        self.manager.switch_to(CadastrosWindow())
        

        self.remove_widget(self.menu_content)
        self.remove_widget(self.transparent_widget)

    def declarar_falecido(self, *args):
        paciente_file = "data/pacientes/" + self.ids.label_nome.text.replace(" ", "_") + ".txt"
        diretorio_falecidos = "data/falecidos"
        shutil.copy(paciente_file, diretorio_falecidos)
        #Apenas confirmação caso o Arquivo Não Tenha sido Copiado
        if self.ids.label_nome.text.replace(" ", "_") + ".txt" in os.listdir(diretorio_falecidos):
            os.remove(paciente_file)
            #Adicionando Novamente a Tela ao SM, pois o sm quando Usado em sequencia de current no mesmo arquivo, apaga a tela do SM
            sm.add_widget(PacienteWindow(name="paciente"))
            self.manager.switch_to(CadastrosWindow())
        
        self.remove_widget(self.menu_content)
        self.remove_widget(self.transparent_widget)

    def modificar_paciente(self, paciente, *args):
        """Faz uma Gambiarra para Voltar os Dados do paciente para a screen(CadastrarPaciente) e salva-lo Novamente"""

        sm.add_widget(CadastrarWindow(name="cadastrar"))
        cadastrar_screen = self.manager.get_screen('cadastrar')
        paciente_file = "data/pacientes/" + self.ids.label_nome.text.replace(" ", "_") + ".txt"

        cadastrar_screen.ids.reference_to_modify_file.text = str(paciente)
        cadastrar_screen.ids.nome.text = self.ids.label_nome.text
        cadastrar_screen.ids.conjugue.text = self.ids.label_conjugue.text
        cadastrar_screen.ids.cpf.text = self.ids.label_cpf.text
        cadastrar_screen.ids.data_de_nascimento.text = self.ids.label_data_de_nascimento.text
        cadastrar_screen.ids.dependentes.text = self.ids.label_dependentes.text
        cadastrar_screen.ids.telefone.text = self.ids.label_telefone.text
        cadastrar_screen.ids.telefone_fixo.text = self.ids.label_telefone_fixo.text
        with open(paciente_file, "r") as file:
            data = file.readlines()
            rua = data[9].replace("\n", "")
            bairro = data[10].replace("\n", "")
            cidade = data[11].replace("\n", "")
            numero = data[12].replace("\n", "")
        cadastrar_screen.ids.rua.text = rua 
        cadastrar_screen.ids.bairro.text = bairro
        cadastrar_screen.ids.numero.text = numero
        cadastrar_screen.ids.cidade.text = cidade
        cadastrar_screen.ids.sus.text = self.ids.label_sus.text
        cadastrar_screen.ids.ca.text = self.ids.label_ca.text
        cadastrar_screen.ids.data_de_cadastro.text = self.ids.label_data_de_cadastro.text 
        if "Acompanhamento" in self.ids.label_tratamento.text:
            cadastrar_screen.ids.acompanhamento_image.source = 'images/botões/botão acompanhamento.png'
        if "Cirurgia" in self.ids.label_tratamento.text:
            cadastrar_screen.ids.cirurgia_image.source = 'images/botões/botão cirurgia.png'
        if "Quimioterapia" in self.ids.label_tratamento.text:
            cadastrar_screen.ids.quimioterapia_image.source = 'images/botões/botão quimioterapia.png'
        if "Radioterapia" in self.ids.label_tratamento.text:
            cadastrar_screen.ids.radioterapia_image.source = 'images/botões/botão radioterapia.png' 

        self.remove_widget(self.menu_content)
        self.remove_widget(self.transparent_widget)
        self.manager.current = "cadastrar"

    def remover_options_menu(self, *args):
        """Remove o Menu das tres bolinhas"""

        self.remove_widget(self.menu_content)
        self.remove_widget(self.transparent_widget)

    def options_menu(self):
        """Cria o Menu das Tres bolinhas"""

        #Cria um Widget transparente que cubra toda a tela
        self.transparent_widget = Label(size_hint= (1,1), opacity=0)
        self.add_widget(self.transparent_widget)
        
        #Adiciona um handler para remover o menu quando o usuário tocar no Widget transparente
        self.transparent_widget.bind(on_touch_down=self.remover_options_menu)
        #Pegando o Nome do arquivo Atual
        nome = self.ids.label_nome.text
        nome = nome.replace(" ", "_")
        #Pegando o Link do Paciente Para Colocar na Função
        paciente_file = "data/pacientes/" + nome + ".txt"
        #Cria um BoxLayout com os botões
        self.menu_content = BoxLayout(orientation='vertical')
        btn_modificar = Button(text='Modificar Dados')
        btn_modificar.bind(on_release=lambda *args: self.modificar_paciente(paciente_file, *args))
        
        btn_falecido = Button(text='Declarar Como Falecido')
        btn_falecido.bind(on_release=self.declarar_falecido)
        
        btn_remover = Button(text='Remover Paciente')
        btn_remover.bind(on_release=self.remover_paciente)
        self.menu_content.add_widget(btn_modificar)
        self.menu_content.add_widget(btn_falecido)
        self.menu_content.add_widget(btn_remover)
        
        #Adiciona o BoxLayout na tela de cadastro do paciente
        self.add_widget(self.menu_content)
        self.menu_content.pos_hint = {'x': 0.785, 'y': 0.675}
        self.menu_content.size_hint = (0.2, 0.2)

class PacienteFalecidoWindow(Screen):
    def remover_paciente(self, *args):
        RemoveFPacienteWarningChoicePopup(f"{self.ids.label_fnome.text}", callback=self.on_confirm_exclusao).open()

    def paciente_to_cadastro(self):
        sm.add_widget(PacienteFalecidoWindow(name="pacientefalecido"))
        self.manager.switch_to(CadastrosWindow())

    def on_confirm_exclusao(self):
        #Adicionando Novamente a Tela ao SM, pois o sm quando Usado em sequencia de current no mesmo arquivo, apaga a tela do SM
        sm.add_widget(PacienteWindow(name="pacientefalecido"))
        self.manager.switch_to(CadastrosWindow())

        self.remove_widget(self.menu_content)
        self.remove_widget(self.transparent_widget)
    
    def declarar_vivo(self, *args):
        """Move os Dados do Paciente para a Sessão de Pacientes Vivos"""

        fpaciente_file = "data/falecidos/" + self.ids.label_fnome.text.replace(" ", "_") + ".txt"
        diretorio_pacientes = "data/pacientes"
        shutil.copy(fpaciente_file, diretorio_pacientes)
        #Apenas confirmação caso o Arquivo Não Tenha sido Copiado
        if self.ids.label_fnome.text.replace(" ", "_") + ".txt" in os.listdir(diretorio_pacientes):
            os.remove(fpaciente_file)
            #Adicionando Novamente a Tela ao SM, pois o sm quando Usado em sequencia de current no mesmo arquivo, apaga a tela do SM
            sm.add_widget(PacienteFalecidoWindow(name="pacientefalecido"))
            self.manager.switch_to(CadastrosWindow())

        self.remove_widget(self.menu_content)
        self.remove_widget(self.transparent_widget)

    def remover_options_menu(self, *args):
        """O Menu das tres bolinhas"""
        self.remove_widget(self.menu_content)
        self.remove_widget(self.transparent_widget)

    def options_menu(self):
        """Cria o Menu das Tres bolinhas"""
        # Cria um Widget transparente que cubra toda a tela
        self.transparent_widget = Label(size_hint= (1,1), opacity=0)
        self.add_widget(self.transparent_widget)
        
        # Adiciona um handler para remover o menu quando o usuário tocar no Widget transparente
        self.transparent_widget.bind(on_touch_down=self.remover_options_menu)
        #Pegando o Nome do arquivo Atual
        nome = self.ids.label_fnome.text
        nome = nome.replace(" ", "_")
        # Cria um BoxLayout com os botões
        self.menu_content = BoxLayout(orientation='vertical')
        
        btn_vivo = Button(text='Declarar Como Vivo')
        btn_vivo.bind(on_release=self.declarar_vivo)
        
        btn_remover = Button(text='Remover Paciente')
        btn_remover.bind(on_release=self.remover_paciente)
        self.menu_content.add_widget(btn_vivo)
        self.menu_content.add_widget(btn_remover)
        
        # Adiciona o BoxLayout na tela de cadastro do paciente
        self.add_widget(self.menu_content)
        
        # Posiciona o BoxLayout na tela
        self.menu_content.pos_hint = {'x': 0.785, 'y': 0.675}
        self.menu_content.size_hint = (0.2, 0.2)

class AdicionarEstoqueWindow(Screen):
    def to_suple(self):
        self.manager.switch_to(SuplementaçãoWindow(name="suplementação"))
   
    def change_main_icon(self, id):
        self.ids.main_icon.source = id.source
    
    def save_data(self):
        invalidos = []
        datas = []

        alimento = self.ids.Alimento.text
        if alimento != "":
            datas.append(alimento)
        else:
            invalidos.append("Alimento")

        quantidade = self.ids.quantidade_estoque.text
        self.ids.quantidade_estoque.text
        datas.append(quantidade)

        icon = self.ids.main_icon.source
        if icon != "images/icones/branco.png":
            datas.append(icon)
        else:
            invalidos.append("Icone")

        file_alimento = alimento.replace(" ", "_").replace("|", "-")
        if invalidos == []:
            with open(f"data/estoque/{file_alimento}.txt", "w") as file:
                for data in datas:
                    file.write(data + "\n")
            
            self.ids.Alimento.text = ""
            self.ids.quantidade_estoque.text = "1"
            self.ids.main_icon.source = "images/icones/branco.png"
            self.manager.switch_to(SuplementaçãoWindow(name="suplementação"))
        else:
            InvalidPopup(invalidos=invalidos).open()

class EnviarSuplementaçãoWindow(Screen):
    def __init__(self, **kwargs):
        super(EnviarSuplementaçãoWindow, self).__init__(**kwargs)

        scroll_view = self.ids.pendentes_scrollview
        layout = BoxLayout(orientation='vertical', size_hint=(1, None), spacing=1)
        layout.bind(minimum_height=layout.setter('height'))

        #Desativando a label caso não possua nenhum banner
        if len(os.listdir("data\data\cesta_basica_donations/")) != 0:
            cesta_basica_image = Image(source = "images/icones/Cesta Básicas icone.png",
                                    size_hint_y = None,
                                    size_hint_x =0.359,
                                    height = 40,
                                    pos_hint = {"x": 0, "y": 0},
                                    allow_stretch = False,
                                    keep_ratio = False)
            layout.add_widget(cesta_basica_image)


        #Atualizando a Lista com os Novos Dados
        for doação in os.listdir("data/data/cesta_basica_donations/"):
            with open(f"data\data\cesta_basica_donations/{doação}", "r") as file:
                nome_endereço = file.readlines()
                Nome = nome_endereço[0].replace("\n", "")
                Endereço = nome_endereço[1].replace("\n", "")

                banner_cesta = RelativeLayout(size_hint_y=None, height=260, width=100)
                
                banner_cesta_image =  Image(source = "images/icones/Banner_add_remove.png",
                                            allow_stretch = False,
                                            keep_ratio = False)
                
                Nome_paciente_label = Label(text = Nome,
                                            color = (1,1,1,1),
                                            size_hint_y= 1.65,
                                            size_hint_x= 1.05,
                                            font_size = 25,
                                            halign='left',
                                            text_size= (500, None))
                
                Endereço_paciente_label = Label(text = Endereço,
                                            color = (1,1,1,1),
                                            size_hint_y= 1.5,
                                            size_hint_x= 0.75,
                                            font_size = 25,
                                            halign='left',
                                            text_size= (300, 300))
                
                Accept_botão_button = Button(text = f"data/data/cesta_basica_donations/{doação}",
                                            color = (0,0,0,0),
                                            background_color = (0,0,0,0),
                                            size_hint = (0.18, 0.35),
                                            pos_hint = {"x": 0.78, "y": 0.57})
                Accept_botão_button.bind(on_release=self.accept_donation_cesta)
                
                Recuse_botão_button = Button(text = f"data/data/cesta_basica_donations/{doação}",
                                            color = (0,0,0,0),
                                            background_color = (0,0,0,0),
                                            size_hint = (0.18, 0.35),
                                            pos_hint = {"x": 0.78, "y": 0.07})
                Recuse_botão_button.bind(on_release=self.recuse_donation_cesta)
                
                banner_cesta.add_widget(banner_cesta_image)
                banner_cesta.add_widget(Nome_paciente_label)
                banner_cesta.add_widget(Endereço_paciente_label)
                banner_cesta.add_widget(Accept_botão_button)
                banner_cesta.add_widget(Recuse_botão_button)

            layout.add_widget(banner_cesta) 

        if len(os.listdir("data/data/suplementação_unica_donations")) != 0:
            cesta_basica_image = Image(source = "images/icones/Suplementação Única.png",
                                    size_hint_y = None,
                                    size_hint_x =0.5,
                                    height = 40,
                                    pos_hint = {"x": 0, "y": 0},
                                    allow_stretch = False,
                                    keep_ratio = False)
            layout.add_widget(cesta_basica_image)


        #Atualizando a Lista com os Novos Dados
        for doação in os.listdir("data/data/suplementação_unica_donations"):
            with open(f"data/data/suplementação_unica_donations/{doação}", "r") as file:
                nome_suplementação = file.readlines()
                Nome = nome_suplementação[0].replace("\n", "")
                Suplementação = nome_suplementação[1].replace("\n", "")

                banner_suplementação = RelativeLayout(size_hint_y=None, height=260, width=100)
                
                banner_cesta_image =  Image(source = "images/icones/Banner_add_remove.png",
                                            allow_stretch = False,
                                            keep_ratio = False)
                
                Nome_paciente_label = Label(text = Nome,
                                            color = (1,1,1,1),
                                            size_hint_y= 1.65,
                                            size_hint_x= 1.05,
                                            font_size = 25,
                                            halign='left',
                                            text_size= (500, None))
                
                Suplementação_paciente_label = Label(text = Suplementação,
                                            color = (1,1,1,1),
                                            size_hint_y= 1.5,
                                            size_hint_x= 0.75,
                                            font_size = 25,
                                            halign='left',
                                            text_size= (300, 300))
                
                Accept_botão_button = Button(text = f"data/data/suplementação_unica_donations/{doação}",
                                            color = (0,0,0,0),
                                            background_color = (0,0,0,0),
                                            size_hint = (0.18, 0.35),
                                            pos_hint = {"x": 0.78, "y": 0.57})
                Accept_botão_button.bind(on_release=self.accept_donation_suplementação)
                
                Recuse_botão_button = Button(text = f"data/data/suplementação_unica_donations/{doação}",
                                            color = (0,0,0,0),
                                            background_color = (0,0,0,0),
                                            size_hint = (0.18, 0.35),
                                            pos_hint = {"x": 0.78, "y": 0.07})
                Recuse_botão_button.bind(on_release=self.recuse_donation_suplementação)
                
                banner_suplementação.add_widget(banner_cesta_image)
                banner_suplementação.add_widget(Nome_paciente_label)
                banner_suplementação.add_widget(Suplementação_paciente_label)
                banner_suplementação.add_widget(Accept_botão_button)
                banner_suplementação.add_widget(Recuse_botão_button)

            layout.add_widget(banner_suplementação) 
            
        scroll_view.add_widget(layout)

    #DEFS DE REGISTRO DE DOAÇÂO E A ATIVAÇÂO DA INIT
    def pendentes_cesta_basica(self):
        #Pegando Todos os Itens Setados para Serem da Cesta Basica
        try:#Caso o Padrão de Cesta não Tenha sido Criado
            with open("data/data/cesta_basica_set.txt", "r") as file:
                cesta_basica_set = file.readlines()
                for i in range(len(cesta_basica_set)):
                        cesta_basica_set[i] = "data/estoque/" + cesta_basica_set[i].replace("\n", "").replace("|", "-") + ".txt"
        
            #Verificando se Todos os Itens Estão no Estoque
            invalidos = []
            quantidade_list = []
            for item in cesta_basica_set:
                #Try Caso um Item Setado AnteriorMente na Cesta Basica Não Exista mais no sistema
                try:
                    with open(item, "r") as a:
                        suple_info = a.readlines()
                        quantidade = int(suple_info[1].replace("\n", ""))
                
                    if quantidade == 0:
                        invalidos.append(item.replace("data/estoque/", "").replace(".txt", ""))
                        
                    else:
                        #Verificar caso Ocorra de Dois Suplementos Iguias na Cesta com 1 quantidade!
                        for suple in quantidade_list:
                            if item in suple.keys() and 0 in suple.values():
                                invalidos.append(item.replace("data/estoque/", "").replace(".txt", ""))

                        if invalidos == []:
                            if cesta_basica_set.count(item) == 1:
                                quantidade -= 1
                            else:
                                quantidade -= cesta_basica_set.count(item)
                                if quantidade < 0:
                                    invalidos.append(item.replace("data/estoque/", "").replace(".txt", ""))
                            quantidade_list.append({item: quantidade})
            
                    #Abrindo um Popup com os Invalidos
                    if invalidos != []:
                        EstoqueMissingPopup(invalidos).open()
                    
                    #Com Todos os Items da Cesta no Estoque, Bora Criar o Arquivo!
                    else:   
                        #Extraindo os Dados para Criar o Arquivo de Doação
                        paciente_nome = (self.ids.cesta_basica_paciente.text).replace(" ", "_")
                        file_of_paciente = "data/pacientes/" + paciente_nome.replace(" ", "_").replace("|", "-") + ".txt"
                        paciente_list = []
                    
                        for paciente in os.listdir("data/pacientes/"):
                            paciente_list.append(paciente)
                        
                        if paciente_nome + ".txt" in paciente_list: 
                            with open(f"{file_of_paciente}", "r") as file:
                                data = file.readlines()
                                endereço = f"{data[10]}, {data[9]}, {data[12]} | {data[11]}".replace("\n", "")

                            #Criando o Arquivo de Doação
                            with open(f"data/data/cesta_basica_donations/{paciente_nome}.txt", "w") as file:
                                file.write(paciente_nome + "\n" + endereço)
                        
                        else:
                            self.ids.cesta_basica_paciente.text = ""
                            InvalidPopup(["Paciente Inválido"]).open()

                except:
                    os.remove("data/data/cesta_basica_set.txt")
                    os.remove(f"data/data/cesta_basica_donations/{paciente_nome}.txt")
                    EstoqueMissingPopup(["Algum Suplemento\nEstava Excluida do Sistema\nPortanto, o Padrão de Cesta Basica\nfoi Desfeito...\nCrie-o Novamente!"]).open()
            self.manager.switch_to(EnviarSuplementaçãoWindow())
        
        except:
            InvalidPopup(["O Padrão de Cesta Basica\nNão esta Definido!\n\nClique Nos 3 Pontos para\nCria-lo Novamente!"]).open()
    def pendentes_suplementação_unica(self):
        #Verificando se o Nome do Paciente e da Suplementação Estão Corretos
        suple_list = []
        for suple in os.listdir("data/estoque"):
            suple_list.append(suple)
        
        paciente_list = []
        for paciente in os.listdir("data/pacientes"):
            paciente_list.append(paciente)
        suplementação_paciente_nome = (self.ids.suplementação_unica_paciente.text).replace(" ", "_")
        paciente_suplementação = self.ids.suplementação_unica_suplementação.text
        paciente_suplementação_to_verify = paciente_suplementação.replace(" ", "_").replace("|", "-")
        
        if suplementação_paciente_nome + ".txt" in paciente_list and paciente_suplementação_to_verify + ".txt" in suple_list:
            suple_file = "data/estoque/" + paciente_suplementação_to_verify + ".txt"
            
            #Verificando se Há o Suplemento Disponivel
            with open(suple_file, "r") as file:
                suple_data = file.readlines()
                quantidade = int(suple_data[1].replace("\n", ""))
                if quantidade == 0:
                    EstoqueMissingPopup([paciente_suplementação]).open()
                else:
                    #Criando o Arquivo de Doação
                    with open(f"data/data/suplementação_unica_donations/{suplementação_paciente_nome}_{paciente_suplementação_to_verify}.txt", "w") as file:
                        file.write(suplementação_paciente_nome + "\n" + paciente_suplementação)
                    self.manager.switch_to(EnviarSuplementaçãoWindow())

        else:
            InvalidPopup(["Paciente ou Suplementação Inválidos"]).open()
    
    #Botões de Accept e Recuse do ScrollView Pendentes
    def accept_donation_cesta(self, button):
        #Puxando o Arquivo referente ao Banner Pelo Text do Butão
        doação_file = button.text
        #Pegando Todos os Itens Setados para Serem da Cesta Basica
        with open("data/data/cesta_basica_set.txt", "r") as file:
            cesta_basica_set = file.readlines()
            for i in range(len(cesta_basica_set)):
                    cesta_basica_set[i] = "data/estoque/" + cesta_basica_set[i].replace("\n", "").replace("|", "-") + ".txt"

        #Verificando se Todos os Itens Estão no Estoque Mesmo apos a Entrada do Banner, Vai que Acabou
        invalidos = []
        quantidade_list = []
        for item in cesta_basica_set:
            try:
                with open(item, "r") as a:
                    suple_info = a.readlines()
                    quantidade = int(suple_info[1].replace("\n", ""))
                    if quantidade == 0:
                        invalidos.append(item.replace("data/estoque/", "").replace(".txt", ""))
                        
                    else:
                        #Verificar caso Ocorra de Dois Suplementos Iguias na Cesta com 1 quantidade!
                        for suple in quantidade_list:
                            if item in suple.keys() and 0 in suple.values():
                                invalidos.append(item.replace("data/estoque/", "").replace(".txt", ""))

                        if invalidos == []:
                            if cesta_basica_set.count(item) == 1:
                                quantidade -= 1
                            else:
                                quantidade -= cesta_basica_set.count(item)
                                if quantidade < 0:
                                    invalidos.append(item.replace("data/estoque/", "").replace(".txt", ""))
                            quantidade_list.append({item: quantidade})
            except:
                ItemMissing = item.replace("data/estoque/", "").replace(".txt", "")
                os.remove("data/data/cesta_basica_set.txt")
                os.remove(doação_file)
                self.manager.switch_to(EnviarSuplementaçãoWindow())
                EstoqueMissingPopup([f"O Suplemento:\n\n{ItemMissing}\n\nEstava Excluida do Sistema\nPortanto, o Padrão de Cesta Basica\ne a Doação foram Desfeitos\nCrie-os Novamente!"]).open()
        
        #Abrindo um popup com invalidos
        if invalidos != []:
            EstoqueMissingPopup(invalidos).open()

        #Reescrever o Arquivo do Suplemento
        if len(quantidade_list) == len(cesta_basica_set):
            for item in quantidade_list:
                for k,v in item.items():
                    with open(k, "r") as file:
                        data = file.readlines()
                        data[1] = str(v) + "\n"
                    with open(k, "w") as file:
                        for line in data:
                                file.write(line)
            #Arquivando que a Doanção foi Contabilizada na Info
            with open("data/data/info.txt", "r+") as file:
                data = file.readlines()
                cesta_basica_cont = data[0].replace("\n", "")
                cesta_basica_cont = int(cesta_basica_cont) + 1
                data[0] = str(cesta_basica_cont) + "\n"
                file.seek(0)
                for line in data:
                    file.write(line)
            #Removendo o Arquivo de Doação e Reiniciando a Lista de Pendentes
            os.remove(doação_file)
            self.manager.switch_to(EnviarSuplementaçãoWindow())
    def recuse_donation_cesta(self, button):
        #Puxando o Arquivo referente ao Banner Pelo Text do Butão
        doação_file = button.text
        #Apenas Excluindo o Arquivo do Banner e Reiniciando a Lista de Pendentes
        os.remove(doação_file)
        self.manager.switch_to(EnviarSuplementaçãoWindow())
    
    def accept_donation_suplementação(self, button):
        #Puxando o Arquivo referente ao Banner Pelo Text do Butão
        doação_file = button.text
        #Achando o File da Suplementação Para Conferir se Tem em Estoque
        with open(doação_file, "r") as file:
            data = file.readlines()
            suple_file = data[1].replace("|", "-").replace(" ", "_")
            suple = "data/estoque/" + suple_file + ".txt"
        #Verificando se Há o Suplemento Disponivel
        try: #Um Try Caso a Suplementação Tenho Sido Excluida Apos a Criação da Doação
            with open(suple, "r") as file:
                suple_data = file.readlines()
                quantidade = int(suple_data[1].replace("\n", ""))
            if quantidade == 0:
                EstoqueMissingPopup([data[1]]).open()
            
            else:
                #Alterando o File do Suplemento e Reitirando o Banner
                quantidade -= 1
                suple_data[1] = str(quantidade) + "\n"
                with open(suple, "w") as File:
                    for line in suple_data:
                        File.write(line)
                #Salvando a Doação
                with open("data/data/info.txt", "r+") as file:
                    data = file.readlines()
                    suplementação_unica_cont = data[1].replace("\n", "")
                    suplementação_unica_cont = int(suplementação_unica_cont) + 1
                    data[1] = str(suplementação_unica_cont) + "\n"
                    file.seek(0)
                    for line in data:
                        file.write(line)
                #Removendo o Arquivo de Doação e Reiniciando a Lista de Pendentes
                os.remove(doação_file)   
                self.manager.switch_to(EnviarSuplementaçãoWindow())
        except:
            os.remove(doação_file)  
            self.manager.switch_to(EnviarSuplementaçãoWindow())
            EstoqueMissingPopup([f"O Suplemento:\n\n{data[1]}\n\nEstava Excluida do Sistema\nPortanto, a Doação Foi Desfeita\nCrie-a Novamente!"]).open()
    def recuse_donation_suplementação(self, button):
        #Puxando o Arquivo referente ao Banner Pelo Text do Butão
        doação_file = button.text
        #Apenas Excluindo o Arquivo do Banner e Reiniciando a Lista de Pendentes
        os.remove(doação_file)
        self.manager.switch_to(EnviarSuplementaçãoWindow())

    #Primeiro Dropdown
    def open_scrollview_1(self):
        if self.ids.suplementação_unica_paciente.size_hint_x == 0.228:
            self.ids.suplementação_unica_paciente.size_hint_x = 0
        else:
            self.ids.suplementação_unica_paciente.size_hint_x = 0.228

        if self.ids.paciente_choicer_cesta_basica.size_hint_y == 0:
            self.ids.paciente_choicer_cesta_basica.size_hint_y = 0.2
            
            if len(self.ids.paciente_choicer_cesta_basica.children) > 0:
                self.ids.paciente_choicer_cesta_basica.remove_widget(self.ids.paciente_choicer_cesta_basica.children[0])

            box_layout = BoxLayout(orientation='vertical', spacing=0, size_hint_y=None)
            box_layout.bind(minimum_height=box_layout.setter('height'))



            # Adicionar botões ao BoxLayout
            file_pacientes = 'data/pacientes'
            for paciente in os.listdir(file_pacientes):
                #pegando o nome do paciente
                with open(f"data/pacientes/{paciente}", "r") as file:
                    info_paciente = file.readlines()
                    paciente_nome = info_paciente[0].replace("\n", "")

                button = Button(text=f"{paciente_nome}",
                                size_hint_y=None,
                                size_hint_x= 1,
                                font_size = 20,
                                color = (0,0,0,1),
                                height=40,
                                background_normal = "images/icones/branco.png",
                                halign='left',
                                text_size= (280, None))
                
                #gambiarra para tirar todas as infos a partir do nome
                button.bind(on_press=self.name_to_textinput_1)
                box_layout.add_widget(button)

            # Adicionar BoxLayout ao ScrollView
            self.ids.paciente_choicer_cesta_basica.add_widget(box_layout)
        else:
            self.ids.paciente_choicer_cesta_basica.size_hint_y = 0
    def paciente_filter_1(self):
        if len(self.ids.paciente_choicer_cesta_basica.children) > 0:
            self.ids.paciente_choicer_cesta_basica.remove_widget(self.ids.paciente_choicer_cesta_basica.children[0])

        box_layout = BoxLayout(orientation='vertical', spacing=0, size_hint_y=None)
        box_layout.bind(minimum_height=box_layout.setter('height'))

        # Adicionar botões ao BoxLayout
        file_pacientes = 'data/pacientes'
        for paciente in os.listdir(file_pacientes):
            if self.ids.cesta_basica_paciente.text in paciente:
            #pegando o nome do paciente
                with open(f"data/pacientes/{paciente}", "r") as file:
                        info_paciente = file.readlines()
                        paciente_nome = info_paciente[0].replace("\n", "")

                button = Button(text=f"{paciente_nome}",
                                size_hint_y=None,
                                size_hint_x= 1,
                                font_size = 20,
                                color = (0,0,0,1),
                                height=40,
                                background_normal = "images/icones/branco.png",
                                halign='left',
                                text_size= (280, None))
                
                #gambiarra para tirar todas as infos a partir do nome
                button.bind(on_press=self.name_to_textinput_1)
                box_layout.add_widget(button)
                
            # Adicionar BoxLayout ao ScrollView
        self.ids.paciente_choicer_cesta_basica.add_widget(box_layout)
    def name_to_textinput_1(self, button):
        self.ids.cesta_basica_paciente.text = str(button.text)

    #Segundo Dropdown
    def open_scrollview_2(self):
        if self.ids.suplementação_unica_suplementação.size_hint_x == 0.228:
            self.ids.suplementação_unica_suplementação.size_hint_x = 0
        else:
            self.ids.suplementação_unica_suplementação.size_hint_x = 0.228
        
        if self.ids.paciente_choicer_suplementação_unica.size_hint_y == 0:
            self.ids.paciente_choicer_suplementação_unica.size_hint_y = 0.2
            
            if len(self.ids.paciente_choicer_suplementação_unica.children) > 0:
                self.ids.paciente_choicer_suplementação_unica.remove_widget(self.ids.paciente_choicer_suplementação_unica.children[0])

            box_layout = BoxLayout(orientation='vertical', spacing=0, size_hint_y=None)
            box_layout.bind(minimum_height=box_layout.setter('height'))

            # Adicionar botões ao BoxLayout
            file_pacientes = 'data/pacientes'
            for paciente in os.listdir(file_pacientes):
                #pegando o nome do paciente
                with open(f"data/pacientes/{paciente}", "r") as file:
                    info_paciente = file.readlines()
                    paciente_nome = info_paciente[0].replace("\n", "")

                button = Button(text=f"{paciente_nome}",
                                size_hint_y=None,
                                size_hint_x= 1,
                                font_size = 20,
                                color = (0,0,0,1),
                                height=40,
                                background_normal = "images/icones/branco.png",
                                halign='left',
                                text_size= (280, None))
                
                #gambiarra para tirar todas as infos a partir do nome
                button.bind(on_press=self.name_to_textinput_2)
                box_layout.add_widget(button)

            # Adicionar BoxLayout ao ScrollView
            self.ids.paciente_choicer_suplementação_unica.add_widget(box_layout)
                
        else:
            self.ids.paciente_choicer_suplementação_unica.size_hint_y = 0
    def paciente_filter_2(self):
        if len(self.ids.paciente_choicer_suplementação_unica.children) > 0:
            self.ids.paciente_choicer_suplementação_unica.remove_widget(self.ids.paciente_choicer_suplementação_unica.children[0])

        box_layout = BoxLayout(orientation='vertical', spacing=0, size_hint_y=None)
        box_layout.bind(minimum_height=box_layout.setter('height'))

        # Adicionar botões ao BoxLayout
        file_pacientes = 'data/pacientes'
        for paciente in os.listdir(file_pacientes):
            if self.ids.suplementação_unica_paciente.text in paciente:
            #pegando o nome do paciente
                with open(f"data/pacientes/{paciente}", "r") as file:
                        info_paciente = file.readlines()
                        paciente_nome = info_paciente[0].replace("\n", "")

                button = Button(text=f"{paciente_nome}",
                                size_hint_y=None,
                                size_hint_x= 1,
                                font_size = 20,
                                color = (0,0,0,1),
                                height=40,
                                background_normal = "images/icones/branco.png",
                                halign='left',
                                text_size= (280, None))
                
                #gambiarra para tirar todas as infos a partir do nome
                button.bind(on_press=self.name_to_textinput_2)
                box_layout.add_widget(button)
                
            # Adicionar BoxLayout ao ScrollView
        self.ids.paciente_choicer_suplementação_unica.add_widget(box_layout)
    def name_to_textinput_2(self, button):
        self.ids.suplementação_unica_paciente.text = str(button.text)

    #Terceiro Dropdown
    def open_scrollview_3(self):
        if self.ids.suplementação_choicer_suplementação_unica.size_hint_y == 0:
            self.ids.suplementação_choicer_suplementação_unica.size_hint_y = 0.2
            
            if len(self.ids.suplementação_choicer_suplementação_unica.children) > 0:
                self.ids.suplementação_choicer_suplementação_unica.remove_widget(self.ids.suplementação_choicer_suplementação_unica.children[0])

            box_layout = BoxLayout(orientation='vertical', spacing=0, size_hint_y=None)
            box_layout.bind(minimum_height=box_layout.setter('height'))

            file_estoque = 'data/estoque'
            for suplementação in os.listdir(file_estoque):
                #Pegando o Nome do Paciente
                with open(f"data/estoque/{suplementação}", "r") as file:
                    info_suple = file.readlines()
                    suple_nome = info_suple[0].replace("\n", "")

                button = Button(text=f"{suple_nome}",
                                size_hint_y=None,
                                size_hint_x= 1,
                                font_size = 20,
                                color = (0,0,0,1),
                                height=40,
                                background_normal = "images/icones/branco.png",
                                halign='left',
                                text_size= (280, None))
                
                #gambiarra para tirar todas as infos a partir do nome
                button.bind(on_press=self.name_to_textinput_3)
                box_layout.add_widget(button)

            # Adicionar BoxLayout ao ScrollView
            self.ids.suplementação_choicer_suplementação_unica.add_widget(box_layout)
                
        else:
            self.ids.suplementação_choicer_suplementação_unica.size_hint_y = 0
    def paciente_filter_3(self):
        if len(self.ids.suplementação_choicer_suplementação_unica.children) > 0:
            self.ids.suplementação_choicer_suplementação_unica.remove_widget(self.ids.suplementação_choicer_suplementação_unica.children[0])

        box_layout = BoxLayout(orientation='vertical', spacing=0, size_hint_y=None)
        box_layout.bind(minimum_height=box_layout.setter('height'))

        # Adicionar botões ao BoxLayout
        file_estoque = 'data/estoque'
        for suplementação in os.listdir(file_estoque):
            if self.ids.suplementação_unica_suplementação.text in suplementação:
            #pegando o nome do paciente
                with open(f"data/estoque/{suplementação}", "r") as file:
                    info_suple = file.readlines()
                    suple_nome = info_suple[0].replace("\n", "")

                button = Button(text=f"{suple_nome}",
                                size_hint_y=None,
                                size_hint_x= 1,
                                font_size = 20,
                                color = (0,0,0,1),
                                height=40,
                                background_normal = "images/icones/branco.png",
                                halign='left',
                                text_size= (280, None))
                
                #gambiarra para tirar todas as infos a partir do nome
                button.bind(on_press=self.name_to_textinput_3)
                box_layout.add_widget(button)
                
            # Adicionar BoxLayout ao ScrollView
        self.ids.suplementação_choicer_suplementação_unica.add_widget(box_layout)
    def name_to_textinput_3(self, button):
        self.ids.suplementação_unica_suplementação.text = str(button.text)

    def to_cadastro(self):
        self.manager.switch_to(CadastrosWindow(name="cadastro"))
    
    def to_materiais(self):
        self.manager.switch_to(MateriaisWindow(name="materiais"))

    def to_info(self):
        self.manager.switch_to(InfoWindow(name="info"))

    def to_suple(self):
        self.manager.switch_to(SuplementaçãoWindow(name="suplementação"))

    def to_adicionar_estoque(self):
        self.manager.switch_to(AdicionarEstoqueWindow(name="adicionarestoque"))

class AdicionarMaterialWindow(Screen):
    def to_materiais(self):
        self.manager.switch_to(MateriaisWindow(name="materiais"))

    #DEFS DE ESCOLHA DE ESTADO DO MATERIAL
    def change_pessimo(self):
        if self.ids.péssimo_image.source == f'images/botões/botão péssimo off.png':
            self.ids.péssimo_image.source = f'images/botões/botão péssimo.png'
            self.ids.ok_image.source = f'images/botões/botão ok off.png'
            self.ids.perfeito_image.source = f'images/botões/botão perfeito off.png'
        else:
            self.ids.péssimo_image.source = f'images/botões/botão péssimo off.png'

    def change_ok(self):
        if self.ids.ok_image.source == f'images/botões/botão ok off.png':
            self.ids.ok_image.source = f'images/botões/botão ok.png'
            self.ids.péssimo_image.source = f'images/botões/botão péssimo off.png'
            self.ids.perfeito_image.source = f'images/botões/botão perfeito off.png'
        else:
            self.ids.ok_image.source = f'images/botões/botão ok off.png'

    def change_perfeito(self):
        if self.ids.perfeito_image.source == f'images/botões/botão perfeito off.png':
            self.ids.perfeito_image.source = f'images/botões/botão perfeito.png'
            self.ids.péssimo_image.source = f'images/botões/botão péssimo off.png'
            self.ids.ok_image.source = f'images/botões/botão ok off.png'
        else:
            self.ids.perfeito_image.source = f'images/botões/botão perfeito off.png'

    def datar_mask(self):
        """Defini um limite e formato dos caracteres do TextInput "data_de_recepção" """

        text = self.ids.data_de_recepção.text
        data = text.replace("/", "").replace(" ", "")
        count = len(data)
        pattern = "  /  /  "
        if data.isnumeric():
                if count == 1:
                    pattern = f"{data[0]} /  /  "
                    self.ids.data_de_recepção.text = pattern
                if count == 2:
                    pattern = f"{data[0]}{data[1]}/  /  "
                    self.ids.data_de_recepção.text = pattern
                    if not keyboard.is_pressed('backspace'):
                        pyautogui.press('right') #pular linha aqui
                if count == 3:
                    pattern = f"{data[0]}{data[1]}/{data[2]} /  "
                    self.ids.data_de_recepção.text = pattern
                if count == 4:
                    pattern = f"{data[0]}{data[1]}/{data[2]}{data[3]}/  "
                    self.ids.data_de_recepção.text = pattern
                    if not keyboard.is_pressed('backspace'):
                        pyautogui.press('right') #pular linha aqui    
                if count == 5:
                    pattern = f"{data[0]}{data[1]}/{data[2]}{data[3]}/{data[4]} "
                    self.ids.data_de_recepção.text = pattern
                if count == 6:
                    pattern = f"{data[0]}{data[1]}/{data[2]}{data[3]}/{data[4]}{data[5]}"
                    self.ids.data_de_recepção.text = pattern
                if count > 6:
                    self.ids.data_de_recepção.text = text[:8]
        else:
            self.ids.data_de_recepção.text = ""

    def insert_today_date(self):
        """Usa a Biblioteca Datetime para Inserir no TextInput a Data Atual do Dispositivo"""

        data_atual = datetime.now()
        data_formatada = data_atual.strftime('%d/%m/%y')
        self.ids.data_de_recepção.text = data_formatada

    def save_data(self):
        """Pega todos os Dados da Screen e Compila Tudo no Banco de Dados"""
        datas = []
        invalidos = []
        date_pattern = re.compile("[0-9]{2}/[0-9]{2}/[0-9]{2}")
        conservação = ""

        material = self.ids.material_type.text
        if material != "Selecione...":
            datas.append(material)
        else:
            invalidos.append("Tipo")
        
        doador = self.ids.doador.text
        if doador != "":
            datas.append(doador)
        else:
            invalidos.append("Doador")

        if not "off" in self.ids.péssimo_image.source:
            datas.append(self.ids.péssimo_image.source)
            conservação = "péssimo"
        if not "off" in self.ids.ok_image.source:
            datas.append(self.ids.ok_image.source)
            conservação = "ok"
        if not "off" in self.ids.perfeito_image.source:
            datas.append(self.ids.perfeito_image.source)
            conservação = "perfeito"
        if conservação == "":
            invalidos.append("Estado de Conservação")
        
        data_recepção = self.ids.data_de_recepção.text
        if re.fullmatch(date_pattern, data_recepção) != None:
            datas.append(data_recepção)
            date = data_recepção.replace("/", "_")
        else:
            invalidos.append("Data de Recepção")

        emprestado = self.ids.emprestado.text
        pacientes = []
        file_pacientes = 'data/pacientes'
        for paciente in os.listdir(file_pacientes):
            #pegando o nome do paciente
            with open(f"data/pacientes/{paciente}", "r") as file:
                info_paciente = file.readlines()
                pacientes.append(info_paciente[0].replace("\n", ""))
        pacientes.append("")
        if emprestado in pacientes:
            datas.append(emprestado)
        else:
            invalidos.append("Emprestado")
        
        if invalidos == []:
            with open(f"data/materiais/{material}_{conservação}_{doador}_{date}.txt", "w") as file: 
                    for data in datas:
                        file.write(data + "\n")

            self.ids.emprestado.text = "Selecione..."
            self.ids.data_de_recepção.text = ""
            self.ids.doador.text = ""
            self.ids.material_type.text = "Selecione..."
            self.ids.péssimo_image.source = "images/botões/botão péssimo off.png"
            self.ids.ok_image.source = "images/botões/botão ok off.png"
            self.ids.perfeito_image.source = 'images/botões/botão perfeito off.png'
            self.manager.switch_to(MateriaisWindow(name="materiais"))
        else:
            InvalidPopup(invalidos=invalidos).open()

    def open_scrollview(self):
        if self.ids.paciente_choicer_add_material.size_hint_y == 0:
            self.ids.paciente_choicer_add_material.size_hint_y = 0.2
            
            if len(self.ids.paciente_choicer_add_material.children) > 0:
                self.ids.paciente_choicer_add_material.remove_widget(self.ids.paciente_choicer_add_material.children[0])

            box_layout = BoxLayout(orientation='vertical', spacing=0, size_hint_y=None)
            box_layout.bind(minimum_height=box_layout.setter('height'))



            # Adicionar botões ao BoxLayout
            file_pacientes = 'data/pacientes'
            for paciente in os.listdir(file_pacientes):
                #pegando o nome do paciente
                with open(f"data/pacientes/{paciente}", "r") as file:
                    info_paciente = file.readlines()
                    paciente_nome = info_paciente[0].replace("\n", "")

                button = Button(text=f"{paciente_nome}",
                                size_hint_y=None,
                                size_hint_x= 1,
                                font_size = 20,
                                color = (0,0,0,1),
                                height=40,
                                background_normal = "images/icones/branco.png",
                                halign='left',
                                text_size= (280, None))
                
                #gambiarra para tirar todas as infos a partir do nome
                button.bind(on_press=self.name_to_textinput)
                box_layout.add_widget(button)

            # Adicionar BoxLayout ao ScrollView
            self.ids.paciente_choicer_add_material.add_widget(box_layout)
            self.ids.paciente_choicer_add_material.scroll_y = 0
                
        else:
            self.ids.paciente_choicer_add_material.size_hint_y = 0

    def paciente_filter(self):
        if len(self.ids.paciente_choicer_add_material.children) > 0:
            self.ids.paciente_choicer_add_material.remove_widget(self.ids.paciente_choicer_add_material.children[0])

        box_layout = BoxLayout(orientation='vertical', spacing=0, size_hint_y=None)
        box_layout.bind(minimum_height=box_layout.setter('height'))

        # Adicionar botões ao BoxLayout
        file_pacientes = 'data/pacientes'
        for paciente in os.listdir(file_pacientes):
            if self.ids.emprestado.text in paciente:
            #pegando o nome do paciente
                with open(f"data/pacientes/{paciente}", "r") as file:
                        info_paciente = file.readlines()
                        paciente_nome = info_paciente[0].replace("\n", "")

                button = Button(text=f"{paciente_nome}",
                                size_hint_y=None,
                                size_hint_x= 1,
                                font_size = 20,
                                color = (0,0,0,1),
                                height=40,
                                background_normal = "images/icones/branco.png",
                                halign='left',
                                text_size= (280, None))
                
                #gambiarra para tirar todas as infos a partir do nome
                button.bind(on_press=self.name_to_textinput)
                box_layout.add_widget(button)
                
            # Adicionar BoxLayout ao ScrollView
        self.ids.paciente_choicer_add_material.add_widget(box_layout)
        self.ids.paciente_choicer_add_material.scroll_y = 0

    def name_to_textinput(self, button):
        self.ids.emprestado.text = str(button.text)

class DescriçãoMateriaisWindow(Screen):
    def remover_material(self, *args):
        data_recepção = self.ids.label_material_recepção.text
        data_recepção = data_recepção.replace("/", "_")
        material_file = f"data/materiais/{self.ids.label_material_nome.text}_{self.ids.label_material_conservação.text}_{self.ids.label_material_doador.text}_{data_recepção}.txt"
        RemoveMaterialWarningChoicePopup(material_file, f"{self.ids.label_material_nome.text}", callback=self.on_confirm_exclusao).open()
    
    def on_confirm_exclusao(self):
        self.manager.switch_to(MateriaisWindow())
        adicionar_material_screen = self.manager.get_screen('adicionarmaterial')
        adicionar_material_screen.__init__()
        #Adicionando Novamente a Tela ao SM, pois o sm quando Usado em sequencia de current no mesmo arquivo, apaga a tela do SM
        sm.add_widget(DescriçãoMateriaisWindow(name="descriçãomateriais"))

    def modificar_material(self, *args):
        adicionar_material_screen = self.manager.get_screen('adicionarmaterial')

        adicionar_material_screen.ids.material_type.text =  self.ids.label_material_nome.text
        adicionar_material_screen.ids.doador.text =  self.ids.label_material_doador.text
        adicionar_material_screen.ids.data_de_recepção.text =  self.ids.label_material_recepção.text
        adicionar_material_screen.ids.emprestado.text =  self.ids.label_material_emprestado.text

        if "péssimo" in self.ids.label_material_conservação.text:
            adicionar_material_screen.ids.péssimo_image.source = 'images/botões/botão péssimo.png'
        elif "ok" in self.ids.label_material_conservação.text:
            adicionar_material_screen.ids.ok_image.source = 'images/botões/botão ok.png'
        elif "perfeito" in self.ids.label_material_conservação.text:
            adicionar_material_screen.ids.perfeito_image.source = 'images/botões/botão perfeito.png'

        self.manager.add_widget(AdicionarMaterialWindow(name="adicionarmaterial"))
        self.manager.current = "adicionarmaterial"
        self.remove_widget(self.menu_content)
        self.remove_widget(self.transparent_widget)

    def remover_options_menu(self, *args):
        self.remove_widget(self.menu_content)
        self.remove_widget(self.transparent_widget)

    def options_menu(self):
        # Cria um Widget transparente que cubra toda a tela
        self.transparent_widget = Label(size_hint= (1,1), opacity=0)
        self.add_widget(self.transparent_widget)
        
        # Adiciona um handler para remover o menu quando o usuário tocar no Widget transparente
        self.transparent_widget.bind(on_touch_down=self.remover_options_menu)
        
        # Cria um BoxLayout com os botões
        self.menu_content = BoxLayout(orientation='vertical')
        btn_modificar = Button(text='Modificar Dados')
        btn_modificar.bind(on_release=self.modificar_material)
        
        btn_remover = Button(text='Remover Mateiral')
        btn_remover.bind(on_release=self.remover_material)
        self.menu_content.add_widget(btn_modificar)
        self.menu_content.add_widget(btn_remover)
        
        # Adiciona o BoxLayout na tela de cadastro do paciente
        self.add_widget(self.menu_content)
        
        # Posiciona o BoxLayout na tela
        self.menu_content.pos_hint = {'x': 0.785, 'y': 0.675}
        self.menu_content.size_hint = (0.2, 0.2)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("vida.kv")
sm = WindowManager(transition=NoTransition())

screens = [CadastrosWindow(name="cadastro"), SuplementaçãoWindow(name="suplementação"), 
           MateriaisWindow(name="materiais"), InfoWindow(name="info"), CadastrarWindow(name="cadastrar"), 
           AdicionarEstoqueWindow(name="adicionarestoque"), PacienteWindow(name="paciente"),
           DescriçãoMateriaisWindow(name="descriçãomateriais"), AdicionarMaterialWindow(name="adicionarmaterial"), 
           EnviarSuplementaçãoWindow(name="enviarsuplementação"), PacienteFalecidoWindow(name="pacientefalecido")]

for screen in screens:
    sm.add_widget(screen)

class VidaViva(App):
    def build(self):
        return sm

if __name__ == "__main__":
    VidaViva().run()