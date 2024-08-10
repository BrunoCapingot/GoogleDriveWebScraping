
class ControleProcessos:
    def __init__(self):
        self.object_tables = [list(), list()]
    def add_process_list(self,process_list:list)->None:
        print('ProcessControl :: lista_de_processo_atual --> {}'.format(self.object_tables[1]))
        print('ProcessControl :: autalizando_para_nova_lista --> {}'.format(process_list))
        #var = [print('ProcessControl :: add_process_list {}'.format(processo) for processo in process_list)]
        self.object_tables[1] = process_list
    def adicionar_processo(self,processo):
        self.object_tables[1].append(processo)

    def remover_processo(self, objeto:str):
        if objeto in self.object_tables[1]:
            pass

    def get_lista_processo(self) -> list:
        return self.object_tables[1]