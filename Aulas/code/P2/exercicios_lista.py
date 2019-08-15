# 1 -------------------------------------------------------------
l_signos = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']
l_aniversario = ['05/03/1971', '08/06/1998', '31/07/2002', '07/11/1970']

def DefineSigno(aniv, sign):
    for el in aniv:
        ano = int(el[-4:])
        s = ano%12

        print(sign[s])
    return
        

# 2 -------------------------------------------------------------
def MegaSena(res, l):
    for el in l:
        cont = 0
        for n in res:
            if n in el[1]:
                cont += 1

        if cont == 6:
            print("CPF do ganhador: %s" % el[0])

    return
'''
apostas = [['02192392745', [1,2,3,4,5,6]], ['13815645778', [1,2,3,8,5,6]], ['01396093770', [1,2,3,4,5,6]]]
MegaSena([1,2,3,4,5,6], apostas)
'''
# 3 -------------------------------------------------------------
def traduzir(l):
    s_ordem = ' abcdefghijklmnopqrstuvwxyz'
    mens = ''
    
    for el in l:
        mens += s_ordem[el]

    return mens

'''
print(traduzir([2, 15, 13, 0, 4, 9, 1]))
'''
# 4 -------------------------------------------------------------
def UltFrente(l):
    tam = len(l)
    med = tam//2

    fre = l[:med]
    tra = l[med:]

    return tra + fre

'''
print(UltFrente(['a', 'b', 'c', 'd', 'e', 'f']))
'''

# 5 -------------------------------------------------------------
def ListaOrdenada(l):
    ordn = l
    ordn.sort()
    
    cont = 0
    ig = 0

    for i in range(len(l)):
        if type(l[i]) is list:
            ListaOrdenada(l[i])
            
        elif type(l[i]) == type(ordn[i]):
            cont += 1
            if l[i] == ordn[i]:
                ig += 1

        else:
            cont += 1

    return cont == ig
            
print(ListaOrdenada(['a', 'b', 'c', 'd', 'e']))
print(ListaOrdenada(['a', 'b', 'c', 'd', 'a']))


