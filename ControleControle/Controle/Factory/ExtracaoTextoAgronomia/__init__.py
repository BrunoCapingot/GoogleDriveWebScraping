import csv
from Projeto.ControleControle.Controle.Factory.Casos import PreRequisito, AulasSemanais, CargaHoraria, AulasPraticas, AulasTeoricas, Diciplina, CodigoDaDiciplina, Periodo
from Projeto.ControleModelo.Arquivo import Arquivo
from Projeto.ControleModelo import ControleModelo
from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo

class ExtracaoDadosAgronomia(Processo):
    def executar(self, ControleModelo:ControleModelo,suport=0, txt_fracionado=str(),item_dir_name='Bacharelado em Agronomia',save_dict=dict(),csv_dict=dict()) -> None:
        ControleModelo.set_model_data(type_model='caminhos_de_relacao',key_dict='txt_fracionado')
        for dado in ControleModelo.get_conteudo_do_arquivo(type_arq='txt',Arquivo=Arquivo(nome=item_dir_name.replace('pdf','txt'),caminho=ControleModelo.get_model_data())).split('\n'):
            if dado.__len__() != 0 and dado != '':
                dado = dado.split()
                if dado != ' ' and (not 'Total' in dado and not 'AGRONOMIA ' in dado and dado.__len__() > 5 and not 'ATC-202' in dado):
                    save_dict['pre_requisito'], dado = PreRequisito.requisito_extracao_pre_requisito(dado=dado)
                    save_dict['aulas_semanais'], dado = AulasSemanais.requisito_extracao_aulas_semanais(dado=dado)
                    save_dict['c_h_total'], dado = CargaHoraria.requisito_extracao_carga_horaria_total(dado=dado)
                    save_dict['aulas_praticas'], dado = AulasPraticas.requisito_extracao_aulas_praticas(dado=dado)
                    save_dict['aulas_teoricas'], dado = AulasTeoricas.requisito_extracao_aulas_teoricas(dado=dado)
                    save_dict['diciplina'], dado = Diciplina.requisito_extracao_nome_diciplina(dado=dado)
                    save_dict['codigo_da_diciplina'], dado = CodigoDaDiciplina.requisito_extracao_codigo_da_diciplina(dado=dado)
                    save_dict['periodo'], dado = Periodo.requisito_extracao_periodo(dado=dado)
                    csv_dict = save_dict
                elif 'ATC-202' in dado:
                    pass
                
                with open(r'C:\Users\CPGT\Desktop\WebScrapingGeral\Projeto\Documentos\Download\Csv\dados.csv', mode='a', newline='') as file:
                    fieldnames = ['pre_requisito', 'aulas_semanais', 'c_h_total', 'aulas_praticas','aulas_teoricas', 'diciplina', 'codigo_da_diciplina', 'periodo']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow(csv_dict)
                    save_dict = dict()











