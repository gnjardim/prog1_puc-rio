l1=[3,7,1,90,2]
l2=[3,[98,2,2,1],10]

'''def soma(l):
    tot=0
    for el in l:
        tot+=el
    return tot

print('soma dos valores L1: %d'%(soma(l1)))
print('soma dos valores L2: %d'%(soma(l2)))'''

def soma(l):
    tot=0
    for el in l:
        tipo=type(el)
        if tipo==int or tipo==float:
            tot+=el
        elif tipo==list:
            tot+=soma(el)
            
    return tot
print('soma dos valores L1: %d'%(soma(l1)))
print('soma dos valores L2: %d'%(soma(l2)))
