from Projeto.ControleModelo import ControleModelo
from Projeto.ControleModelo.Arquivo import Arquivo
from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo


class ExtracaoTextoPosicionado(Processo):
    def executar(self,ControleModelo:ControleModelo,content = str(),suport_list=list()) -> None:
        ControleModelo.set_model_data(type_model='caminhos_relacoes',key_dict='texto_bruto')
        for item_dir_name in ControleModelo.get_diretorio_pointer_name_items():
            total_text = ControleModelo.get_conteudo_do_arquivo(type_arq='txt',Arquivo=Arquivo(nome=item_dir_name,caminho=ControleModelo.get_model_data())).split('\n')
            for index, linha in enumerate(total_text):
                if 'ANEXO II' in linha and not '..' in linha:
                    suport_list.append(index)
                    break
                elif 'ANEXO I' in linha and not '..' in linha:
                    suport_list.append(index)
            pos_one = suport_list.pop()
            pos_dois = suport_list.pop()
            cond = False
            for posicao in range(int(pos_dois), int(pos_one)):
                if 'requisitos' in total_text[posicao]:
                    cond = True
                elif 'Semestre' in total_text[posicao]:
                    cond = False
                elif cond:
                    content += '\n' + str(total_text[posicao])
            # '-\n': '',
            ControleModelo.set_model_data(type_model='caminhos_de_relacao', key_dict='substitutions')
            for key, value in ControleModelo.get_caminho_relacoes()['substitutions'].items(): content = content.replace(key, value)
            ControleModelo.set_model_data(type_model='caminhos_de_relacao', key_dict='txt_fracionado')
            ControleModelo.add_list_save(Arquivo=Arquivo(nome=item_dir_name.replace('.pdf', '.txt'),caminho=ControleModelo.get_model_data(), conteudo=content))
            ControleModelo.save_list(type_save='txt')