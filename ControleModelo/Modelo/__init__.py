from Projeto.ControleModelo.Modelo.Os import Os
from Projeto.ControleModelo.Arquivo import Arquivo


class Modelo(Os):
    def __init__(self):
        super().__init__()


    def download_list_download(self,download_list:list)->None:
        for elemento in download_list:
            self.download_arquivo(Arquivo=elemento)
    def get_other_arquivo(self,type_read:str,Arquivo:Arquivo):
        return self.read(type_read=type_read,Arquivo=Arquivo)
    def get_pdf_arq_content(self,Arquivo:Arquivo)->list:
        self.set_ponteiro(caminho_facrionado=Arquivo.get_caminho())
        eee = caminho_facrionado=Arquivo.get_name()
        return self.extract_pdf_content_pointer_path(Arquivo=Arquivo)
