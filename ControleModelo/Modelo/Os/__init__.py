
from typing import List
from Projeto.ControleModelo.Arquivo import Arquivo
import os
import csv
import requests
from PyPDF2 import PdfReader, PageObject


class Os:
    def __init__(self):
        self._atribute_dict = {'ponteiro': str(), 'Arquivo': object(), 'caminho': str(),
                               'caminho_Arquivo_completo': str()}
    def read(self, type_read:str, Arquivo:Arquivo, dado = str()):
        if type_read == 'txt':
            diretorio = Arquivo.get_caminho() +'\\'+ Arquivo.get_name().replace('.pdf','.txt')
            with open(diretorio, 'r', encoding='utf-8') as txt_file:
                dado+=txt_file.read()
            return dado
        elif type_read == 'csv':
            diretorio = Arquivo.get_caminho() +'\\'+ Arquivo.get_name().replace('.pdf','.csv')
            with open(diretorio, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    dado += '||||'.join(row)
                    dado += '\n'
            return dado


    def save(self, type_save, data_table:list):
        for Arquivo in data_table:
            with open(Arquivo.get_caminho() +'\\'+ Arquivo.get_name().replace('.pdf','.txt'), 'w', encoding='utf-8') as txt_file:
                conent = Arquivo.get_conteudo()
                txt_file.write(Arquivo.get_conteudo())

    def download_arquivo(self, Arquivo:Arquivo):
        response = requests.get(Arquivo.get_conteudo())
         if response.status_code == 200:
            with open(r'{}'.format(Arquivo.get_caminho()+'\\'+Arquivo.get_name()), 'wb') as file:
                file.write(response.content)
            print(f"O Arquivo foi baixado e salvo em {Arquivo.get_caminho()}")
        else:
            print(Arquivo.get_conteudo())
            print("Não foi possível baixar o Arquivo PDF.")
        del Arquivo
    def get_diretorio_pointer_name_items(self):
        return os.listdir(self._atribute_dict['ponteiro'])

    def set_ponteiro(self, caminho_facrionado):
        self._atribute_dict['ponteiro'] = caminho_facrionado
    def get_ponteiro(self)-> str:
        return self._atribute_dict['ponteiro']

    def home_ponteiro(self):
        desktop_path = os.path.expanduser("~/Desktop")
        self._atribute_dict['ponteiro'] = desktop_path
        return desktop_path

    def extract_pdf_content_pointer_path(self,Arquivo:Arquivo)-> List[PageObject]:
        especificacoes_do_Arquivo=list((Arquivo.get_name(),Arquivo.get_caminho()))
        return PdfReader(stream=r''+Arquivo.get_caminho()+'//'+Arquivo.get_name()).pages

