def le_arq_livros():
    arq = open("livros.txt", "r")
    livros = list()

    for linha in arq:
        liv = linha.split("\n")[0]

        dist = arq.readline().split()

        for (pos, n) in enumerate(dist):
            dist[pos] = int(n)

        livros.append([liv,dist])

    arq.close()
    return livros


def busca(l, livro):
    for (i, el) in enumerate(l):
        if el[0] == livro:
            return i

    return None

    
def atualiza_informacoes(l):
    arq = open("atualizacoes.txt")

    for linha in arq:
        liv = linha.split("\n")[0]

        op = arq.readline().split()

        dist = int(op[0])
        oper = op[1]
        q_liv = int(op[2])

        pos = busca(l, liv)

        if pos == None:
            return

        if oper == "v":
            l[pos][1][dist-1] -= q_liv

        if oper == "r":
            l[pos][1][dist-1] += q_liv

    arq.close()
    return


def gera_relatorio_final(l):
    arq = open("final.txt", "w")
    zer = list()

    for livros in l:
        cont = 0
        arq.write("%s \n" % livros[0])

        for dist in livros[1]:
            arq.write("\t%d " % dist)

            if dist == 0:
                cont += 1

        if cont == len(livros[1]):
            zer.append(livros[0])
            
        arq.write("\n")

    print("Livros com estoque zerado em todas as distribuidoras: ")
    for liv in zer:
        print(liv)

    menor_q = menor_quantidade(l)
    print("\nCódigo da distribuidora com menor quantidade de livros: %d" % menor_q)
    
    arq.close()
    return


def menor_quantidade(l):
    by_dist = list()

    for livro in l:
        for (i, el) in enumerate(livro[1]):
            if i >= len(by_dist):
                by_dist.append(el)
                
            else:
                by_dist[i] += el

    menor = by_dist[0]
    cod = 1
    for (i, dist) in enumerate(by_dist[1:]):
        if dist < menor:
            menor = dist
            cod = i+2
    
    return cod      


l = le_arq_livros()
atualiza_informacoes(l)
gera_relatorio_final(l)


