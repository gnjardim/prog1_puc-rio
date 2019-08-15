#Exercicio numero mágico
def numeroMagico():
    n=1000
    cont=0
    while n<=9999:
        n1=n//100
        n2=n%100
        a=n1+n2
        if a**2==n:
            print(n)
            cont+=1
        n+=1
    return cont

tot=numeroMagico()
print('Total de números mágicos: %d'%tot)

#Exercício tabuada
def tabuada(n):
    mult=1
    while mult<=10:
        total=n*mult
        print('%d x %d = %d'%(mult,n,total))
        mult+=1
    return

"""n=1
while n<=10:
    print('\nTabuada do',n)
    tabuada(n)
    n+=1"""

"""num=int(input('Qual o numero?'))
while num!=0:#flag
    print('\nTabuada do',num) #printa strings e inteiros
    tabuada(num)
    print()
    num=int(input('Qual o número? (Escolha 0 se deseja sair)'))"""

#Exercicio frascos de essência

def exibirQuant(f1):
    f2=0
    while inicial-novo>10:
        f1-=10
        f2+=10
        f1-=0.0035*f1
        f2-=0.0012*f2
    return

def qtValida():
    qt=float(input('Quantidade no frasco original?'))
    while (qt<40 or qt>=230):
        print('Qt inválida. Digite um valor entre 40 e 230')
        qt=float(input('Quantidade frasco original'))
    return qt

frasco1=qtValida()



        




