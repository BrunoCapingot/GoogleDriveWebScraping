from Projeto.ControleControle.Controle.ControleMotor.Motor import Motor


class ControleMotor:
    def __init__(self):
        self.object_table = [Motor()]

    def iniciar_execucao(self, object_list: list):
        self.object_table[0].executar_processos(object_list)

    def adicionar_processos(self, process_list: list) -> None:
        while len(process_list):
            self.object_table[0].adicionar_processo(Processos=process_list.pop())
