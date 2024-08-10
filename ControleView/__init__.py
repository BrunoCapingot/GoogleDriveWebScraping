from Projeto.ControleView.View import View


class ControleView(View):
    def __init__(self):
        super().__init__()
        self.logBaseDict = {
            'webScrapingNomePrincipal':'WebScraping :: {}',
            'webScrapingLink':'WebScraping :: Analisando link --> {}',
            'webScrapingComando':'WebScraping :: Executando elemento --> {}',
            'webScrapingDownload':'WebScraping :: Adicionando a lista de Download o Objeto com link --> {}',
            'motorResponse':'Motor Response :: Ligando o Processo --> {}',
        }
    def logForScraping(self, dado:list):
        print(self.logBaseDict[dado[0]].format(dado[1]))

    def print_atoa(self, param):
        print(param)
