from tika import parser #biblioteca usada para extrair os txt dos arquivos PDF`s
import pandas as pd #biblioteca usada para transformar os dados em tabelas no excel
import xlwt #usada para transformas os dados em excel

print('--Minera Texto--\n'      
    '1 - PDF\n'
    '2 - TXT\n'
    '3 - Sair')
opcao = int(input('Digite o formato que deseja minerar o seu texto: '))

def OrgTexto(texto): #metodo para organizar o texto
    for i, palavras in enumerate(texto): #laco de repeticao para percorrer o texto
        texto[i] = palavras[0].split() #utilizei o metodo .split() para separar as palavras

        # tirando possiveis caracteres que possam atrapalhar na busca das palavras
        lista_separados = ['.', ',', ':', '"', '?', '!', '@', '#', '$', '%', '^', '&', '*', ';', '(', ')', '|', '/',
                               '–', '-', '_', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        #percorrendo o texto e removendo cacarteres indesejaveis
        trans = {ord(a): '' for a in lista_separados}
        texto[i] = [j.translate(trans) for a in texto for j in a]

        termos = [] #lista para guardar os termos (palavras)
        numeros = [] #lista para guardar a quantidade em que os termos aparecem
        for c in texto[i]:  # procedimento para percorrer o texto e mostrar uma unica vez cada palavra e a sua quantidade
            if c not in termos:
                if len(c) != 1 and len(c) != 2: #removendo vogais e consoantes que estejam sozinhas ex: 'a' frase 'e' 'a' seguinte
                    a = texto[i].count(c)
                    termos.append(c)
                    numeros.append(a)
                    print(c, '=', a)

        print(len(termos))
        dados = pd.DataFrame(data=numeros, index=termos) #utilizando a biblioteca pandas para transformar os dados em tabelas.
        dados.to_excel('dados-tcc_txt.xls') #arquivo xls com os dados

        return dados

if opcao == 1: #extraindo o arquivo txt do pdf
    print('exemplo: C:/Users/User/Documents/texto-tcc.pdf')
    pdf = input('Digite o caminho do arquivo em seu computador: ')

    print('Carregando..')
    arquivo = parser.from_file(pdf) #formato usado para abrir arquivos PDF`s e extrair o txt
    arquivo = arquivo['content'].lower() #retorna o arquivo em letras minusculas para facilitar na mineracao

    txt = [[arquivo]] #nesse momento eu passo o arquivo como lista.
    a = OrgTexto(txt) #chamando o metodo OrgTexto e passando o texto
    print(a)

elif opcao == 2: #caso o usuario forneca o arquivo em txt
    print('exemplo: C:/Users/User/Documents/ArquivosMachineLearning/Abreu.txt')
    arquivo = input('Digite o caminho do arquivo em seu computador: ')
    print('Carregando...')

    arquivo_txt = open(arquivo, 'r', encoding="utf8") #formato usado para abrir arquivos txt
    txt = arquivo_txt.read().lower() #retorna o arquivo em letras minusculas para facilitar na mineracao
    texto_txt = [[txt]]  #nesse momento eu passo o arquivo como lista.
    a = OrgTexto(texto_txt) #chamando o metodo OrgTexto e passando o texto
    print(a)
