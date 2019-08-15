def tabuada(n):
    multi=1
    while multi<=10:
        print('%2dx%2d=%2d'%(multi,n,multi*n))
        multi+=1
    return
    
num=int(input('Qual o numero? ou 0 se quiser parar'))
while num!=0:
    tabuada(num)
    num=int(input('Qual o proximo n? 0 para parar'))
