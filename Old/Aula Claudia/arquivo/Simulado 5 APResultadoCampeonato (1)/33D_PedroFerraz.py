def resultadoJogo(gols1, gols2):
    lRes = [0, 0, 0]
    if gols1 > gols2:
        lRes[0] += 1
    elif gols2 > gols1:
        lRes[1] += 1
    else:
        lRes[2] += 1
    return lRes

def busca(nome, lista):
    for (i, el) in enumerate(lista):
        if el[0] == nome:
            return i
    return 'nao'

def atualizaTabela(tabela, nome, golsP, golsC):
    pos = busca(nome, tabela)
    [v, d, e] = resultadoJogo(golsP, golsC)
    if pos != 'nao':
            tabela[pos][1] += v
            tabela[pos][2] += e
            tabela[pos][3] += d
            tabela[pos][4] += golsP
            tabela[pos][5] += golsC
    else:
        tabela.append([nome, v, e, d, golsP, golsC])
    return tabela

def montaTabela(arqRes):
    tabela = []
    for linha in arqRes:
        linha = linha.strip()
        l = linha.split(" ")
        linha = arqRes.readline()
        linha = linha.strip()
        l += linha.split(" ")
        gols1 = int(l[0])
        nome1 = l[1]
        gols2 = int(l[2])
        nome2 = l[3]
        tabela = atualizaTabela(tabela, nome1, gols1, gols2)
        tabela = atualizaTabela(tabela, nome2, gols2, gols1)
    return tabela

def exibeTabela(tabela):
    print("%-20s%-10s%-10s%-10s%-10s%-10s"%("Time", "V", "E", "D", "GP", "GC"))
    for el in tabela:
        linha = "%-20s"%el[0]
        for i in range(1,6):
            linha += "%-10d"%el[i]
        print(linha)
    return
    
def saldo(tabela):
    maiorSaldo = -1
    melhorTime = ""
    for el in tabela:
        saldo = el[4] - el[5]
        if saldo > maiorSaldo:
            maiorSaldo = saldo
            melhorTime = el[0]
    return melhorTime

def naoEmpataram(tabela):
    naoEmpatou = 0
    for el in tabela:
        if el[2] == 0:
            naoEmpatou += 1
    return naoEmpatou

arqResultados = open("resultados.txt", "r")

tabela = montaTabela(arqResultados)
exibeTabela(tabela)
melhor = saldo(tabela)
naoEmp = naoEmpataram(tabela)
print("\nTime com melhor saldo de gols: %s"%melhor)
print("Numero de times que nao empataram nenhuma vez: %d"%naoEmp)

arqResultados.close()
