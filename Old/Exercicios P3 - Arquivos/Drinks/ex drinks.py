def le_dados_drinks():
    ldrinks=list()
    arq=open('drinks.txt','r')
    for linha in arq:
        lista=linha.split(' ')
        cod=int(lista[0])
        qtd=int(lista[1])
        sublista=[0]*6
        i=0
        while i<qtd:
            pos=i+1
            posSub=int(lista[pos*2])-1
            sublista[posSub]=float(lista[pos*2+1])
            i+=1
        ldrinks.append([cod,sublista])
    arq.close()
    return ldrinks
