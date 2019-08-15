
import random
l1=random.sample(range(0,50,7))
l2=random.sample(range(0,50,10))

def intersecao(l1,l2):
    l=[]
    for el in l1:
        if el in l2:
            l.append(el)
    return l
def uniao(l1.l2):
    l=[]
    l.extend(l1)
    for el in l2:
        if el not in l:
            l.append(el)
    return l 
