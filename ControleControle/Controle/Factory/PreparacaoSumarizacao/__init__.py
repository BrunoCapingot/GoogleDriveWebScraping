from Projeto.ControleModelo import ControleModelo
from Projeto.ControleModelo.Arquivo import Arquivo
from Projeto.ControleControle.Controle.ControleProcessos.Processo import Processo
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer


class PreparacaoSumarizacao(Processo):
    def executar(self,ControleModelo: ControleModelo, sentences_count=3):
        ControleModelo.set_model_data(type_model='caminhos_de_relacao',key_dict='tokenizacao')
        parser = PlaintextParser.from_string(ControleModelo.get_conteudo_do_arquivo(type_arq='txt',Arquivo=Arquivo(nome='',caminho='',conteudo='')), Tokenizer("portuguese"))
        summarizer = TextRankSummarizer()
        summary = summarizer(parser.document, sentences_count)
        return " ".join([str(sentence) for sentence in summary])