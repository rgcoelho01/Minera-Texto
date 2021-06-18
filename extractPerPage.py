import pdfplumber #nova biblioteca
import pontuacoes #nesse arquivo contém um replace para remover as pontuacoes
with pdfplumber.open("C:/Users/User/Documents/Tcc/projetoTccPatente3.pdf") as pdf: #estou utilizando essa biblioteca para extrair o texto dos pdfs
    totalPages = len(pdf.pages)

    i = 0;
    reivindicacoes = []
    resumo = []
    paginaReivindicacao = 0;
    paginaResumo = 0;
    while i < totalPages:
        first_page = pdf.pages[i]
        conteudo = first_page.extract_text()
        texto = [[conteudo]]
        for token in texto:
            for words in token:
                word = pontuacoes.filtro(words)
                conteudo = [[word]]
                for textoFiltrado in conteudo:
                    for textoSplitado in textoFiltrado:
                        alo = textoSplitado.split(" ")
                        print(range(len(alo)))
                        for busca in alo:
                            print(busca)
                            if (busca == "REIVINDICAÇÕES" or busca == "REIVINDICAÇÃO"):
                                reivindicacoes.append(alo)
                                paginaReivindicacao = i
                            if (busca == "RESUMO" or busca == 'Resumo'):
                                print('encontrei')
                                resumo.append(alo)
                                paginaResumo = i
        print('----------------------acabou--------------------------')
        i+=1
        print('Reivindicação: ',reivindicacoes)
        print('Resumo: ', resumo)
        print('pagina reivindicação', paginaReivindicacao)
        print('pagina resumo', paginaResumo)
