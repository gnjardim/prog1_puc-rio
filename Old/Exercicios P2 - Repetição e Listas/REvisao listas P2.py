#Lista de Revisao para P2 (Lista 12 Paula)

"""metodos
lista.append(elemento) - inclui elemento no final da lista
lista.insert(indice,elemento) - inclui elemento antes do indice
lista.extend(sequencia) - adiciona elementos de sequencia no final da lista
del lista[indice] - remove o elemento localizado no indice
del lista[a:b] - remove sublista definida pela fatia
lista.pop(indice) - exclui o elemento do indice da lista e retorna o valor removido
lista.remove(elemento) - exclui primeira instancia do elemento na lista
filter(funcao,lista) - usa a funcao (booleana) e gera uma nova lista com os elementos que gerarem True
map(funcao,lista) - gera uma nova lista composta pelos resultados da funcao aplicada em cada elemento
reduce(funcao,lista)
"""

#2
def obtem_primeiro(lista):
    if type(lista[0])!=list:
        prim=lista[0]
    else:
        prim=obtem_primeiro(lista[0])
    return prim

#2a
def maior_elemento(l):
    maior=obtem_primeiro(l)
    for el in l:
        if type(el)!=list:
            if el>maior:
                maior=el
        else:
            maior_local=maior_elemento(el)
            if maior_local>maior:
                maior=maior_local
    return maior

#2b
def soma_elementos(l):
    total=0
    for el in l:
        if type(el)!=list:
            total+=el
        else:
            total+=soma_elementos(el)
    return total

#2c
def ocorrencias_prim(l):
    prim=obtem_primeiro(l)
    conta=0
    for el in l:
        if type(el)!=list:
            if el==prim:
                conta+=1
        else:
            conta+=ocorrencias_prim(el)
    return conta

#2d
def conta_elementos(l):
    conta=0
    for el in l:
        if type(el)!=list:
            conta+=1
        else:
            conta+=conta_elementos(el)
    return conta

def media_elementos(l):
    total=soma_elementos(l)
    qtd=conta_elementos(l)
    return total/qtd

#2e
def obtem_mais_prox(l,media):
    proximo=obtem_primeiro(l)
    for el in l:
        if type(el)!=list:
            if abs(el-media)<abs(proximo-media):
                proximo=el
        else:
            proximo_local=obtem_mais_prox(el,media)
            if abs(proximo_local-media)<abs(proximo-media):
                proximo=proximo_local
    return proximo

    
def valor_prox_media(l):
    media=media_elementos(l)
    return obtem_mais_prox(l,media)

#2f
def soma_negativos(l):
    soma=0
    for el in l:
        if type(el)!=list:
            if el<0:
                soma+=el
        else:
            soma+=soma_negativos(el)
    return soma

#2g

#2 desafio
def exibir_sublistas(l):
    for el in l:
        if type(el)==list and len(el)==2 and type(el[0])!=list and type(el[1])!=list:
            print(el)
        elif type(el)==list:
            exibir_sublistas(el)
    return

#3a
def listas_iguais(l1,l2):
    for i in range(len(l1)):
        if l1[i]!=l2[i]:
            return False
    return True

"""def listas_iguais(l1,l2):
    if l1==l2:
        return True
    return False"""

#3b
def mesmos_elementos(l1,l2):
    for el in l1:
        if el not in l2:
            return False
    return True

#5a
def maiorCaract(lista):
    maior=''
    for el in lista:
        if type(el)==str:
            if len(el)>len(maior):
                maior=el
        else:
            submaior=maiorCaract(el)
            if len(submaior)>len(maior):
                maior=submaior
    return maior

#5b
def eh_vogal(s):
    if s=='a' or s=='e' or s=='i' or s=='o' or s=='u' or s=='A' or s=='E' or s=='I' or s=='O' or s=='U':
        return True
    return False
    
def conta_vogais(l):
    conta=0
    for el in l:
        if type(el)==str:
            for letra in el:
                if eh_vogal(letra):
                    conta+=1
        else:
            conta+=conta_vogais(el)
    return conta

def media_vogais(l):
    numVogais=conta_vogais(l)
    numElem=conta_elementos(l)
    return numVogais/numElem

#5c) - funciona com a funcao do numero 2b ocorrencias_prim(l)

#5d)
def lexicograf(lista):
    maior=''
    for el in lista:
        if type(el)==str:
            if el>maior:
                maior=el
        else:
            submaior=lexicograf(el)
            if submaior>maior:
                maior=submaior
    return maior

#5e
def eh_composta(s):
    if ' ' in s or '-' in s:
        return True
    return False

def ocorrencias_comp(l):
    conta=0
    for el in l:
        if type(el)==str:
            if eh_composta(el):
                conta+=1
        else:
            conta+=ocorrencias_comp(el)
    return conta

#5f) - tirar duvida

#5 desafio - funciona com exibir_sublistas(l) da 2 desafio

#6)
def traduzir(lSecreta):
    alf=' abcdefghijklmnopqrstuvwxyz'
    l=list() #criar uma lista pq eh mutavel
    for el in lSecreta:
        l.append(alf[el])
    return ''.join(l)

def traduza(l):
    alf=' abcdefghijklmnopqrstuvwxyz'
    for (i,el) in enumerate(l):
        l[i]=alf[el]
    return ''.join(l)

lsecreta=[2,15,13,0,4,9,1]

#7)
def buscar(elem,lista):
    for (pos,valor) in enumerate(lista):
        if valor[0]==elem:
            return pos
    return -1

def obtemFaltaTime(lista):
    novaL=list()
    for el in lista:
        for i in range(2):
            pos=buscar(el[i],novaL)
            if pos!=-1:
                novaL[pos][1]+=el[2][i]
            else:
                novaL.append([el[i],el[2][i]])
    return novaL

def total_faltas(lista):
    total=0
    for el in lista:
        total+=el[1]
    return total
    
jogos=[['Brasil','Italia',[10,9]],['Brasil','Espanha',[5,7]],['Italia','Espanha',[7,8]]]
novaJogos=obtemFaltaTime(jogos)
somaFaltas=novaJogos[0][1]
menorFaltas=novaJogos[0][1]
maisFaltas=novaJogos[0][1]
timeMenos=novaJogos[0][0]
timeMais=novaJogos[0][0]

for el in novaJogos[1:]: #nao precisa comparar com o primeiro de novo
    if el[1]>maisFaltas:
        maisFaltas=el[1]
        timeMais=el[0]
    elif el[1]<menorFaltas:
        menorFaltas=el[1]
        timeMenos=el[0]
    somaFaltas+=el[1]
print('Total de faltas: %d'%somaFaltas)
print('Time com mais faltas: %s'%timeMais)
print('Time com menos faltas: %s'%timeMenos)

#8) - igual ao 2e

#9) - feito pro teste

#10) - ?

#11) - TIRAR DUVIDA
def posicao_valor(lNumeros,valor):
    if not lNumeros:
        return -2
    for (i,el) in enumerate(lNumeros):
        if type(el)!=list:
            if el==valor:
                return i
        else:
            res=posicao_valor(el,valor)
            if res!=-1 or res!=-2
                return i
    return -1

lnum=[4,[8,6],7,5,3,2,-2,1,8]

#12a)
def uniao_listas(l1,l2):
    uniao=l1[:]
    for el in l2:
        if el not in l1:
            uniao.append(el)
    return uniao

#12b)
def intersecao_listas(l1,l2):
    intersecao=[]
    for el in l1:
        if el in l2:
            intersecao.append(el)
    return intersecao

#12c)
def intercala_listas(l1,l2):
    if len(l1)<len(l2):
        tam=len(l1)
        maior=l2[:] #tirar cópia 
    else:
        tam=len(l2)
        maior=l1[:] #tirar cópia
    nova=list()
    for i in range(tam):
        nova.append(l1[i])
        nova.append(l2[i])
    nova.extend(maior[tam:])
    return nova

#13)
def nota_nova(nota,maiorNota):
    return nota*10/maiorNota

def exibir_notas(Lnotas):
    maiorNota=maior_elemento(Lnotas)
    for (i,nota) in enumerate(Lnotas):
        notaNova=nota_nova(nota,maiorNota)
        print('%-5d %-5.1f %-5.1f'%(i+1,nota,notaNova))
    return

listaNotas=[3.0,4.0,5.0,6.0,3.0]

#14)

#15) - feito no teste

#16)

