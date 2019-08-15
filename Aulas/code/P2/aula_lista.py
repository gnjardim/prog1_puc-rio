import random

# a ---------------------------------------------
def produto(l):
    mult = 1
    for el in l:
        if type(el) is list:
            mult *= produto(el)
        else:
            mult *= el     

    return mult

# b ---------------------------------------------
def soma(l):
    sm = 0
    for el in l:
        if type(el) is list:
            sm += soma(el)
        else:
            sm += el     

    return sm      

def conta(l):
    c = 0
    for el in l:
        if type(el) is int:
            c += 1

        else:
            tot = conta(el)
            c += tot

    return c

def media(l):
    sm = soma(l)
    cont = conta(l)
    
    return (sm/cont)

# c ---------------------------------------------
def maior(l):
    m = -41
    
    for el in l:
        if type(el) is list:
            mai = maior(el)
            if mai > m:
                m = mai
            
        elif el > m:
            m = el
            
    return m

# d ---------------------------------------------
def subMult(l):
    for i in range(len(l)):
        if type(l[i]) is list:
            subMult(l[i])
            
        else:
            if l[i]%4 == 0:
                l[i] = 0

    return 

# forma mais eficiente
def subMultV2(l):
    for (i, el) in enumerate(l):
        if type(el) is list:
            subMult(el)
            
        else:
            if el%4 == 0:
                l[i] = 0

    return 


lgrande = random.sample(range(-20, 20), 14)
lgrande[0] = random.sample(range(-10, 10), 3)
lgrande[4] = random.sample(range(100), 2)
lgrande[12] = random.sample(range(-40, 16), 4)

