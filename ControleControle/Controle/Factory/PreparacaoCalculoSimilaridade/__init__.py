from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo
from Projeto.ControleControle.Controle.Factory.PreparacaoCalculoSimilaridade.Similaridade import Similaridade

class PreparacaCalculoSimilaridade(Processo):
    def get_preparacao() -> list:
        return [Similaridade(nome='calculo_similaridade', prioridade=8)]