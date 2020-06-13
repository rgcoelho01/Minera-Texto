import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
import pandas as pd


print('--Minera Texto--\n'      
    '1 - PDF\n'
    '2 - TXT\n'
    '3 - Sair')
opcao = int(input('Digite o formato que deseja minerar o seu texto: '))


def OrgTexto(texto):
    for i, palavras in enumerate(texto):
        texto[i] = palavras[0].split()

        # tirando possiveis caracteres que possam atrapalhar na busca das palavras
        lista_separados = ['.', ',', ':', '"', '?', '!', '@', '#', '$', '%', '^', '&', '*', ';', '(', ')', '|', '/',
                               '–', '-', '_', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        trans = {ord(a): '' for a in lista_separados}
        texto[i] = [j.translate(trans) for a in texto for j in a]



        termos = []
        numeros = []
        for c in texto[i]:  # procedimento para percorrer o texto e mostrar uma unica vez cada palavra e a sua quantidade
            if c not in termos:
                #if len(c) != 1 and len(c) != 2: #removendo vogais e consoantes que estejam sozinhas ex: 'a' frase 'e' 'a' seguinte
                    a = texto[i].count(c)
                    termos.append(c)
                    numeros.append(a)

        print(len(termos))
        dados = pd.DataFrame(data=numeros, index=termos)
        dados.to_excel('textoTcc_NMinerado.xls')

        return dados

if opcao == 1:
    print('exemplo: C:/Users/User/Documents/texto-tcc.pdf')
    pdf = input('Digite o caminho do arquivo em seu computador: ')

    print('Carregando..')
    def extracao_pdf(texto_pdf): #metodo para extrair o texto do arquivo PDF
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle)
        page_interpreter = PDFPageInterpreter (resource_manager, converter)
        with open(texto_pdf, 'rb') as fh:
            for page in PDFPage.get_pages(fh,
                                        caching=True,
                                        check_extractable=True):
                page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()
            converter.close()
            fake_file_handle.close()

        if text:
            return text.lower() #Deixei todas as letras maiusculas para facilitar na busca

    txt = [[extracao_pdf(pdf)]]
    a = OrgTexto(txt)
    print(a)



elif opcao == 2:
    print('exemplo: C:/Users/User/Documents/ArquivosMachineLearning/Abreu.txt')
    arquivo = input('Digite o caminho do arquivo em seu computador: ')
    print('Carregando...')

    arquivo_txt = open(arquivo, 'r', encoding="utf8")
    txt = arquivo_txt.read().lower()
    texto_txt = [[txt]]
    a = OrgTexto(texto_txt)
    print(a)
