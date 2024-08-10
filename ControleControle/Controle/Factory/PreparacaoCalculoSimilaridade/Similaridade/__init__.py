from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo
from Projeto.ControleModelo.Modelo.Os import Os
from Projeto.ControleModelo.Arquivo import Arquivo
from Projeto.ControleModelo.DataInput import DataInput
from Projeto.ControleModelo import ControleModelo
from Projeto.ControleControle.Controle.Factory.PreparacaoCalculoSimilaridade.Jaccard import Jaccard
from sys import argv

class Similaridade(Processo,Jaccard):

    def executar(self, ControleModelo:ControleModelo):
        csv_item = Os.read(type_read='csv',arquivo=Arquivo(nome=item_name_dir, caminho=DataInput.get_caminhos_de_relacao()['csv'],conteudo='')).split('\n')
        for elemento in csv_item:
            if elemento != '':
                dt = elemento.split('||||')
                suport_dict['diciplina'] = dt[0]
                suport_dict['ementa'] = dt[1]
                csv_list.append(suport_dict.copy())
        for dicionario in csv_list:
            if not 'ementa' in dicionario['ementa'] and argv.__len__() < 3:
                argv.append(dicionario)
            elif argv.__len__() == 3:
                print('Similaridade: {}'.format(self.calcular_similaridade(set_one=argv.pop(),set_two=argv.pop())))

