def le_arq_times():
    lTimes = []
    arq = open("times.txt","r")
    for linha in arq:
        time = linha.strip()
        lTimes.append([time,[0,0,0,0,0]])
    arq.close()
    return lTimes

def busca(lista, time):
    tam = len(lista)
    for i in range(tam):
        if lista[i][0]==time:
            return i
    return -1
            
def processa_resultados(lstTimes):
    arq = open("resultados.txt","r")
    for time1 in arq:
        time2 = arq.readline()
        time1 = time1.strip()
        time2 = time2.strip()
        resTime1 = time1.split()
        resTime2 = time2.split()
        pos1 = busca(lstTimes, resTime1[1])
        pos2 = busca(lstTimes, resTime2[1])
        gol1 = int(resTime1[0])
        gol2 = int(resTime2[0])
        lstTimes[pos1][1][3]+=gol1
        lstTimes[pos2][1][3]+=gol2
        lstTimes[pos1][1][4]+=gol2
        lstTimes[pos2][1][4]+=gol1
        if gol1 > gol2:
            lstTimes[pos1][1][0]+=1
            lstTimes[pos2][1][2]+=1
        elif gol2 > gol1:
            lstTimes[pos2][1][0]+=1
            lstTimes[pos1][1][2]+=1
        else:
            lstTimes[pos1][1][1]+=1
            lstTimes[pos2][1][1]+=1
    arq.close()

def exibe_resultados(lstTimes):
    totNemp = 0
    melhorSaldo = -1
    for el in lstTimes:
        print("%15s"%el[0],end='')
        for res in el[1]:
            print("%5d"%res,end='')
        if el[1][1]==0:
            totNemp+=1
        saldoGols = el[1][3]-el[1][4]
        if saldoGols > melhorSaldo:
            melhorSaldo = saldoGols
            melhorTime = el[0]
        print("")
    print("O time %s teve o melhor saldo de gols"%melhorTime)
    print("%d times não empataram"%totNemp)

times = le_arq_times()
processa_resultados(times)
exibe_resultados(times)
