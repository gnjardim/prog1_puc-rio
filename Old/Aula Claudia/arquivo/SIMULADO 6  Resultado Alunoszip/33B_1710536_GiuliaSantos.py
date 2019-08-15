def busca(lista,c):
    for (i,el) in enumerate(lista):
        if el[0]==c:
            return i
    return "não tem"

def le_arq_disc():
    disc=open("disciplinas.txt","r")
    ldisc=[]
    for linha in disc:
        l=linha.strip().split(" ")
        ldisc.append(l+[[0,0,0,0]])
    disc.close()
    return ldisc

def atualiza_resultados(ldisc):
    rst=open("resultados.txt","r")
    for linha in rst:
        linha=linha.strip()
        qt=int(linha[-1])
        n=1
        while n<=qt:
            linha2=rst.readline()
            l2=linha2.strip().split(",")
            disciplina=l2[0]
            tipo=int(l2[1])
            i=busca(ldisc,disciplina)
            if i!="não tem":
                ldisc[i][2][tipo-1]+=1
            n+=1
    rst.close()
    return ldisc

def descobre_pos_maior(ldisc):
    ltipo=["AP","RM","RF","TR"]
    maior=-1
    for (i,el) in enumerate(ldisc):
        for (ii,ele) in enumerate(el[2]):
            if ele>maior:
                maior=ele
                imaior=i
                iimaior=ii
    l=ldisc[imaior]
    print("%s de %s créditos tem %d alunos %s"%(l[0],l[1],l[2][iimaior],ltipo[iimaior]))

def gera_arquivo_atual(ldisc):
    atual=open("atual.txt","w")
    atual.write("Disciplina   AP  RM  RF  TR\n")
    for el in ldisc:
        atual.write("%-11s"%el[0])
        for ele in el[2]:
            atual.write("%4d"%ele)
        atual.write("\n")
    atual.close()


ldisc=le_arq_disc()
ldisc=atualiza_resultados(ldisc)
gera_arquivo_atual(ldisc)
descobre_pos_maior(ldisc)
                
                            
