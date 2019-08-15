def calcularIMC(altura,massa):
    return massa/altura**2

def situacaoIMC(idade,altura,peso):
    imc=calcularIMC(altura,peso)
    print(imc)
    if imc<18.5:
        print('Abaixo do peso')
    elif imc<=24.9:
        print('Peso ideal')
    elif imc<=29.9:
        print('Sobre peso')
    elif imc<=34.9:
        print('Obesidade grau 1')
    elif imc<=39.9:
        print('Obesidade grau 2')
    elif imc>=40:
        print('Obesidade grau 3')
    return

#usar if todas as vezes não é bom pq todos serão testados, enquanto o elif\
#só é executado qnd todos os anteriores forem false

#Exercicio em sala

def maiorNumero(a,b):
    if a>b:
        return a
    return b

"""Alternativa:
def maiorNumero(a,b):
    if a>n:
        maior=a
    else:
        maior=b
    return maior"""

"""a=int(input('Qual o numero?'))
b=int(input('Qual o outro numero'))
m=maiorNumero(a,b)
print('O maior número é',m)"""

def resultado_aluno(n1,n2):
    media=(n1+n2)/2
    if media>=5.0 and n1>=3.0 and n2>=3.0:
        print('Aprovado')
    elif media<3.0:
        print('Reprovado')
    else:
        notamin=10-maiorNumero(n1,n2)
        print('Aluno em final. Nota mínima é %.1f'%notamin)
    return

n1=float(input('Qual a primeira nota?'))
n2=float(input('Qual a segunda nota?'))
resultado_aluno(n1,n2)

#Exercicio biorritmo

def salBruto(horas,valorhora):
    return horas*valorhora

def INSS(salarioB):
    if salarioB<=800.45:
        inss=salarioB*0.0765
    elif salarioB<=900:
        inss=salarioB*0.0865
    elif salarioB<=1334.07:
        inss=salarioB*0.09
    elif salarioB<=2688.15:
        inss=salarioB*0.11
    else:
        inss=293.50
    return inss

def ImpRenda(salarioB):
    brutoMenosInss=salarioB-INSS(salarioB)
    if brutoMenosInss <=1257.12:
        impostoR=0
    elif brutoMenosInss <=2512.08:
        impostoR=0.15*(brutoMenosInss)-188.57
    else:
        impostoR=0.275*(brutoMenosInss)-502.58
    return impostoR

def salLiquido(horas,valorhora):
    salarioB=salBruto(horas,valorhora)
    return salarioB-INSS(salarioB)-ImpRenda(salarioB)

    

    
