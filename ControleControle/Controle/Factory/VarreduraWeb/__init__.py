from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo
from Projeto.ControleModelo import ControleModelo, Arquivo
from Projeto.ControleView import ControleView
from Projeto.ControleModelo.Arquivo import Arquivo
from Projeto.ControleControle.Controle.Factory.Web import Web


class VarreduraWeb(Processo):
    def executar(self, object_list: list) -> None:
        self.execucao(Web=object_list[0],ControleModelo=object_list[1],ControleView=object_list[2])

    def execucao(self, Web:Web, ControleModelo: ControleModelo, ControleView: ControleView,arquivo = Arquivo(nome='', caminho='',conteudo='')) -> None:
        for nome in ControleModelo.get_localizacao_link_comando():
            ControleView.logForScraping(list(('webScrapingNomePrincipal',nome)))
            for link in ControleModelo.get_localizacao_link_comando()[nome]:
                ControleView.logForScraping(list(('webScrapingLink', link)))
                Web.open_link(link=link)
                for comando in ControleModelo.get_localizacao_link_comando()[nome][link]:
                    ControleView.logForScraping(list(('webScrapingComando', comando)))
                    links = Web.clickElementoPorComando(comand=comando)
                    if type(links) == list:
                        for link in links:
                            if '.pdf' in link:
                                ControleView.logForScraping(list(('webScrapingDownload', link)))
                                ControleModelo.add_list_download(Arquivo=Arquivo(nome=nome, caminho=ControleModelo.get_caminho_relacoes()['projeto_pedagogico'], conteudo=link))
                                ControleModelo.download_list()
                                break