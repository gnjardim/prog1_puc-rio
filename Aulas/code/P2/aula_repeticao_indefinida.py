'''
num = int(input("Digite um nº "))
maior = num

while num != 0:
    if num > maior:
        maior = num

    num = int(input("Digite um nº "))

print("O maior é: %d" % maior)
'''

import random

def ExibeSinal(n):
    if n > 0:
        print("%d é positivo" % n)
    elif n < 0:
        print("%d é negativo" % n)
    else:
        print("%d é zero" % n)

    return

def ExibePares(n):
    mult = 0

    while mult < n:
        print(mult, end = ' ')
        mult += 2

    print('')        
    return

num = random.randint(-100, 100)
qt_zero = 0
soma_par = 0
maior = 0
menor = 0
total = 0
cont = 0

while num != 5:
    ExibeSinal(num)
    
    if num%3 == 0 and num%4 == 0:
        ExibePares(num)

    if num == 0:
        qt_zero += 1

    if num%2 == 0:
        soma_par += num

    if num < menor:
        menor = num

    if num > maior:
        maior = num

    total += num
    cont += 1

    num = random.randint(-100, 100)

print("\nA quantidade de zeros gerada é: %d" % qt_zero)
print("\nA soma dos números pares é: %d" % soma_par)
print("\nO menor número negativo gerado é: %d" % menor)
print("\nO maior número positivo gerado é: %d" % maior)
print("\nA média dos números é: %.1f" % (total/cont))

    
