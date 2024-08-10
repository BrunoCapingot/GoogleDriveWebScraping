class Arquivo:
    def __init__(self, nome, caminho, conteudo=''):
        self.atribute_table = [nome, caminho, conteudo]

    def set_name(self, nome):
        self.atribute_table[0] = nome

    def set_caminho(self, caminho):
        self.atribute_table[1] = caminho

    def set_conteudo(self, conteudo):
        self.atribute_table[2] = conteudo

    def get_name(self):
        return self.atribute_table[0]

    def get_caminho(self):
        return self.atribute_table[1]

    def get_conteudo(self):
        return self.atribute_table[2]


