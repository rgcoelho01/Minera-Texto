
import pdfplumber
import pontuacoes
with pdfplumber.open("C:/Users/User/Documents/Tcc/projetoTccPatente2.pdf") as pdf: #estou utilizando essa biblioteca para extrair o texto dos pdfs
    totalPages = len(pdf.pages)

    i = 0
    reivindicacoes = []
    resumo = []
    paginaReivindicacao = 0
    pageReivi = 0
    pageResumo = 0
    paginaResumo = 0
    while i < totalPages:
        first_page = pdf.pages[i]
        conteudo = first_page.extract_text().lower()
        texto = [[conteudo]]
        lista = []
        for token in texto:
            for words in token:
                word = pontuacoes.filtro(words)
                conteudo = [[word]]
                for textoFiltrado in conteudo:
                    # print(textoFiltrado)
                    for textoSplitado in textoFiltrado:
                        alo = textoSplitado.split(" ")
                        # print(alo)
                        for busca in alo:
                            if(busca != ''):
                                lista.append(busca)
        print(lista, 'alo')
        for alo in lista:
            if(lista[0] == "reivindicações" or lista[0] == "reivindicação"):
                reivindicacoes.append(alo)
                pageReivi = i
            else
            if(lista[0] == "resumo"):
                resumo.append(alo)
                pageResumo = i

            if(pageReivi != 0):
                if(lista[0] != "resumo"):
                    reivindicacoes.append(alo)

            if(pageResumo != 0):
                if(pageResumo < i):
                    resumo.append(alo)
        i+= 1
        
    print('pageReivi', pageReivi, 'page resumo', pageResumo)
    print('Reivindicação: ',reivindicacoes)
    print('Resumo: ', resumo)
