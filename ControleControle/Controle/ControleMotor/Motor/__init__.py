from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo


class Motor:
    def __init__(self):
        self.process_table = list()

    def executar_processos(self,object_list:list):
        while len(self.process_table):
            dt = self.process_table.pop()
            print('Motor response :: executando_processo --> ### {} ###'.format(dt.get_name()))
            dt.executar(object_list)

    def adicionar_processo(self, Processos:Processo):
        self.process_table.append(Processos)

