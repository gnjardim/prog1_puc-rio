def le_arq_times():
    arq=open('times.txt','r')
    ltimes=list()
    for linha in arq:
        nome=linha.strip()
        lres=[0]*5 # V, E, D, GP, GC
        ltimes.append([nome,lres])
    arq.close()
    return ltimes

def busca_time(time,lista):
    for (i,el) in enumerate(lista):
        if el[0]==time:
            return i
    return -1

def atualiza_resultados(ltimes):
    latual=ltimes.copy()
    arq=open('resultados.txt','r')
    for linha in arq:
        ltime1=linha.strip().split(' ')
        gols1=int(ltime1[0])
        time1=ltime1[1]
        ltime2=arq.readline().strip().split(' ')
        gols2=int(ltime2[0])
        time2=ltime2[1]
        posT1=busca_time(time1,ltimes) #pos do time 1
        posT2=busca_time(time2,ltimes) #pos do time 2
        ltimes[posT1][1][-2]+=gols1
        ltimes[posT1][1][-1]+=gols2
        ltimes[posT2][1][-2]+=gols2
        ltimes[posT2][1][-1]+=gols1
        if gols1>gols2:
            ltimes[posT1][1][0]+=1
            ltimes[posT2][1][2]+=1
        elif gols2>gols1:
            ltimes[posT2][1][0]+=1
            ltimes[posT1][1][2]+=1
        else:
            ltimes[posT1][1][1]+=1
            ltimes[posT2][1][1]+=1
    arq.close()
    return ltimes

def exiba_resultados(latual):
    arq=open('tabela_final.txt','w')
    maior=-1
    for (i,time) in enumerate(latual):
        saldo=time[1][-2]-time[1][-1]
        if saldo>maior:
            maior=saldo
            pos=i #encontra a posicao do time de maior saldo de gols
        conta=0
        if time[1][1]==0:
            conta+=1
        arq.write('%-20s'%time[0])
        for (i,n) in enumerate(time[1]):
            arq.write('%-5d'%time[1][i])
        arq.write('\n')
    arq.close()
    print('Time com melhor saldo de gols: %s'%ltimes[pos][0])
    print('Numero de times que nao emparataram nenhuma vez: %d'%conta)
    return

ltimes=le_arq_times()
latual=atualiza_resultados(ltimes)
exiba_resultados(latual)


