import random

def le_territorios():
    arq = open("territorios.txt", "r")
    lista_t = list()

    for linha in arq:
        terr = linha.split(",")

        lista_t.append([terr[0], int(terr[1])])

    arq.close()
    return lista_t


def le_fronteiras():
    arq = open("fronteiras.txt", "r")
    lista_f = list()
    fronteiras = list()
    
    for linha in arq:
        terr = linha.strip('\n').split(",")

        pais = terr[0]
        fronteiras = terr[1:]

        lista_f.append([pais, fronteiras])
            

    arq.close()
    return lista_f


def buscaTerritorio(territorios, nome_t):
    for (i, el) in enumerate(territorios):
        if el[0] == nome_t:
            return i

    return ''


def lancaDados(n_dados):
    res = list()
    
    for n in range(n_dados):
        res.append(random.randint(1, 6))

    res.sort(reverse = True)
    return res


def ataca(ataque, defesa):
    perd_a = 0
    perd_d = 0

    if len(ataque) > len(defesa):
        batalhas = len(defesa)

    else:
        batalhas = len(ataque)
        
    for jogada in range(batalhas):
        if ataque[jogada] > defesa[jogada]:
            perd_d += 1

        else:
            perd_a += 1

    perdidos = [perd_a, perd_d]
    return perdidos

def numeroDados(exercitos, jog):
    if exercitos <= 4:
        if jog == "a":
            dados = exercitos-1

        else:
            dados = exercitos

    else:
        dados = 3

    return dados

    
def jogo(lt, lf, t1, t2, r1, r2):
    p_ataq = lt[r1]
    p_defs = lt[r2]
    
    dados_ataq = numeroDados(p_ataq[1], "a")
    dados_defs = numeroDados(p_defs[1], "d")

    if dados_defs > dados_ataq:
        dados_defs = dados_ataq

    print("\nSituação (antes do ataque) do território de origem: ", p_ataq)
    print("Situação (antes do ataque) do território de destino: ", p_defs)

    print("\n%s ataca %s com %d dados" % (p_ataq[0], p_defs[0], dados_ataq))
    print("%s se defende com %d dados" % (p_defs[0], dados_defs))

    res_ataq = lancaDados(dados_ataq)
    res_defs = lancaDados(dados_defs)

    print("\nDados de ataque: ", res_ataq)
    print("Dados de defesa: ", res_defs)

    mortes = ataca(res_ataq, res_defs)

    lt[r1][1] -= mortes[0]
    lt[r2][1] -= mortes[1]

    if lt[r2][1] == 0:
        print("\n%s conquista %s" % (p_ataq[0], p_defs[0]))
        sob = lt[r1][1]
        lt[r1][1] = sob//2
        lt[r2][1] = sob - lt[r1][1]

    print("\nSituação (depois do ataque) do território de origem: ", lt[r1])
    print("Situação (depois do ataque) do território de destino: ", lt[r2])


    return
            

territ = le_territorios()
front = le_fronteiras()


cont_atq = 0
while cont_atq < 3:
    origem = input("\nDigite o nome do território de origem: ")
    pos_o = buscaTerritorio(territ, origem)
    n_dados = numeroDados(territ[pos_o][1], "a")

    if pos_o == '':
        print("Território não existe")
        
    elif n_dados == 0:
        print("%s possui apenas 1 exército" % territ[pos_o][0])

    else:
        dest = input("Digite o nome do território de destino: ")
        pos_front = buscaTerritorio(front, origem)
        
        if dest in front[pos_front][1]:
            pos_dest = buscaTerritorio(territ, dest)
            jogo(territ, front, origem, dest, pos_o, pos_dest)

        else:
            print("Destino não tem fronteira")

    print("--------------------------------------------------------")    
    cont_atq += 1

print("\nJogada concluída")
