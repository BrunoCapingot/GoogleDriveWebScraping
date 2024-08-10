class Csv:
    def __init__(self):
        self._estrutura = []
        self._tema = None
        self._subTema = None

    def setTema(self, tema):
        self._tema = tema

    def setSubTema(self, subTema):
        self._subTema = subTema

    def cadTema(self):
        self._estrutura.append([self._tema])

    def getList(self):
        return self._estrutura

    def cadSubTema(self, tema, subTema):
        for pos in range(0, len(self._estrutura)):
            if self._estrutura[pos][0] == tema:
                self._estrutura[pos].append(subTema)