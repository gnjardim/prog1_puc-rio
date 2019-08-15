# Copie este arquivo para sua máquina na pasta indicada e o renomeie conforme o exemplo:
#            33B-1012983-MariaPatinhas.py;
#
# Caso você não consiga desenvolver uma função desta avaliação,
# a construa retornando um valor de sua escolha, mas você não terá os pontos da mesma.
#
# Complete as linhas abaixo com seus dados:
"""
Nome: 			                          
Matricula: 
Turma: 
Professor: 
"""

#Questão 1 - Desenvolva as funções da questão 1 aqui:

#ou vc para na string vazia ou para no arroba

def qntAlg(s):
    if not s:
        return -1
    if s[0]=='@':
        return 0
    cont=qntAlg(s[1:])
    if cont==-1:
        return -1
    if '0'<=s[0]<='9':
        return 1+cont
    return cont

#Questão 2 - Desenvolva as funções da questão 2 aqui:

def ehMultiplo(n1,n2):
    return n1%n2==0

def algarismosDigitoVerificador(PB):
    if ehMultiplo(PB,2):
        return PB%8
    return PB%7

def parteBaseDigitoVerificador(n):
    C=n//100
    D=n//10%10
    U=n%10
    return 8*C + 4*D + 3*U

def digitosVerificadores(n):
    pb1=parteBaseDigitoVerificador(n%1000)
    pb2=parteBaseDigitoVerificador(n//1000)
    y=algarismosDigitoVerificador(pb1)
    x=algarismosDigitoVerificador(pb2)
    return x*10+y


#Questão 3 - Desenvolva as funções da questão 3 aqui:

def geraCaracteres(idade,sexo):
    if sexo=='m':
        if idade<18:
            caract='#*'
        elif 18<=idade<40:
            caract='$%'
        else:
            carct='&@'
    else:
        if idade<21:
            caract='#%'
        else:
            caract='&$'
    return caract

def geraSenhaBase(nome,data):
    soma=int(data[0:2])+int(data[-2:])
    nomeInv=nome[-1::-1]
    meio=len(nomeInv)//2
    return nomeInv[0:meio]+str(soma)+nomeInv[meio:]

def geraSenhaAcesso(nome,idade,data,sexo):
    c1=geraCaracteres(idade,sexo)[0]
    sb=geraSenhaBase(nome,data)
    c2=geraCaracteres(idade,sexo)[1]
    return c1+sb+c2

   
#Teste da Questão 1
def QUESTAO1():
    print("\nTeste da Questão 1- exibindo os resultados de chamadas da função qtAlg com os valores fornecidos no texto da prova\n")
    qtd=qntAlg("Dia 5/05 tem 1@ e dia 2/2 tem 2 demais ")
    if qtd==-1:
        print('Não existe @')
    else:
        print('%d dígitos'%qtd)
    qtd=qntAlg("Dia 5/05 tem 1@ e dia 2/2 tem 2 demais, mas tem @ no texto")
    if qtd==-1:
        print('Não existe @')
    else:
        print('%d dígitos'%qtd)
    qtd=qntAlg("Dia 5/05 não tem 1 e dia 2/2 tem 2 demais")
    if qtd==-1:
        print('Não existe @')
    else:
        print('%d dígitos'%qtd)
    qtd=qntAlg("Dia @ 5/05 não tem 1 e dia 2/2 também")
    if qtd==-1:
        print('Não existe @')
    else:
        print('%d dígitos'%qtd)


#Teste da Questão 2
def QUESTAO2():
    print("\nTeste da Questão 2- exibindo os resultados de chamadas da função digitosVerificadores com os valores fornecidos no texto da prova\n")
    print(digitosVerificadores(123457))
    print(digitosVerificadores(1002))
    

#Teste da Questão 3
def QUESTAO3():
    print("\nLendo os dados de um funcionário e exibindo sua senha\n")
    nome=input('Nome?')
    idade=int(input('Idade?'))
    data=input('Data de aniversário? (dd/mm)')
    sexo=input('Sexo? (m ou f)')
    senha=geraSenhaAcesso(nome,idade,data,sexo)
    print('Senha de acesso:',senha)


#--------EXECUCAO DOS TESTES DAS QUESTÕES-------------------
QUESTAO1()
QUESTAO2()
QUESTAO3()
