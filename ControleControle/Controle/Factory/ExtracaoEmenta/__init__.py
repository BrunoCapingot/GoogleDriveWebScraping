import csv
from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo
from Projeto.ControleView import ControleView
from Projeto.ControleModelo import ControleModelo, Arquivo


class ExtracaoEmenta(Processo):
    def executar(self,ControleModelo:ControleModelo):
        ControleModelo.set_model_data(type_model='caminhos_de_relacao',key_dict='texto_bruto')
        for name_item in ControleModelo.get_diretorio_pointer_name_items():
            print(ControleModelo.read(type_read='txt',Arquivo=Arquivo(nome=name_item,caminho=ControleModelo.get_model_data())))



    def requisito_extracaoPrimariaEmEmenta_old(self,ControleModelo:ControleModelo,ControleView:ControleView, csv_data_lista=list(),save_dict=dict(diciplina=str(), ementa=str())):
        cond = False
        texto = ''
        total_text = total_text.replace('HORÁ-\n', 'HORÁ')
        for index, linha in enumerate(total_text.split('\n')):
            if 'ANEXO IV' in linha and not '..' in linha:
                argv.append(str(index))
                break
            elif 'ANEXO  III' in linha and not '..' in linha:
                argv.append(str(index))
        pos_one = argv.pop()
        pos_dois = argv.pop()
        for posicao in range(int(pos_dois), int(pos_one)):
            dt = total_text.split('\n')
            onde_ta = dt[posicao]
            if 'HORÁRIA' in dt[posicao]:
                dn = total_text.split('\n')[posicao + 1].split()
                while dn.__len__():
                    if dn[-1].isalpha():
                        texto += dn.pop(0)
                    else:
                        dn.pop()
                save_dict['diciplina'] = texto
                texto = ''

            elif 'EMENTA  ' in dt[posicao] and not 'III' in dt[posicao]:
                ss = posicao + 1
                while True:
                    texto += dt[ss]
                    ss += 1
                    if 'BIBLIOGRAFIA BÁ SICA' in dt[ss] or 'BIBLIOGRAFIA BÁSICA  ' in dt[ss]: break
                save_dict['ementa'] = texto
                texto = ''
                if 'BIBLIOGRAFIA BÁ SICA' in dt[ss] or 'BIBLIOGRAFIA BÁSICA  ' in dt[ss] or 'BIBLIOGRA FIA BÁSICA' in dt[ss]:
                    cond = True
                else:
                    cond = False
            elif save_dict['ementa'] != '' and save_dict['diciplina'] != '' and cond == True:
                csv_data_lista.append(save_dict.copy())
                cond = False
        csv_file_path = os.path.join(DataInput.get_caminhos_de_relacao()['ementa'],
                                     '{}'.format(item_dir_name.replace('.pdf', '.csv')))
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=['diciplina', 'ementa'])
            csv_writer.writeheader()
            for data in csv_data_lista:
                csv_writer.writerow(data)
            Os.save(type_save='txt', arquivo=Arquivo(nome=item_dir_name, caminho=DataInput.get_caminhos_de_relacao()['ementa'],conteudo=str(csv_data_lista)))
