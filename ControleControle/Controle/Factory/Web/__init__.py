import time
from Projeto.ControleControle.Controle.Factory.Driver import Driver


class Web(Driver):
    def __init__(self):
        super().__init__()

    def open_link(self, link: str):
        self.open("{}".format(link))
        time.sleep(5)

    def clickElementoPorComando(self, comand:str):
        if 'id' in comand:
            self.clickFromXpath(comand)
            return 'xpath'
        elif '/html' in comand:
            self.clickFromXpath(comand)
            return 'xpath'
        elif 'content' in comand:
            self.clickFromCssSelector(comand)
            return 'css_selector'
        elif 'pdfDownloadLinkUrl' in comand:
            return self.getListLink()
        elif 'finishWeb' in comand:
            self.quit()
            return 'finishWeb'
