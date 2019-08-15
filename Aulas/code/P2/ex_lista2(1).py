# 1
'''
n = 0
lista_n = list()
while n < 6:
    nome = input("Nome %d: " % (n+1))
    lista_n.append(nome)

    n += 1


nom_i = input("\nLeia nomes: ")
while nom_i != "fim":
    if nom_i in lista_n:
        ind = lista_n.index(nom_i)
        lista_n[ind] = nom_i.upper()

    else:
        lista_n.append(nom_i)

    print(lista_n)
    nom_i = input("\nLeia nomes: ")
'''

# 2
'''
def busca(l, elem):
    for (i, time) in enumerate(l):
        if time[0] == elem:
            return i

    return None


l_jogos = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7, 8]]]

tot_faltas = 0
nova = list()

for jogo in l_jogos:
    tot_faltas += jogo[-1][0] + jogo[-1][1]

    for i in range(2):
        pos = busca(nova, jogo[i])

        if pos == None:
            nova.append([jogo[i], jogo[-1][i]])

        else:
            nova[pos][1] += jogo[-1][i]

print("Total de faltas: %d" % tot_faltas)


posMenos = 0
posMais = 0

for (pos, time) in enumerate(nova):
    if time[1] < nova[posMenos][1]:
        posMenos = pos

    if time[1] > nova[posMais][1]:
        posMais = pos

print("O time com menos faltas é: ", nova[posMenos][0])
print("O time com mais faltas é: ", nova[posMais][0])
'''

# 5
lista_al = [ ['ana','f'],['pedro','m'],['carla','f'],['carlos','m']]

def HotelAlunos(l):
    cont_f = 0
    cont_m = 0
    
    for el in l:
        if el[1] == 'm':
            cont_m += 1

        else:
            cont_f += 1

    if cont_m > cont_f:
        hotel = "Hotel do Sport"

    elif cont_f > cont_m:
        hotel = "Pink Hotel"

    else:
        hotel = "Le Hotel"

    return hotel

# 6
def classificaDBO(v_dbo, l_class):
    pos = int(v_dbo)

    if pos > 4:
        pos = 4
    return l_class[pos]

def buscaMaior(l):
    maior = -1

    for el in l:
        if type(el) is list:
            maior_el = buscaMaior(el)
            if maior_el > maior:
                maior = maior_el

        elif el > maior:
            maior = el

    return maior

def piorClassificacao(l):
    maior_valor = buscaMaior(l)

    l_classif = ['Muito limpo', 'Limpo', 'Razoável', 'Ruim', 'Péssimo']
    class_dbo = classificaDBO(maior_valor, l_classif)
    
    return class_dbo

def classificaRios(l):
    l_rios = list()
    
    for el in l:
        n_rio = el[0]
        class_dbo = piorClassificacao(el[1])

        l_rios.append([n_rio, class_dbo])

    return l_rios

lDBO = [['Rio AMAZONAS', [3.9, [2.7,2.3, 2.3, 5.6],1.0,[2.0,2.0], 2.0]],
     	['Rio URUGUAI', [[1.9, 1.8], 1.8, 0.3, 1.6, [1.0, 2.0, 1.9, 2.0]]],
        ['Rio TIETE', [3.9, [2.7, 3.0, 3.8, 2.3], [1.6, 1.0],[1.0, 2.0], 2.5]],
        ['Rio GUANDU', [4.0, [2.7, 7.8, 2.3, 5.6], [1.0, 9.0], 2.0, 2.0]],
        ['Rio DA PRATA', [0.02, [0.1, 0.1, 0.1], 0.05, 0.09, 0.08]],
        ['Rio MURIAE', [1.8, 1, 0.8, 4.0, 3.0]],
        ['Rio NEGRO', [[1.9, 1.8], 1.8, 0.3, 1.6, [1.0, 1.8, 1.9, 1.9]]]]


res_dbo = classificaRios(lDBO)
print(res_dbo)

