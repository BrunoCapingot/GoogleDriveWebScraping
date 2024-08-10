def requisito_extracao_aulas_praticas(dado: list, save_dict=dict(c_h_total=str())):
    if save_dict is None:
        save_dict = {'aulas_praticas': ''}
    save_dict['aulas_praticas'] = dado.pop()
    return save_dict['aulas_praticas'], dado
