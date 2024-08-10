import os


class Os:
    def __init__(self): self._atribute_dict = {'ponteiro': str(), 'arquivo': object(), 'caminho': str(), 'caminho_arquivo_completo': str()}

    def set_arquivo_atribute_dict(self, arquivo): self._atribute_dict['arquivo'] = arquivo

    def get_arquivo_atribute_dict(self): return self._atribute_dict['arquivo']

    def set_ponteiro_atribute_dict(self, caminho): self._atribute_dict['ponteiro'] = caminho

    def get_ponteiro_atribute_dict(self): return self._atribute_dict['ponteiro']

    #def setDiretorio(self, caminho): self._atribute_dict['caminho_arquivo_completo'] = caminho

    def limpaDir(self):
        for file_name in os.listdir(self._atribute_dict['ponteiro']):
            file_path = os.path.join(self._atribute_dict['ponteiro'], file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f"Erro ao excluir {file_path}: {e}")

        if not os.listdir(self._atribute_dict['ponteiro']):
            print(f"O diretório {self._atribute_dict['ponteiro']} foi limpo com sucesso.")
        else:
            print(f"O diretório {self._atribute_dict['ponteiro']} não pôde ser limpo.")

    def getDirNameItens(self):
        self.suportList = []
        for nomes in os.listdir(self._atribute_dict['ponteiro']):
            self.suportList.append(nomes)
        return self.suportList

    def getArqPath(self, arquivo):
        return self.ponteiro+'\\'+arquivo

    def setHomePonteiro(self,):
        return os.path.join(os.path.expanduser("~"), "Desktop")

    def getPonteiro(self):
        return self.ponteiro

    def saveArqTxtInDir(self, conteudoTxt, caminhoString):
        caminho = os.path.join(caminhoString)
        file_path = os.path.join(caminho, '{}.txt'.format(self.txtName))
        # print('Salvando arquivo txt gerado em: {}'.format(file_path))
        with open(file_path, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudoTxt)
        print(f"O arquivo foi salvo em: {file_path}")

    def saveArqInDir(self, conteudo, caminho, name):
        caminho = os.path.join(caminho)
        nome = str(name).split('.')
        extensao = nome[1]
        nome = nome[0]
        file_path = os.path.join(caminho, '{}.{}'.format(nome, extensao))
        # print('Salvando arquivo txt gerado em: {}'.format(file_path))
        with open(file_path, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
        print(f"O arquivo foi salvo em: {file_path}")

    def getConteudoArquivo(self):
        conteudo = self.arquivo.read()
        return conteudo

    def openArq(self, caminho, modo, codificacao):
        self.setHomePonteiro()
        self.arquivo = open(self.getPonteiro()+'\\'+caminho, modo, encoding=codificacao)
        return None

    def closeArq(self):
        self.arquivo.close()
        return None


