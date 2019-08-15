### 1
def qtAlg(s):
    if s == "":
        return -1

    if s[0] == "@":
        return 0

    cont = qtAlg(s[1:])
    if cont == -1:
        return -1
    if s[0] in "1234567890":
        return 1 + qtAlg(s[1:])

    return qtAlg(s[1:])


### 2
def ehMultiplo(num1, num2):
    return num1 % num2 == 0
        
def algarismoDigitoVerificador(pb):
    if ehMultiplo(pb, 2):
        return pb%8
    else:
        return pb%7

def parteBaseDigitoVerificador(num):
    a1 = num//100
    a2 = (num//10)%10
    a3 = num%10

    return a1*8 + a2*4 + a3*3

def digitosVerificadores(n):
    pb1 = parteBaseDigitoVerificador(n//1000)
    pb2 = parteBaseDigitoVerificador(n%1000)

    x = algarismoDigitoVerificador(pb1)
    y = algarismoDigitoVerificador(pb2)
    return 10*x + y


### 3
def geraCaracteres(idade, sexo):
    if sexo == 'm':
        if 0 <= idade < 18:
            string = "#*"
            
        elif idade < 40:
            string = "$%"

        else:
            string = "&@"

    if sexo == 'f':
        if 0 <= idade < 21:
            string = "#%"

        else:
            string = "&$"

    return string

def geraSenhaBase(nome, data):
    d1 = int(data[0:2])
    d2 = int(data[3:])
    soma = str(d1 + d2)
    
    p1 = nome[:(len(nome)//2):-1]
    p2 = nome[(len(nome)//2)::-1]

    return p1 + soma + p2

def geraSenhaAcesso():
    nome  = input("Nome: ")
    idade = int(input("Idade: "))
    data  = input("Data de aniversário: ")
    sexo  = input("Sexo: ")

    c = geraCaracteres(idade, sexo)
    sb = geraSenhaBase(nome, data)

    return c[0:1] + sb + c[1:]



    
            




    
