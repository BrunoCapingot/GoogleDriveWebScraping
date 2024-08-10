from Projeto.ControleControle.Controle.Factory.PreparacaoCalculoSimilaridade.Casos import Caso
class Jaccard(Caso):

    def calcular_similaridade(self, set_one:dict, set_two:dict) -> float:
        print('Comparando {} :: {}'.format(set_one['diciplina'],set_two['diciplina']))
        return set(set_one['ementa']).intersection(set(set_two['ementa'])).__len__() / set(set_one['ementa']).union(set(set_two['ementa'])).__len__()

