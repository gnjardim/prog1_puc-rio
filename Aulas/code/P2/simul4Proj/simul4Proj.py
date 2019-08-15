def le_dados_previstos():
    prev = list()
    arq = open("prev.txt", "r")

    for linha in arq:
        lfunc = linha.split()

        matr = int(lfunc[0])
        lproj = lfunc[1:]

        for (pos, proj) in enumerate(lproj):
            lproj[pos] = int(proj)

        prev.append([matr,lproj])

    arq.close()
    return prev


def gera_saida_arquivo(lfunc):
    arq = open("real.txt", "w")

    for func in lfunc:
        cont = 0
        arq.write("%d " % func[0])

        for p in func[1]:
            arq.write("%d " % p)

            if p == 0:
                cont += 1

        arq.write("\n")
        
        if cont == len(func[1]):
            print("funcionarios com previsão correta: %d" % func[0])            

    arq.close()
    return


def busca(el, lista):
    for (pos, f) in enumerate(lista):
        if f[0] == el:
            return pos

    return None


def processa(l):
    arq = open("mov.txt", "r")

    for linha in arq:
        lf = linha.split()

        matr  = int(lf[0])
        proj  = int(lf[1])
        horas = int(lf[3])

        pos = busca(matr, l)

        l[pos][1][proj-1] -= horas

    arq.close()
    return
            
			
l = le_dados_previstos()
processa(l)
gera_saida_arquivo(l)


