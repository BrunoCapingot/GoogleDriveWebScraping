def requisito_extracao_nome_diciplina(dado: list, dado_tratado: str = "", save_dict=dict(diciplina=str())):
    if save_dict is None:
        save_dict = {'diciplina': ''}

    if dado[0].__len__() == 2 and dado != '':
        while len(dado) > 2:
            if dado[0].__len__() == 2:
                dado_tratado += dado.pop(2)
    elif dado[0].__len__() >= 7:
        while len(dado) > 1:
            if dado[0].__len__() == 7 or dado[0].__len__() == 8 or dado[1].__len__() == 1:
                dado_tratado += dado.pop(1)
            else:
                break
    elif 'OPT' in dado[0]:
        while len(dado) > 1:
            dado_tratado += dado.pop(1)
    save_dict['diciplina'] = dado_tratado
    # save_dict = dict()
    return save_dict['diciplina'], dado
