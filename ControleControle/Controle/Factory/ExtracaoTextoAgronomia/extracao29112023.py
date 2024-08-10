from Projeto.ControleModelo import ControleModelo
from Projeto.ControleModelo.Arquivo import Arquivo
from Projeto.ControleModelo.DataInput import DataInput
from Projeto.ControleModelo.Modelo.Os import Os
from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo


class ExtracaoTextoAgronomia(Processo):
    def executar(self, object_list):
        self.execucao(Arquivo=object_list[0], DataInput=object_list[1], Os=object_list[2],
                      ControleModelo=object_list[3])

    def execucao(self, Arquivo: Arquivo, DataInput: DataInput, Os: Os, ControleModelo: ControleModelo):
        lista = list()
        Os.set_ponteiro(DataInput.get_caminhos_de_relacao()['projeto_pedagogico'])
        for item_dir_name in Os.get_dir_pointer_name_items():
            if item_dir_name == 'Bacharelado em Agronomia.pdf':
                total_text = ''
                suport = 0
                pos_dois = 0
                pos_one = 0
                pdf = Os.extract_content_pointer_path(tipo='pdf', Arquivo=Arquivo(nome=item_dir_name, caminho=DataInput.get_caminhos_de_relacao()['projeto_pedagogico'], conteudo=''))
                while len(pdf) != suport:
                    dt = pdf[suport].extract_text()
                    if dt == '' or dt == ' ':
                        suport += 1
                    else:
                        dt = dt.replace('-\n', '')
                        dt = dt.rstrip()
                        total_text += dt
                        suport += 1
                for index, linha in enumerate(total_text.split('\n')):
                    if 'ANEXO II' in linha and not '..' in linha:
                        lista.append(index)
                        break
                    elif 'ANEXO I' in linha and not '..' in linha:
                        lista.append(index)
                while len(lista):
                    pos_one = lista.pop()
                    pos_dois = lista.pop()
                    dict_save = dict()
                    cond = False
                    for posicao in range(pos_dois, pos_one):
                        if 'requisitos' in total_text.split('\n')[posicao]:
                            cond = True
                        elif 'Semestre' in total_text.split('\n')[posicao]:
                            cond = False
                        elif cond:
                            save_dict = dict()
                            if 'Manejo e Conservação do Solo e da' in total_text.split('\n')[posicao]:
                                element_text_list = total_text.split('\n')[posicao] + total_text.split('\n')[posicao+1]
                                print(self.remover_pre_requisitos(data=element_text_list.split()))
                            else:
                                if not 'Água' in total_text.split('\n')[posicao]:
                                    element_text_list = total_text.split('\n')[posicao].split()
                                    print(self.remover_pre_requisitos(data=element_text_list))
            else:
                break

    def remover_pre_requisitos(self,data:list,save_dict=dict(pre_requisito=str()))->dict:
        if len(data)>2:
            if len(data[-1]) == 1 or len(data[-1]) == 7:
                if len(data[-3]) == 7:
                    req = data.pop()
                    req_2 = data.pop()
                    save_dict['pre_requisito'] = data.pop() + req_2 + req
                elif len(data[-3]) == 4:
                    req = data.pop()
                    req_2 = data.pop()
                    req_3 = data.pop()
                    save_dict['pre_requisito'] = data.pop() + req_3 + req_2 + req
                else:
                    save_dict['pre_requisito'] = data.pop()
            elif len(data[-1]) == 4:
                req = data.pop()
                save_dict['pre_requisito'] = data.pop() + req

        return save_dict




    def unir_frase(self, texto: str) -> str:
        return texto.replace(' ', '')

