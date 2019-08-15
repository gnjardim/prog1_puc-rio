#Recursão

def numDigitos(n):
    if n<10:
        return 1
    return 1+numDigitos(n//10)

"""caso base: 1, se n<10
recursivo: 1+numdigitos(n//10)
n=4317
numero de digitos:
numero de digitos de 4317=1+numero de digitos(431)
numero de digitos(431)= 1 + numero de digitos(43)
numero de digitos de 43=1+numero de digitos(4)
numero de digitos(4)=1 (CASO BASE)"""

#toda vez que a função é chamada uma área da memória é guardada para ela e fica
#presa até que consiga concluir sua tarefa

tot=numDigitos(4317)

def exibirVert(n):
    if n<10:
        print(n) #nao botar print ao lado de return pq a função n retorna nenhum valor
        return
    exibirVert(n//10) #separa o numero que precede a unidade
    print(n%10) #exibe a unidade
    return

#ele esibe de 'tras pra frente' pq a exibição do 3 é o primeiro problema que consegue resolver


def exibirVertInv(n):
    if n<10:
        print(n)
        return
    print(n%10)
    exibirVertInv(n//10)
    return


