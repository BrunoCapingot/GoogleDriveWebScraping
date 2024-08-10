class Condicional:
    def __init__(self):
        self.mapaCondicional = {}

    def preencheMapa(self, condicao, valores):
        self.mapaCondicional[condicao] = valores

    def getMapaCondicional(self):
        return self.mapaCondicional


    def getCondicao(self,condicao):
        return self.mapaCondicional[condicao]



