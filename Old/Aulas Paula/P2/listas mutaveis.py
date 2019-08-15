#método .split: cria uma lista com os elementos da string separadas 

def stringMaluca(s):
    l=s.split(' ') #o espaço é o divisor 
    tam=len(l)
    meio=tam//2
    novaL=l[:meio]+[l[meio]]*tam+l[meio+1:]
    return ' '.join(novaL) #inverso do .split

#Exercicio

def posicaoZero(l):
    for (i,el) in enumerate(l): #enumerate gera pares dos indices e seus elementos- primeiro argumento é o indice
        if el==0:
            return i
    return False #se nao tiver zero

def posicaoZeroAlt(l):
    for i in range(len(l)):
        el=l[i]
        if el==0:
            return i
    return False

#método que retorna o indice de um elemento da lista: l.index(el)
    
def concatenaSinal(l1,l2):
    pos0l1=posicaoZero(l1)
    pos0l2=posicaoZero(l2)
    if pos0l1==False or pos0l2==False:
        print('Inexistente')
        return
    novaL=l1[:pos0l1]+l2[:pos0l2]+l1[pos0l1+1:]+l2[pos0l2+1:]
    return novaL
    
#Exercicio pauta

def exibe(l):
    l.sort()
    for nome in l:
        print('%-20s|___|___|___|___|___|'%nome)
    return

lista=[]
nome=input('Nome do aluno?')
while nome!='fim':
    lista=lista+[nome]
    nome=input('Nome do aluno?')
exibe(lista)

