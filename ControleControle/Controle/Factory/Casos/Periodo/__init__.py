from typing import List, Dict, Union, Any


def requisito_extracao_periodo(dado: list, save_dict: Dict[str, Union[str, List[str]]] = None) -> list[
    str | list | Any]:
    if save_dict is None:
        save_dict = {'periodo': ''}
    if dado:
        save_dict['periodo'] = dado.pop()
    return list((save_dict['periodo'], dado))
