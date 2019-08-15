#Lista revisao p2 claudia

#Repeticao
#A
def valor_carne(produto,qtd):
    if qtd<=10:
        if produto=='Picanha':
            preco=25
        else:
            preco=30
    else:
        if produto=='File Mignon':
            preco=15
        elif produto=='Picanha':
            preco=12
        else:
            preco=8
    return preco*qtd
    
def valor_total():
    produto=input('Produto:')
    totalF=0
    totalP=0
    totalA=0
    while produto!='':
        if produto=='File Mignon':
            totalF+=1
        elif produto=='Picanha':
            totalP+=1
        else:
            totalA+=1
        produto=input('Produto:')
    valorF=valor_carne('File Mignon',totalF)
    valorP=valor_carne('Picanha',totalP)
    valorA=valor_carne('Alcatra',totalA)
    total=valorF+valorP+valorA
    print('Total a ser pago: R$%.2f'%total)
    return total

def exibir_troco(total):
    tipo=input('Tipo de pagamento?')
    if tipo=='c':
        print('Nao ha troco')
        return
    if tipo=='d':
        valPago=int(input('Valor entregue:'))
    else:
        qtd=int(input('Quantos tickets?'))
        valPago=0
        for i in range(qtd):
            valor=int(input('Valor do ticket?'))
            valPago+=valor
    troco=valPago-total
    if troco==0:
        print('Nao ha troco')
    else:
        print('Troco: R$%.2f'%troco)
    return

#Lista

#A

#B
# nome - sexo - idade

def tem_nova_turma(lista):
    numMasc=0
    numFem=0
    listaMasc=list()
    listaFem=list()
    for el in lista:
        if el[2]<14:
            print('Nao eh possivel formar uma nova turma')
            return
        if el[1]=='f':
            numFem+=1
            listaFem.append(el[0])
        else:
            numMasc+=1
            listaMasc.append(el[0])
    if numFem<3 or numMasc<3:
        print('Nao eh possivel formar uma nova turma')
        return
    print('Eh possivel formar uma nova turma')
    if len(listaFem)>len(listaMasc):
        tam=len(listaMasc)
    else:
        tam=len(listaMasc)
    for i in range(tam):
        print('Casal %d: %s e %s'%(i+1,listaFem[i],listaMasc[i]))
    return

inscritos=[['Joyce','f',50],['Jorge','m',15],['Mariana','f',30],['Luis','m',40],['Maria','f',20],['Jose','m',70]]

#C
"""def contaUmaEscola(lEscola):
    numF=0
    numM=0
    for el in lEscola:
        if type(el)==str:
            if el=='f':
                numF+=1
            else:
                numM+=1
        else:
            aux=contaUmaEscola(el)
            numF+=aux[0]
            numM+=aux[1]
    novaL=[numF,numM]
    return novaL

def determinaHotel(redeEscolas):
    total=[0,0]
    for el in redeEscolas:
        qtd=contaUmaEscola(el)
        total[0]+=qtd[0]
        total[1]+=qtd[1]
    if total[0]>total[1]:
        hotel='Machistas nao passarao'
    elif total[0]<total[1]:
        hotel='Menina tbm faz esporte'
    else:
        hotel='Le Hotel'
    print(hotel)
    return

LEscolas=[[[['f','m'],['f','m','m']],['f','m','f','f']],['f','f','m','m']]
determinaHotel(LEscolas)"""

#D
def calcule_midrange(l):
    vmin=l[0]
    vmax=l[0]
    for el in l:
        if el>vmax:
            vmax=el
        elif el<vmin:
            vmin=el
    return (vmax+vmin)/2

#E
#entre 15/05 e 10/06
def verificaData(data):
    dia=int(data[0:2])
    mes=int(data[-2:])
    if mes<5 or mes>6:
        return False
    if mes==5:
        if dia<15:
            return False
    elif mes==6:
        if dia>10:
            return False
    return True

def dataValida():
    data=input('Data da prova?')
    while verificaData(data)==False:
        data=input('Data inválida. Favor digitar data válida')
    return data

def montaDataProvas():
    lProvas=list()
    codigo=input('Código da matéria?')
    while codigo!='':
        data=dataValida()
        dia=int(data[0:2])
        mes=int(data[-2:])
        lProvas.append([[mes,dia],codigo])
        codigo=input('Código da matéria?')
    print(lProvas)
    return lProvas

"""def montaCalendario(ldatas):
    matr=input('Digite sua matrícula')
    nome=input('Digite seu nome')
    num=int(input('Número de disciplinas?'))"""
    
    
    


    




            
        
        
