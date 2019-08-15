import random
l1=[3,7,1,90,2]
l2=[3,[98,2,1],10]

def exibirElementos(lista):
    for i in lista:
        print(i)
    return

"""def exibirElementos2(lista):
    for i in range(len(lista)):
        print(lista[i])
    return"""

#gera uma lista onde cada valor é uma lista composta pela posição do valor da lista original e o valor

def exibirElementos3(lista):
    for (i,el) in enumerate(lista):
        print(el)
    return

def somaElementos(lista):
    soma=0
    for i in lista:
        tipo=type(i) #para não chamar a função type mais de uma vez
        if tipo==int or tipo==float:
            soma+=i
        elif tipo==lista: #despreza se o elemento i for uma string
            soma+=somaElementos(i)
    return soma

#exercicio
lgrande=random.sample(range(-20,20),14)
lgrande[0]=random.sample(range(-10,10),3)
lgrande[4]=random.sample(range(100),2)
lgrande[12]=random.sample(range(-20,16),4)

def produtoLista(lista):
    produto=1
    for el in lista:
        if type(el)==int:
            produto*=el
        else:
            produto=produtoLista(el)
    return produto

def contaElementos(lista):
    cont=0
    for el in lista:
        if type(el)==int:
            cont+=1
        else:
            cont+=contaElementos(el)
    return cont

def mediaLista(l):
    s=somaElementos(l)
    c=contaElementos(l)
    return s/c

def maiorValor(lista):
    maior=-41
    for el in lista:
        if type(el)==int:
            if el>maior:
                maior=el
        else:
            submaior=maiorValor(el)
            if submaior>maior:
                maior=submaior
    return maior

def substituir(lista):
    for i in range(len(lista)):
        if type(lista[i])==int:
            if lista[i]%4==0:
                lista[i]=0
        else:
            substituir(lista[i])
    return

#solução paula:

def subst(l):
    for (i,el) in enumerate(l):
        if type(el)==int:
            if el%4==0:
                l[i]=0
        else:
            subst(el)
    return

def localiza(l,n):
    for el in l:
        if type(el)==int:
            if el==n:
                return True
        else:
            r=localiza(el,n)
            if r:
                return True #se for falso a função checa o proximo elemento
    return False


