class Presenca():
    def __init__(self):
        pass

    def verifica(self,dadoUm, dadoDois):
        if dadoUm in dadoDois:
            return dadoUm
        else:
            return None