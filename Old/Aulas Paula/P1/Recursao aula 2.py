#Exercicio de recursao em sala

#2
def algarismo2opcao1(n):
    if n<10: #caso base
        if n==2:
            return 1
        else:
            return 0
    ult=n%10 #diminuir o problema
    if ult==2:
        cont=1
    else:
        cont=0
    return cont + algarismo2(n//10)

def algarismo2opcao2(n):
    if n<10: #caso base
        if n==2:
            return 1
        else:
            return 0
    elif n%10==2:
        return 1+algarismos2(n//10)
    else:
        return algarismo2(n//10)
    
#3
def algarismoX(n,x):
    if n<10:
        if n==x:
            return 1
        else:
            return 0
    elif n%10==x:
        return 1+algarismoX(n//10,x)
    else:
        return algarismoX(n//10,x)

#4
def verifica2(n):
    if n<10:
        if n==2:
            return True
        else:
            return False
    ult=n%10
    if ult==2:
        return True
    return verifica2(n//10)
