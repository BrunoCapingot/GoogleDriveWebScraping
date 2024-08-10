from Projeto.ControleControle.Controle.Factory.Casos import Requisitos
from typing import List, Dict, Union, Any


def requisito_extracao_pre_requisito(dado: list, save_dict=None) -> list[str | list | Any]:
    if save_dict is None:
        save_dict = {'pre_requisito': ''}
    if dado.__len__() > 0 and (dado[-1].__len__() == 1 or dado[-1].__len__() == 7):
        save_dict['pre_requisito'] = dado.pop()
        if dado.__len__() > 0 and (dado[-1] == '-'):
            save_dict['pre_requisito'] += dado.pop()
            save_dict['pre_requisito'] += dado.pop()
            if dado.__len__() > 0 and (dado[-1] == '-'):
                save_dict['pre_requisito'] += dado.pop()
                save_dict['pre_requisito'] += dado.pop()
    return list((save_dict['pre_requisito'], dado))
