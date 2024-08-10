from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo
from Projeto.ControleModelo import ControleModelo
from Projeto.ControleModelo.Arquivo import Arquivo


class PreparacaoTokenizacao(Processo):
    def executar(self, ControleModelo: ControleModelo, content_arq=list()):
        ControleModelo.set_model_data(type_model='caminhos_de_relacao',key_dict='txt_fracionado')
        for item_dir_name in ControleModelo.get_diretorio_pointer_name_items():
            for linha in ControleModelo.get_conteudo_do_arquivo(type_arq='txt', Arquivo=Arquivo(nome=item_dir_name,caminho=ControleModelo.get_model_data())).split('\n'):
                if linha.__len__() > 1:
                    content_arq.append(linha.split())
            ControleModelo.set_model_data(type_model='caminhos_de_relacao', key_dict='tokenizacao')
            ControleModelo.add_list_save(Arquivo=Arquivo(nome=item_dir_name,caminho=ControleModelo.get_model_data(),conteudo=str(content_arq.copy())))
            ControleModelo.set_model_data(type_model='caminhos_de_relacao', key_dict='txt_fracionado')
        ControleModelo.save_list(type_save='txt')