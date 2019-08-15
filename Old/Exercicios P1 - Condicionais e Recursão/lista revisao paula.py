#Revisao P1

#1 - area da figura (funcao)

"""def areaRetangulo(b,a):
    return b*a

def hipotenusa(c1,c2):
    return (c1**2+c2**2)**(1/2)

def areaTotal(a,b,c,d,e):
    retAB=areaRetangulo(a,b)
    retCD=areaRetangulo(c,d)
    retE=areaRetangulo(e,hipotenusa(a,d))
    triang=areaRetangulo(a,d)/2
    areaT=retAB+retCD+retE+triang
    print('Area retangulo 1: %.1f  Area retangulo 2: %.1f\
  Area retangulo 3: %.1f  Area triangulo: %.1f'%(retAB,retCD,retE,triang))
    return

a=float(input('Valor de a?'))
b=float(input('Valor de b?'))
c=float(input('Valor de c?'))
d=float(input('Valor de d?'))
e=float(input('Valor de e?'))
areaTotal(a,b,c,d,e)"""

#2 contar quantos 3 e 4 aparecem em um numero
def quantos3_ou_4(n):
    if n<10:
        if n==3 or n==4:
            return 1
        return 0
    elif n%10==3 or n%10==4:
        return 1+quantos3_ou_4(n//10)
    return quantos3_ou_4(n//10)


#3 parcelas - condicional
"""def qtdParcelas(valor):
    if valor<=200:
        qtd=2
        vParcela=valor/qtd
    elif 200.01<=valor<=600:
        qtd=4
        vParcela=valor/qtd
    elif 600.01<=valor<=1400:
        qtd=8
        vParcela=valor/qtd
    else:
        qtd=10
        vParcela=valor/qtd
    print('Quantidade de parcelas: %d  Valor da parcela: %.2f'%(qtd,vParcela))
    return"""

#4 - dia de pascoa - condicional
def descobre_x(ano):
    if 1900<=ano<=2199:
        return 24
    elif 2200<=ano<=2299:
        return 25
    return
    
def descobre_y(ano):
    if 1900<=ano<=2099:
        return 5
    elif 2100<=ano<=2199:
        return 6
    elif 2200<=ano<=2299:
        return 7
    #return?

def exibe_dia_mes(A,D,E):
    if D+E>9:
        dia=D+E-9
        mes=4
        if dia==26:
            novoDia=19
            print('%d/%d'%(novoDia,mes))
        elif dia==25 and D==28 and A>10:
            novoDia=18
            print('%d/%d'%(novoDia,mes))
        else:
            print('%d/%d'%(dia,mes))
    else:
        dia=D+E+22
        mes=3
        print('%d/%d'%(dia,mes))
    return

def dia_de_pascoa(ano):
    if ano<1900 or ano>2299:
        print('Impossivel de determinar')
        return
    A=ano%19
    B=ano%4
    C=ano%7
    X=descobre_x(ano)
    D=(19*A+X)%30
    Y=descobre_y(ano)
    E=(2*B+4*C+6*D+Y)%7
    exibe_dia_mes(A,D,E)
    return

#5 transformar numero em string - recursao
"""def string(n):
    if n<10:
        return '%d'%n
    return string(n//10)+string(n%10)"""

#6 verificar se todos os algarismos de um numero sao menos que de outro numero - recursao
"""def algMenores(n1,n2):
    if n1<10 and n2<10:
        if n1<n2:
            return True
        else:
            return False
    return algMenores(n1//10,n2//10) and algMenores(n1%10,n2%10)"""

#resolucao Paula:
"""def compAlg(num1,num2):
    if num1<10:
        if num1<num2:
            return True
        return False
    ult1=num1%10
    ult2=num2%10
    if ult1<ult2:
        return compAlg(num1//10,num2//10)
    else:
        return False"""

#7 string
"""def primSegInv(s1,s2):
    return s1[1:]+s2[-1:0:-1]"""

#8 string
"""def stringMaluca(s):
    copia=s[0:2]+s[-1:-3:-1]
    return s+copia*4"""

#9 desconto agencia de turismo - condicional
"""def desconto_padrao(preco,qtd):
    total=preco*qtd
    if qtd<=2:
        desconto=0.10*total
    elif 3<=qtd<=5:
        desconto=0.15*total
    else:
        desconto=0.20*total
    return desconto

def desconto_fidelidade(qtdInt,qtdMeia):
    if qtdInt==2*qtdMeia:
        desconto=200
    else:
        desconto=100
    return desconto

def valorFinal(precoInt,tipo,qtdInt,qtdMeia):
    if tipo=='n':
        desconto=desconto_padrao(precoInt,qtdInt)
    else:
        desconto=desconto_padrao(precoInt,qtdInt)+desconto_fidelidade(qtdInt,qtdMeia)
    precoMeia=0.50*precoInt
    total=precoInt*qtdInt+precoMeia*qtdMeia
    vFinal=total-desconto
    print('Desconto: %.2f  Valor total: %.2f'%(desconto,vFinal))
    return"""

#10 exibir(1234): 1 - 12 - 123 - 1234 (verticalmente) - recursao 
"""def exibir(n):
    if n<10:
        print(n)
        return
    exibir(n//10)
    print(n)
    return"""

#11 nota final concurso de fantasia (condicional)
"""def notaValida(n1,n2,n3):
    if n2<=n1<=n3 or n3<=n1<=n2:
        return n1
    if n1<=n2<=n3 or n3<=n2<=n1: #aqui if e mais apropriado que elif?
        return n2
    return n3"""
#outra alternativa seria notaValida=n[0] e depois retornar notaValida

"""nome=input('Nome?') #quando eh preciso usar input? quando ha palavras como obter, capturar?
o1=float(input('Primeira nota de originalidade?'))
o2=float(input('Segunda nota de originalidade?'))
o3=float(input('Terceira nota de originalidade?'))
b1=float(input('Primeira nota de beleza?'))
b2=float(input('Segunda nota de beleza?'))
b3=float(input('Terceira nota de beleza?'))
notaFinal=0.6*notaValida(o1,o2,o3)+0.4*notaValida(b1,b2,b3)
print('%s, sua nota final eh %.1f'%(nome,notaFinal))"""

#12 recursao - intercalar letras de duas strings
"""def intercalarLetras(s1,s2):
    if not s1 and not s2:
        return ''
    if not s2:
        return s1
    if not s1:
        return s2
    return s1[0]+s2[0]+intercalarLetras(s1[1:],s2[1:])"""



#13 - mudanca de base (recursao)

def mudarBase(n,b):
    if n<b:
        return str(n)
    return mudarBase(n//b,b)+str(n%b)


#14 - nova string apenas com algarismos repetidos (recursivo)
"""def repetirAlgarismos(s):
    if not s:
        return ''
    if s[0]>='0' and s[0]<='9': 
        return (s[0]*2)+repetirAlgarismos(s[1:])
    else:
        return s[0]+repetirAlgarismos(s[1:])"""

#15 - verificar 2 strings iguais (recursivo)
"""def igual(s1,s2):
    if not s1 and not s2:
        return True
    elif not s1 or not s2:
        return False
    return s1[0]==s2[0] and igual(s1[1:],s2[1:])"""

#16 verificar se a primeira string eh prefixo da segunda
"""def prefixo(s1,s2):
    if not s1:
        return True
    if not s2:
        return False
    return s1[0]==s2[0] and prefixo(s1[1:],s2[1:])"""

#17 - bonus
"""def temSol(s):
    if len(s)<3:
        return False
    if s[:3]=='sol' or s[0:3]=='Sol':
        return True
    return temSol(s[1:])

def acrescimo(nome,num,sexo):
    if sexo=='f':
        numAcrescimo=num+4
    else:
        numAcrescimo=num+2
    if temSol(nome):
        numAcrescimo=numAcrescimo+7
    return numAcrescimo
       
def numero_sorte(dia,mes,ano,sexo,nome):
    total=acrescimo(nome,dia,sexo)+acrescimo(nome,mes,sexo)+ano
    return total%10

nome=input('Qual o seu nome?')
sexo=input('Qual o seu sexo?(f ou m)')
estCivil=input('Estado civil?c-casado(a) ou o-outros)')
dataNasc=input('Data de nascimento?(dd/mm/aa)')
dia=int(dataNasc[0:2])
mes=int(dataNasc[3:5])
ano=int(dataNasc[-2:])
numSorte=numero_sorte(dia,mes,ano,sexo,nome)
if estCivil=='c':
    dataCasam=input('Data de casamento?(dd/mm/aa)')
    diaC=int(dataCasam[0:2])
    mesC=int(dataCasam[3:5])
    anoC=int(dataCasam[-2:])
    numSorte2=numero_sorte(diaC,mesC,anoC,sexo,nome)
    if numSorte2>numSorte:
        numSorte=numSorte2
bonus=numSorte*1000
print('%s, seu bônus de Natal é: R$.2f'%(nome,bonus))"""


#18 premio olimpico
"""def calcularPontos(ouro,prata,bronze):
    return ouro*6+prata*3+bronze*1

def calcularPremio(pontos,ouro):
    if pontos<=10:
        premio=50000
    elif pontos<=20:
        premio=200000
    else:
        premio=400000+ouro*10000
    print('Valor do premio: R$%.2f'%premio)
    return

ouro=int(input('Quantas medalhas de ouro'))
prata=int(input('Quantas mdalhas de prata?'))
bronze=int(input('Quantas medalhas de bronze?'))
pontos=calcularPontos(ouro,prata,bronze)
premio=calcularPremio(pontos,ouro)"""

#19
#assumindo data no formato dd/mm (em string)
"""def exibirValor(v):
    print('Valor do premio: R$%.2f'%v)
    return

def calculaPremio(dataPromo,dataAniver):
    diaP=dataPromo[0:2]
    mesP=dataPromo[-2:]
    diaA=dataAniver[0:2]
    mesA=dataAniver[-2:]
    if diaP==diaA and mesP==mesA:
        premio=30*(int(mesP)+int(diaP))
        exibirValor(premio)
        #nao precisa por return aqui?
    elif mesP==mesA:
        premio=20*int(mesP)
        exibirValor(premio)
    elif diaP==diaA:
        premio=0.5*int(diaP)
        exibirValor(premio)
    else:
        print('Nao tem direito')
        return"""

#20
"""def precoUnitario(codigo):
    if codigo%2==0:
        return codigo*0.15
    return codigo*0.04

def descontoValorTotal(valor):
    if valor<=1000:
        return valor
    if 1000<valor<=3000:
        desconto=0.25*valor
    elif 3000<valor<=5000:
        desconto=0.35*valor
    elif valor>5000:
        desconto+0.40*valor
    return valor-desconto

def temR(s):
    if not s:
        return False
    if s[0]=='r' or s[0]=='R':
        return True
    return temR(s[1:])

def temA(s):
    if not s:
        return False
    if s[0]=='a' or s[0]=='A':
        return True
    return temR(s[1:])

def descontoMes(valor,mes):
    if temR(mes):
        desconto=20
        if temA(mes):
            desconto=80
    else:
        desconto=35
    return valor-desconto*(valor//500)"""



