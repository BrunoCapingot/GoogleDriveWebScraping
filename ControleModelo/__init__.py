from Projeto.ControleModelo.Modelo import Modelo
from Projeto.ControleModelo.Arquivo import Arquivo
from Projeto.ControleModelo.DataInput import DataInput


class ControleModelo(Modelo, DataInput):
    def __init__(self):
        super().__init__()
        self.table = dict(save=list(), download=list())

    def add_list_save(self, Arquivo: Arquivo) -> None:
        self.table['save'].append(Arquivo)

    def add_list_download(self, Arquivo: Arquivo) -> None:
        self.table['download'].append(Arquivo)

    def __getitem__(self, item) -> None:
        return self.get_complete_dict()[item]

    def set_model_data(self, type_model: str, key_dict: str) -> None:
        if type_model == 'caminhos_de_relacao':
            self.set_ponteiro(caminho_facrionado=self.get_caminho_relacoes()[key_dict])
        elif type_model == 'localização_nome_link_comando':
            self.set_ponteiro(caminho_facrionado=self.get_localizacao_link_comando()[key_dict])

    def get_model_data(self):
        return self.get_ponteiro()

    def download_list(self) -> None:
        self.download_list_download(self.table['download'])

    def save_list(self, type_save: str) -> None:
        if type_save == 'donwload':
            self.download_list_download(self.table['save'])
        else:
            self.save(type_save=type_save, data_table=self.table['save'])

    def get_conteudo_do_arquivo(self, type_arq: str, Arquivo: Arquivo):
        if type_arq == 'txt':
            return self.get_other_arquivo(type_read=type_arq,Arquivo=Arquivo)
        elif type_arq == 'pdf':
            return self.get_pdf_arq_content(Arquivo=Arquivo)
        elif type_arq == 'csv':
            return self.get_other_arquivo(type_read=type_arq,Arquivo=Arquivo)