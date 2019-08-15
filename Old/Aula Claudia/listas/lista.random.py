import random
lgrade=random.sample(range(-20,20),14)
lgrade[0]=random.sample(range(-10.10),3)
lgrade[4]=random.sample(range(-20,20),14)
lgrade[12]e=random.sample(range(-20,20),14)
print(lgrade)

def mediaLista(l):
    soma=0
    for el in l :
        if type(el)==list:
            soma+=mediaLista(el)
        else:
            soma+=el
    return soma/len(l)
def maiorLista(l):
    maior=None
    for el in (l):
        if type(el)==list:
            maiorsl=maiorLista(el)
        else:
            maiorsl=el
        if maior==None:
            maior=maiorsl
        elif maiorsl>maior:
            maior=maiorsl
        return maior
def pertenceLista(l,val):
    for el in l:
        if type(el)==list:
            sit=pertenceLista(el,vai)
            if sit==True:
                return True
        elif el==vai:
            return True
    return False
        
