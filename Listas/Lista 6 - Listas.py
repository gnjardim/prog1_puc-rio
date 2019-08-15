# 1 ------------------------------------------------------
def Limites(l, inf, sup):
    res = list()
    for el in l:
        if type(el) is list:
            res += Limites(el)

        elif type(el) is int or type(el) is float:
            if el >= inf and el <= sup:
                res.append(el)

    return res

l_in = [12,14,15,16,18,20,24,26,28,32,34,38]

sub_l = Limites(l_in, 13, 26)
print(sub_l)

# 2 ------------------------------------------------------
def InvertMetade(l):
    tam = len(l)
    metad = tam//2

    f = l[:metad]
    t = l[metad:]

    return t+f

l_test = ['a','b','c','d','e','f']

n_lista = InvertMetade(l_test)
print(n_lista)

# 3 ------------------------------------------------------
def MediaTurma(lista):
    tot = 0
    cont = 0
    
    for el in lista:
        tot += el[1]
        cont += 1

    media = tot/cont
    return media

def Conta_Baixinhos(lista, media):
    baix = 0
    for el in lista:
        if el[0] > 13 and el[1] < media:
            baix += 1

    return baix

def Alt_Alunos(l):
    med = MediaTurma(l)

    baixinhos = Conta_Baixinhos(l, med)
    print("Número de alunos com mais de 13 anos abaixo da média de altura da turma: %d" % baixinhos)
    
    return
    
l_alunos = [[11,1.6], [12,1.5], [14,1.2], [13,1.7], [10,1.4]]
Alt_Alunos(l_alunos)







    
