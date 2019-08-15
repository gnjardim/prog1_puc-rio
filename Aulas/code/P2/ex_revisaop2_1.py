# 1
lista = [2.5,7.5,10,4.0]

def PegaMedia(l):
    soma = 0

    for el in l:
        soma += el
        
    return soma/len(l)

media = PegaMedia(lista)
dist = abs(media - lista[0])

for num in lista[1:]:
    if abs(num - media) < dist:
        dist = abs(num - media)
        mais_prx = num

print("Valor mais próximo da média = %.1f" % mais_prx)
'''

# 2
def ContaPontos(l):
    lista_pontos = list()
    
    for sub_l in l:
        n_esc = sub_l[1]

        n_ouro = sub_l[2].count('o')
        n_prata = sub_l[2].count('p')
        n_bronze = sub_l[2].count('b')
        n_pontos = 5*n_ouro + 3*n_prata + n_bronze

        lista_pontos.append([n_esc,n_pontos])

    return lista_pontos

def busca(l, elem):
    for (i, esc) in enumerate(l):
        if esc[0] == elem:
            return i
 
    return None

def AgregaPontos(l):
    l_pontos = ContaPontos(l)
    agregada = list()
    
    for el in l_pontos:
        pos = busca(agregada, el[0])
 
        if pos == None:
            agregada.append([el[0], el[1]])
 
        else:
            agregada[pos][1] += el[1]

    return agregada
    

lRes=[[1010,'Esc1',['o','o','o','p','p']], [2010,'Esc2',['o','p','b','p','b']], [1020,'Esc1',['b','p']], [1030,'Esc1',['b']],
      [3010,'Esc3',['o','o','o','o','p','o','o']], [2010,'Esc2',['b','b','b']], [3020,'Esc3',['o','o']]]

lRes = list()
aluno = int(input("Número do aluno: "))
while aluno != 0:
    l_med = list()
    escola = input("Escola: ")
    medalha = input("Medalha ganha (o, p, b) ou fim para próximo aluno: ")

    while medalha != 'fim':
        l_med.append(medalha)
        medalha = input("Medalha ganha (o, p, b) ou fim para próximo aluno: ")

    lRes += [[aluno, escola, l_med]]
    
    aluno = int(input("\nNúmero do aluno: "))
    

qd_medal = AgregaPontos(lRes)
mais_p = 0
   
for esc in qd_medal:
    print("%s com %d pontos" % (esc[0], esc[1]))
    
    if esc[1] > mais_p:
        mais_p = esc[1]
        vencedor = esc[0]

print("\nEscola campeã: %s com %d pontos" % (vencedor, mais_p))    
    

        
    
    
