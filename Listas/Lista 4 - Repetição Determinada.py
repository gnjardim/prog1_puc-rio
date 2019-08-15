### 1 ----------------------------------------------------------
qt = int(input("Quantos Números? "))
cont = 0
dentro = 0
fora = 0
soma = 0

while cont < qt:
    num = int(input("Número? "))

    if num >= 1 and num <= 15:
        print("%d está dentro do intervalo" % num)
        dentro += 1
        soma += num

    else:
        print("%d está fora do intervalo" % num)
        fora += 1

    cont += 1

print("%d valores dentro do intervalo, soma = %d e média = %.1f" % (dentro, soma, (soma/dentro)))
print("%d valores fora do intervalo" % fora)


### 2 ----------------------------------------------------------
import random

def TemperaturaAtipica(temp):
    if temp < 15 or temp > 38:
        atipc = True
        
    else:
        atipc = False

    return atipc

cont = 1
dias = 31
total_max = 0
total_min = 0
atipico = 0

while cont <= dias:
    temp1 = random.randint(-10, 45)
    temp2 = random.randint(-10, 45)

    if temp1 <= temp2:
        minima = temp1
        maxima = temp2

    else:
        minima = temp2
        maxima = temp1

    total_max += maxima
    total_min += minima

    media = (minima+maxima)/2

    if TemperaturaAtipica(media):
        atipico += 1

    print("Média do dia %d: %.1f" % (cont, media))
    cont += 1

media_min = total_min/dias
media_max = total_max/dias
p_atip = atipico/dias*100

print("\nMédia das temperaturas mínimas: %.1f \nMédia das temperaturas máximas: %.1f \nPercentual de dias atípicos: %.1f%%" % (media_min, media_max, p_atip))


### 3 ----------------------------------------------------------
qt_pessoas = int(input("Quantas pessoas? "))
cont = 0
menor = 0
mais_20 = 0
total_idade = 0

while cont < qt_pessoas:
    idade = int(input("Idade da pessoa %d: " % (cont+1)))

    if idade < 18:
        menor += 1

    if idade > 20:
        mais_20 += 1

    total_idade += idade
    cont += 1

media_idade = total_idade/qt_pessoas
p_mais20 = mais_20/qt_pessoas*100

print("Quantidade de pessoas menores de idade: %d" % menor)
print("Média de idade: %.1f" % media_idade)
print("Percentual de pessoas com mais de 20 anos: %.1f%%" % p_mais20)


    
