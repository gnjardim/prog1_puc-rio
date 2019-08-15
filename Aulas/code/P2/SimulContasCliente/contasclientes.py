def le_arq_contas():
    arq = open("contas.txt", "r")
    mov = list()

    for linha in arq:
        nome = linha.split("\n")[0]

        contas = arq.readline().split()

        for (pos, el) in enumerate(contas):
            contas[pos] = float(el)

        mov.append([nome, contas])

    arq.close()
    return mov


def busca(l, nome):
    for (i, conta) in enumerate(l):
        if conta[0] == nome:
            return i

    return None


def atualiza_saldos(l):
    arq = open("movimentacoes.txt", "r")
    
    for linha in arq:
        nome = linha.split("\n")[0]

        trans = arq.readline().split()
        conta = int(trans[1])
        
        pos = busca(l, nome)
        
        if trans[0] == "r":
            l[pos][1][conta-1] -= float(trans[2])

        elif trans[0] == "d":
            l[pos][1][conta-1] += float(trans[2])

        else:
            l[pos][1][conta-1] = 0

    arq.close()
    return


def gera_arquivo_atual(l):
    arq = open("atual.txt", "w")

    for conta in l:
        arq.write("%s \n" % conta[0])

        for saldos in conta[1]:
            arq.write("\t %.2f" % saldos)

        arq.write("\n")

    arq.close()
    return


l = le_arq_contas()
atualiza_saldos(l)
gera_arquivo_atual(l)

