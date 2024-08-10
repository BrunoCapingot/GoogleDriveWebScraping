from abc import ABC, abstractmethod
from Projeto.ControleControle.Controle.Factory.ExtracaoTexto import ExtracaoDeTexto
from Projeto.ControleControle.Controle.Factory.ExtracaoEmenta import ExtracaoEmenta
from Projeto.ControleControle.Controle.Factory.ExtracaoTextoPosicionado import ExtracaoTextoPosicionado
from Projeto.ControleControle.Controle.Factory.ExtracaoTextoAgronomia import ExtracaoDadosAgronomia
from Projeto.ControleControle.Controle.Factory.PreparacaoLemantizacao import PreparacaoLemantizacao
from Projeto.ControleControle.Controle.Factory.PreparacaoTokenizacao import PreparacaoTokenizacao
from Projeto.ControleControle.Controle.Factory.Web import Web
from Projeto.ControleControle.Controle.Factory.EstruturaX import EstruturaX
from Projeto.ControleControle.Controle.Factory.PreparacaoCalculoSimilaridade import PreparacaCalculoSimilaridade
from Projeto.ControleControle.Controle.Factory.PreparacaoSumarizacao import PreparacaoSumarizacao
from Projeto.ControleControle.Controle.Factory.ExtracaoTexto import ExtracaoDeTexto
from Projeto.ControleControle.Controle.Factory.ExtracaoTextoAgronomia import ExtracaoDadosAgronomia
from Projeto.ControleControle.Controle.Factory.VarreduraWeb import VarreduraWeb


class FacFactory(ABC):
    @abstractmethod
    def get_extrutura_x(self) -> EstruturaX:
        pass

    def get_web(self) -> Web:
        pass

    def get_preparacao_calculo_similaridade(self) -> PreparacaCalculoSimilaridade:
        pass

    def get_varredura_web(self) -> VarreduraWeb:
        pass

    def get_preparacao_tokenizacao(self):
        pass

    def get_preparacao_lemantizacao(self):
        pass

    def get_preparacao_execucao_extracao_dados(self):
        pass

    def get_preparacao_extracao_ementa(self):
        pass


class Factory(FacFactory):
    def get_varredura_web(self) -> VarreduraWeb:
        return VarreduraWeb(nome='varredura_web', prioridade=10)

    def get_extrutura_x(self) -> EstruturaX:
        return EstruturaX()

    def get_web(self) -> Web:
        return Web()

    def get_preparacao_extracao_ementa(self) -> ExtracaoEmenta:
        return ExtracaoEmenta(nome='Preparacao_extracao_ementas', prioridade=8)

    def get_preparacao_execucao_extracao_dados(self) -> list[ExtracaoDadosAgronomia | PreparacaoTokenizacao | PreparacaoLemantizacao | PreparacaoSumarizacao | PreparacaCalculoSimilaridade]:
        return [ExtracaoDadosAgronomia(nome='Preparacao_extracao_agronomia', prioridade=9),
                PreparacaoTokenizacao(nome='PreparacaoTokenizacao',prioridade=9),
                #PreparacaoLemantizacao(nome='PreparacaoLemantizacao',prioridade=8),
                #PreparacaoSumarizacao(nome='PreparacaoSumarizacao',prioridade=8),
                PreparacaCalculoSimilaridade(nome='PreparacaCalculoSimilaridade',prioridade=7)]

    def get_preparacao_calculo_similaridade(self) -> PreparacaCalculoSimilaridade:
        return PreparacaCalculoSimilaridade(nome='PreparacaoCalculoSimilaridade', prioridade=10)

    def get_preparacao_execucao_extracao_texto(self) -> list[ExtracaoDeTexto | ExtracaoTextoPosicionado]:
        return [ExtracaoDeTexto(nome='ExtracaoDeTexto', prioridade=10),ExtracaoTextoPosicionado(nome='ExtracaoDeTextoPosicionada',prioridade=10)]

    def get_preparacao_tokenizacao(self):
        return PreparacaoTokenizacao(nome='PreparacaoTokenizacao', prioridade=10)

    def get_preparacao_lemantizacao(self):
        return PreparacaoLemantizacao(nome='PreparacaoLemantizacao', prioridade=10)
