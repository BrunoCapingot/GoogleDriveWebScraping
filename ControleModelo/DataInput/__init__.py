
class Caminho:

    def get_caminho_relacoes(self):
        pass

    def get_localizacao_link_comando(self):
        pass

    def get_complete_dict(self):
        pass

class DataInput(Caminho):

    def get_complete_dict(self):
        complete_dict = dict(caminhos_de_relacao=self.get_caminho_relacoes().copy())
        complete_dict.update(dict(localização_nome_link_comando=self.get_localizacao_link_comando()))
        return complete_dict

    def get_caminho_relacoes(self):
        return dict(
            substitutions=dict({'OPT -': 'OPT-', 'ATC ': 'ATC', 'GAM -': 'GAM-', 'EAL -': 'EAL-', 'ZOO -': 'ZOO-','ENG -': 'ENG-', 'EXA -': 'EXA-', 'AGR -': 'AGR-', 'AGR-218-': 'AGR-218 -','AGR-226 - \n': 'AGR-226 - ', 'AGR- ': 'AGR-', 'HUM -': 'HUM-','Manejo e Conservação do Solo e da \n': 'Manejo e Conservação do Solo e da ','Plantas e Receituário \n': 'Plantas e Receituário ','AGR-222 Avaliação e Perícia Rural': '9º AGR-222 Avaliação e Perícia Rural','Café e \n': 'Café e ', 'Al-\n': 'Al', 'Bacharelado  \n': '', 'AGRONOMIA  \n': '','das unidades \ncurriculares': 'das unidades curriculares','estágio curri-\n': 'estágio curri', '(Milho, Arroz, Trigo e \n': '(Milho, Arroz, Trigo e ','BIBLIOGRA FIA BÁSICA': 'BIBLIOGRAFIA BÁSICA', 'BIBLIOGRAF IA \n': 'BIBLIOGRAFIA'}),
            texto_bruto=r'C:\Users\CPGT\Desktop\WebScrapingGeral\Projeto\Documentos\Download\TextosBrutos',
            projeto_pedagogico=r'C:\Users\CPGT\Desktop\WebScrapingGeral\Projeto\Documentos\Download\ProjetoPedagogicoCurso',
            ementa=r'C:\Users\CPGT\Desktop\WebScrapingGeral\Projeto\Documentos\Download\Ementas',
            txt_fracionado=r'C:\Users\CPGT\Desktop\WebScrapingGeral\Projeto\Documentos\Download\TextosFracionados',
            csv=r'C:\Users\CPGT\Desktop\WebScrapingGeral\Projeto\Documentos\Download\Csv',
            tokenizacao=r'C:\Users\CPGT\Desktop\WebScrapingGeral\Projeto\Documentos\Download\Tokenizados',
            lemanizacao=r'C:\Users\CPGT\Desktop\WebScrapingGeral\Projeto\Documentos\Download\Lemantizados',
            sumarizacao=r'C:\Users\CPGT\Desktop\WebScrapingGeral\Projeto\Documentos\Download\Sumarizados')


    def get_localizacao_link_comando(self):
        return dict({
            'Bacharelado em Agronomia': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                    '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[1]/div[1]/h2/a',
                    '//*[@id="content-section"]/div/div[1]/ul[2]/li[8]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                )),
            },
            'Bacharelado em Ciência da Computação': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                    '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[2]/div[1]/h2/a',
                    '//*[@id="content-section"]/div/div[1]/ul[2]/li[4]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                )),
            },
            'Bacharelado em Química Industrial': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                    '//*[@id="adminForm"]/div[2]/div[4]/div[1]/h2/a',
                    '//*[@id="content-section"]/div/div[1]/ul[2]/li[3]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                )),
            },
            'Bacharelado em Zootecnia': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                    '//*[@id="adminForm"]/div[2]/div[4]/div[1]/h2/a',
                    '//*[@id="content-section"]/div/div[1]/ul[2]/li[2]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                )),
            },
            'Licenciatura em Pedagogia': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                    '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[5]/div[1]/h2/a',
                    '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div[1]/p[12]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                )),
            },
            'Licenciatura em Química': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                    '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[6]/div[1]/h2/a',
                    '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div[1]/ul[2]/li[2]/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                )),
            },
            'Tecnologia em Alimentos': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                    '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[7]/div[1]/h2/a',
                    '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div[1]/ul[2]/li[6]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb'
                )),
            },
            'Tecnologia em Sistemas para Internet': {
                'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': list((
                    '//*[@id="adminForm"]/div[2]/div[8]/div[1]/h2/a',
                    '//*[@id="content-section"]/div/div[1]/ul[2]/li[6]/strong/a',
                    'pdfDownloadLinkUrl',
                    'finishWeb',
                ))
            },
        },
    )