def requisito_extracao_carga_horaria_total(dado: list, save_dict=dict(c_h_total=str())):
    if save_dict is None:
        save_dict = {'c_h_total': ''}
    save_dict['c_h_total'] = dado.pop()
    return save_dict['c_h_total'], dado
