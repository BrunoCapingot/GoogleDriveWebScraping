from Projeto.Controle.ControlFactory.FactoryArquivo.Arquivo.Escrita.Mapa.Condicional import Condicional
from Projeto.Controle.ControlFactory.FactoryOs.Os import Os
# import pytesseract
import PyPDF2


class Escrita:
    def __init__(self):
        self._mapaCondicional = Condicional()
        self.os = Os()
        self._dirSaveEscrita = None
        self._dirOrigemEscrita = None
        self._arqOrientado = None
        # pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

    def setArquivo(self, nomeArquivo):
        self._arqOrientado = nomeArquivo

    def setSaveEscrita(self, caminho):
        self._dirSaveEscrita = caminho

    def setDirOrigemExcrita(self, caminho):
        self._dirOrigemEscrita = caminho

    def extrairTexto(self):
        diretorio_textos = r'\webScraping\Projeto\Controle\Download\Textos'
        diretorio_pdf = r'\webScraping\Projeto\Controle\Download\projetoPedagogicoCurso'
        self.os.setHomePonteiro()
        self.os.setDiretorio(diretorio_pdf)
        print(self.os.getPonteiro())
        nomes = self.os.getDirNameItens()
        for x in nomes:
            self.os.setHomePonteiro()
            self.os.setDiretorio(diretorio_pdf)
            print('{}-> Excutando extração de texto'.format(x))
            path_arquivo = self.os.getArqPath(x)
            # print(path_arquivo)
            pdf = PyPDF2.PdfReader(path_arquivo)
            paginas = len(pdf.pages)
            tabelas = ''

            mapa_arquivos = {
                'BachareladoemAgronomia.pdf': ['BachareladoemAgronomia.pdf', 40, 106],
                'BachareladoemCienciadaComputacao.pdf': ['BachareladoemCienciadaComputacao.pdf', [[9, 13], [51, 88]]],
                'BachareladoemQuimicaIndustrial.pdf': ['BachareladoemQuimicaIndustrial.pdf', 49, 60],
                'BachareladoemZootecnia.pdf': ['BachareladoemZootecnia.pdf', 50, 60],
                'LicenciaturaemPedagogia.pdf': ['LicenciaturaemPedagogia.pdf', 34, 70],
                'LicenciaturaemQuimica.pdf': ['LicenciaturaemQuimica.pdf', 37, 67],
                'TecnologiaemAlimentos.pdf': ['TecnologiaemAlimentos.pdf', 49, 104],
                'TecnologiaemSistemasparaInternet.pdf': ['TecnologiaemSistemasparaInternet.pdf', 49, 90]
            }

            for mapa in mapa_arquivos:
                if x == mapa_arquivos[mapa][0]:
                    valor = mapa_arquivos[mapa][1]
                    if type(valor) == int:
                        for k in range(0, paginas):
                            page = pdf.pages[k]
                            if mapa_arquivos[mapa][2] >= k >= mapa_arquivos[mapa][1]:
                                tabelas += page.extract_text()
                    elif type(valor) == list:
                        for intervalo in valor:
                            for k in range(0, paginas):
                                page = pdf.pages[k]
                                if intervalo[1] >= k >= intervalo[0]:
                                    tabelas += page.extract_text()
            self.os.setTxtName(str(x).replace('.pdf', ''))
            self.os.setHomePonteiro()
            self.os.setDiretorio(diretorio_textos)
            self.os.saveArqTxtInDir(str(tabelas), self.os.getPonteiro())

    def prepararArquivos(self):
        """
            Responsavel por preparar os arquivo txt,
            molda-los e criar dos moldes o arquivo csv
            :return:
            None
        """
        diretorioFracionado = r'\webScraping\Projeto\Controle\Download\Textos'
        self.os.setHomePonteiro()
        self.os.setDiretorio(diretorioFracionado)
        nomes = self.os.getDirNameItens()

        for nomeArq in nomes:
            print('Preparando arquivo-> {}'.format(nomeArq))
            diretorioFracionado = r'\webScraping\Projeto\Controle\Download\Textos'
            self.os.setHomePonteiro()
            self.os.setDiretorio(diretorioFracionado)
            pathArq = self.os.getArqPath(nomeArq)
            self.os.getOpenArq(pathArq, 'r', 'utf-8')
            texto = str(self.os.getArquivo())
            self.os.closeArq()
            text = ''
            texto = texto.split('\n')

            mapa_instrucoes = {
                'BachareladoemAgronomia.txt': [[6, 35], [40, 42], [47, 54], [55, 64], [65, 70], [75, 78], [84, 94], [95, 104], [105, 109], [114, 122]],
                'BachareladoemCienciadaComputacao.txt': [[0, 3], [4, 5]],
                'BachareladoemQuimicaIndustrial.txt': [[0, 3], [4, 5]],
                'BachareladoemZootecnia.txt': [[0, 3], [4, 5]],
                'LicenciaturaemPedagogia.txt': [[0, 3], [4, 5]],
                'LicenciaturaemQuimica.txt': [[0, 3], [4, 5]],
                'TecnologiaemAlimentos.txt': [[0, 3], [4, 5]],
                'TecnologiaemSistemasparaInternet.txt': [[0, 3], [4, 5]],
            }

            for linha in range(0, len(texto)):
                for instrucaoInt in mapa_instrucoes.items():
                    if nomeArq == instrucaoInt[0]:
                        for instrucao in instrucaoInt[1]:
                            if instrucao[0] <= linha <= instrucao[1]:
                                if texto[linha].split():
                                    text += str(texto[linha].split())+'\n'
            diretorioFracionadoCsv = r'\webScraping\Projeto\Controle\Download\Csv'
            self.os.setHomePonteiro()
            self.os.setDiretorio(diretorioFracionadoCsv)
            self.os.saveArqInDir(text, self.os.getPonteiro(), nomeArq.replace('.txt', '.csv'))
