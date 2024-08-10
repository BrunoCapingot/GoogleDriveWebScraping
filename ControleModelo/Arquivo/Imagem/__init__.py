from pdf2image import convert_from_path
from Projeto.Controle.ControlFactory.FactoryOs.Os import Os



class Imagem:
    def __init__(self):
        self.os = Os()
        self.pdfName = None

    #agronomia
    #cienciasDaComputação
    #tecnologiaEmAlimentos
    #tecnologiaEmSistemasDaInternet


    def extractPdfToImage(self):

        diretorio_fracionado = 'r/webScraping/Projeto/Controle/Download/matrizes_curriculares/'
        self.os.setHomePonteiro()
        self.os.setDiretorio(diretorio_fracionado)
        camino_destino_fracionado = r'C:\Users\CPGTEnterprise\Desktop\webScraping\Projeto\Controle\Download\Imagens'
        listDir = self.os.getDirNameItens()
        for item in listDir:
            #self.os.setHomePonteiro()
            #self.os.setDiretorio(pdf_path)
            pdf_name = item.replace('.pdf', '')
            images = convert_from_path(self.os.getPonteiro())
            print('Convertendo pdf: {}'.format(pdf_name))
            for i, image in enumerate(images):
                image = image.convert('L')
                #conteudo caminho nome no metodo saveArqInDir
                self.os.saveArqInDir(image, camino_destino_fracionado, f'{pdf_name.split("/")[-1]}_pagina_{i + 1}.jpg')
                #image.save(os.path.join(camino_destino_fracionado, f'{pdf_name.split("/")[-1]}_pagina_{i + 1}.jpg'), 'JPEG')


