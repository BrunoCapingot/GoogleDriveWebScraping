class Processo:
    def __init__(self, nome, prioridade):
        self.atribute_table = [nome, prioridade]

    def get_name(self):
        return self.atribute_table[0]

    def get_prioridade(self):
        return self.atribute_table[1]

    def get_estado(self) -> bool:
        return self.atribute_table[2]

    def executar(self, object_list: list):
        pass

    def set_name(self, nome: str):
        self.atribute_table[0] = nome

    def set_prioridade(self, prioridade: int):
        self.atribute_table[1] = prioridade

    def get_preparacao(self) -> list:
        pass
