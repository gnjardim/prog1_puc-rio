### 1
def SemanaDias(ds):
    semanas = ds//7
    dias = ds%7
    return print('%d semanas e %d dias' % (semanas, dias))

##dias_in = int(input("Número de dias?"))
##SemanaDias(dias_in)


### 2
def FormData(dt_string):
    dia = int(dt_string[:2])
    mes = dt_string[6:9]
    ano = int(dt_string[-4:])
    return print('%d/%s/%d' % (dia, mes, ano))

##data_in = input("Data?")
##FormData(data_in)
    
### 3
def CalculaMedia(p1, p2):
    return print(0.3*p1 + 0.7*p2)

##nota1 = int(input("Primeira Nota?"))
##nota2 = int(input("Segunda Nota?"))
##CalculaMedia(nota1, nota2)

### 4
def AlturaMetros(alt):
    metros = alt//100
    cent = alt%100
    return print('%dm %dcm' % (metros, cent))

##altura_in = int(input("Altura?"))
##AlturaMetros(altura_in)

### 5
from math import pi

def VolCaixa(lado1, lado2, lado3):
    return lado1*lado2*lado3

def VolCilindro(raio, altura):
    return pi*altura*(raio**2)

def VolCaixaFuro(a, b, h, d):
    caixa = VolCaixa(a, b, h)
    cilindro = VolCilindro(d, h)
    return print(caixa - cilindro)

lado_a = float(input("Lado a:"))
lado_b = float(input("Lado b:"))
alt    = float(input("Altura:"))
raio_c = float(input("Raio:"))


VolCaixaFuro(lado_a, lado_b, alt, raio_c)






    
