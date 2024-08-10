from Projeto.ControleControle.Controle.Factory import Factory
from Projeto.ControleControle.Controle.ControleProcessos import ControleProcessos
from Projeto.ControleControle.Controle.ControleMotor import ControleMotor
from Projeto.ControleModelo import ControleModelo
from Projeto.ControleView import ControleView


class Controle(Factory):
    def __init__(self):
        self.estrutura_x = self.get_extrutura_x()
        self.estrutura_x.addInTable(pos=0, object=ControleProcessos())
        self.estrutura_x.addInTable(pos=0, object=ControleMotor())

    def preparacoes_execucao_varredura_web(self) -> None:
        self.inserir_processo(processo=self.get_varredura_web())
        self.carregar(pos=0, object_name='ControleMotor').adicionar_processos(process_list=self.carregar(pos=0, object_name='ControleProcessos').get_lista_processo())
        self.carregar(pos=0, object_name='ControleMotor').iniciar_execucao(object_list=[self.get_web(), ControleModelo(), ControleView()])

    def preparacao_extrair_texto_geral(self) -> None:
        self.inserir_processo(processo=self.get_preparacao_execucao_extracao_texto())
        self.carregar(pos=0, object_name='ControleMotor').adicionar_processos(process_list=self.carregar(pos=0, object_name='ControleProcessos').get_lista_processo())
        self.carregar(pos=0, object_name='ControleMotor').iniciar_execucao(object_list=ControleModelo())

    def preparacao_extrair_texto_posicionado(self):
        pass

    def preparacao_extracao_dados(self):
        self.inserir_processo(processo=self.get_preparacao_execucao_extracao_dados())
        self.carregar(pos=0, object_name='ControleMotor').adicionar_processos(process_list=self.carregar(pos=0, object_name='ControleProcessos').get_lista_processo())
        self.carregar(pos=0, object_name='ControleMotor').iniciar_execucao(object_list=ControleModelo())

    def preparacao_tokenizacao(self):
        self.get_preparacao_tokenizacao()

    def preparacao_extracao_ementa(self):
        self.inserir_processo(processo=self.get_preparacao_extracao_ementa())
        self.carregar(pos=0, object_name='ControleMotor').adicionar_processos(process_list=self.carregar(pos=0, object_name='ControleProcessos').get_lista_processo())
        self.carregar(pos=0, object_name='ControleMotor').iniciar_execucao(object_list=ControleModelo())

    def preparacao_lemantizacao(self):
        self.get_preparacao_lemantizacao()

    def preparacao_extrair_similaridade(self) -> None:
        self.inserir_processo(processo=self.get_preparacao_calculo_similaridade())
        self.carregar(pos=0, object_name='ControleMotor').adicionar_processos(process_list=self.carregar(pos=0, object_name='ControleProcessos').get_lista_processo())
        self.carregar(pos=0, object_name='ControleMotor').iniciar_execucao(object_list=ControleModelo())

    def carregar(self, pos, object_name) -> object:
        return self.estrutura_x.getInTable(type_return=object, pos=pos, object_name=object_name)

    def carregar_motor(self, process_list) -> None:
        self.carregar(pos=0, object_name='ControleMotor').adicionar_processos(process_list=process_list)

    def inserir_processo(self, processo) -> None:
        if type(processo) != list:
            self.estrutura_x.getInTable(type_return=object, pos=0, object_name='ControleProcessos').adicionar_processo(processo=processo)
        elif type(processo) == list:
            self.estrutura_x.getInTable(type_return=object, pos=0, object_name='ControleProcessos').add_process_list(process_list=processo)
