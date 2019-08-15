def le_arq_contas():
    arq=open('contas.txt','r')
    lcontas=list()
    for linha in arq:
        cliente=linha.strip()
        lsaldos=arq.readline().split(' ')
        for (i,n) in enumerate(lsaldos):
            lsaldos[i]=float(n)
        lcontas.append([cliente,lsaldos])
    arq.close()
    return lcontas

def busca_cliente(nome,lista):
    for (i,el) in enumerate(lista):
        if el[0]==nome:
            return i
    return -1

def atualiza_saldos(lcontas):
    latual=lcontas.copy()
    arq=open('movimentacoes.txt','r')
    for linha in arq:
        cliente=linha.strip()
        loperacao=arq.readline().split(' ')
        posCliente=busca_cliente(cliente,latual)
        if posCliente!=-1:
            posConta=int(loperacao[1])-1
            if loperacao[0]=='r':
                latual[posCliente][1][posConta]-=float(loperacao[2])
            elif loperacao[0]=='d':
                latual[posCliente][1][posConta]+=float(loperacao[2])
            else:
                latual[posCliente][1][posConta]=0.0
    arq.close()
    return latual

def gera_arq_atual(latual):
    arq=open('atual.txt','w')
    for cliente in latual:
        nome=cliente[0]
        lsaldos=cliente[1]
        arq.write(nome+'\n')
        for n in lsaldos:
            arq.write('%.2f\t'%n)
        arq.write('\n')
    arq.close()
    return

lcontas=le_arq_contas()
latual=atualiza_saldos(lcontas)
gera_arq_atual(latual)
