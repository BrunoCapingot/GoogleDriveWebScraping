from typing import List, Dict, Union, Any


def requisito_extracao_aulas_semanais(dado: list, save_dict: Dict[str, Union[str, List[str]]] = None) -> list[str | list | Any]:
    if save_dict is None:
        save_dict = {'aulas_semanais': ''}
    if dado and dado.__len__() != 1:
        if dado[-1].__len__() == 1:
            save_dict['aulas_semanais'] = dado.pop()
    return list((save_dict['aulas_semanais'], dado))
