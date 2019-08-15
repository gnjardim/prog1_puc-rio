#1 - tinta
import math

def areaRetangulo(b,a):
    return b*a

def areaCirculo(r):
    return math.pi*r**2

def areaCilindro(r,a):
    base=areaCirculo(r)
    circum=2*math.pi*r
    ret=areaRetangulo(circum,a)
    return 2*base+ret

def quantLatas():
    altura=int(input('altura?'))
    raio=int(input('raio?'))
    qtd=int(input('quantos cilindros?'))
    areaTotal=areaCilindro(raio,altura)*qtd
    tintaTotal=areaTotal/3
    latas=tintaTotal//5
    if tintaTotal//5!=0:
        latas=latas+1
    custo=latas*20
    print('quantidade de latas de tinta: %d'%latas)
    print('preco a pagar: R$%.2f'%custo)
    return

#2 - data do dia seguinte
def anoBissexto(ano):
    if ano%4==0 and (ano%100!=0 or ano%400==0):
        return True
    return False

def mes30(mes):
    if mes==4 or mes==6 or mes==9 or mes==11:
        return True
    return False

def diaSeguinte(data):
    dia=int(data[0:2])
    mes=int(data[3:5])
    ano=int(data[-4:])
    if dia==28 and mes==2:
        if anoBissexto(ano):
            dia=29
        else:
            dia=1
            mes=3
    elif dia==30 and mes30(mes):
        dia=1
        mes=mes+1
    elif dia==31:
        if mes==12:
            dia=1
            mes=1
            ano=ano+1
        else:
            dia=1
            mes=mes+1
    else:
        dia=dia+1
    return '%02d/%02d/%d'%(dia,mes,ano)

#11 - intercalar strings
def intercala(s1,s2):
    if not s1:
        return s2
    if not s2:
        return s1
    return s1[0]+s2[0]+intercala(s1[1:],s2[1:])

#14 - verificar strings iguais
def igual(s1,s2):
    if not s1 and not s2:
        return True
    if not s1 or not s2:
        return False
    if s1[0]==s2[0]:
        return igual(s1[1:],s2[1:])
    else:
        return False

#15 - prefixo
def prefixo(s1,s2):
    if not s1:
        return True
    if not s2:
        return False
    if s1[0]==s2[0]:
        return prefixo(s1[1:],s2[1:])
    else:
        return False

#18 - aposentadoria
"""def data1_posterior_data2(dia1,mes1,ano1,dia2,mes2,ano2):
    #queremos saber se data 1 e posterior a data 2
    if ano1>ano2:
        return True
    if ano1==ano2:
        if mes1>mes2:
            return True
        if mes1==mes2:
            if dia1>=dia2:
                return True
            return False
    return False
    
def temDireito(idade,sexo,diaFil,mesFil,anoFil):
    if (idade>=65 and sexo=='m') or (idade>=60 and sexo=='f'):
        if data1_posterior_data2(diaFil,mesFil,anoFil,25,7,1991):
            qtd=int(input('contribuicoes mensais realizadas?'))
            if qtd>=180:
                return True
            return False
        return True
    return False

nome=input('Nome?')
idade=int(input('Idade?'))
sexo=input('Sexo?')
diaF=int(input('Dia de filiacao?'))
mesF=int(input('Mes de filiacao?'))
anoF=int(input('ano de filiacao?'))
resp=temDireito(idade,sexo,diaF,mesF,anoF)
if resp:
    print('%s, voce ja tem direito a sua aposentadoria'%nome)
else:
    print('%s, voce ainda nao tem direito a sua aposentadoria'%nome)"""

#19 - presenca
"""def indicePresenca(numAulas,numPres):
    freq=numPres/numAulas
    if freq>=0.95:
        indice=3
    elif freq>=0.90:
        indice=2
    elif freq>0.80:
        indice=1
    else:
        indice=0
    return indice

def acrescimoSobreNota(numAulas,numPres,nota):
    indice=indicePresenca(numAulas,numPres)
    perc=indice*0.03
    acrescimo=perc*nota
    return acrescimo

def notaFinal(numAulas,numPres,notaOrig):
    acrescimo=acrescimoSobreNota(numAulas,numPres,notaOrig)
    nota=notaOrig+acrescimo
    if nota<10:
        return nota
    else:
        return 10
    
numAulas=int(input('Numero de aulas da disciplina?'))
nome=input('Nome?')
media=float(input('Media atual?'))
numPres=int(input('Numero de presencas?'))
notaF=notaFinal(numAulas,numPres,media)
print('Nome: %s  Nota original: %.1f  Nota final: %.1f'%(nome,media,notaF))"""

#20 - restaurante
"""def descontoAtual(valor):
    if valor>300:
        desconto=0.25
    elif valor>=100:
        idade=int(input('qual a idade?'))
        if idade>50:
            desconto=0.15
        else:
            desconto=0
    else:
        desconto=0
    return desconto*valor

def valeDesconto(valor,pratos,bebidas):
    if valor>400:
        vale=100
    elif valor>=150:
        if pratos>=3:
            if bebidas>=6:
                vale=50
            else:
                vale=30
        elif bebidas>=6:
            vale=20
        else:
            vale=0
    elif pratos>=1 and bebidas>=1:
        vale=10
    else:
        vale=0
    return vale

valor=int(input('valor da conta?'))
numPratos=int(input('numero de pratos?'))
numBebidas=int(input('numero de bebidas?'))
desconto=descontoAtual(valor)
valorFinal=valor-desconto
vale=valeDesconto(valor,numPratos,numBebidas)
print('Valor final: R$%.2f  Vale desconto na proxima compra: R$%.2f'%(valorFinal,vale))"""



            







