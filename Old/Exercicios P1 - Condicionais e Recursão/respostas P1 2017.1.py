#P1 2017.1

#1
"""def detY(a,b,x):
    return a*x+b

def traca_Reta(tart,x1,y1,x2,y2,cor):
    tart.color(cor)
    tart.up()
    tart.goto(x1,y1)
    tart.down()
    tart.goto(x2,y2)
    return

def desenha_Reta(tart,a,b,cor):
    x1=random.randint(-10,-1)
    x2=random.randint(1,10)
    y1=detY(a,b,x1)
    y2=detY(a,b,x2)
    traca_Reta(tart,x1,y1,x2,y2,cor)
    return

def retas_CoefAngulares_Diferentes(tart,a,b):
    if a>0:
        desenha_Reta(tart,a,b,'black')
        desenha_Reta(tart,-a,b,'gray')
    else:
        desenha_Reta(tart,a,b,'gray')
        desenha_Reta(tart,-a,b,'black')
    return

import turtle
import random
tat=turtle.Turtle()
retas_CoefAngulares_Diferentes(tat,2,40)"""

#2
"""def dentro_do_horario(h1,h2):
    hora1=int(h1[0:2])
    hora2=int(h2[0:2])
    min1=int(h1[-2:])
    min2=int(h2[-2:])
    if hora1<hora2:
        return True
    if hora1==hora2 and min1<=min2:
        return True
    return False

def valor_ingresso(h,sexo):
    if dentro_do_horario(h,'18:00'):
        ingresso=50
    elif sexo=='f':
        ingresso=60
    else:
        if dentro_do_horario(h,'20:00'):
            ingresso=70
        else:
            ingresso=80
    return ingresso

def valor_promocional(qtd):
    if qtd<=5:
        valor=qtd*8
    else:
        valor=5*8+(qtd-5)*20
    return valor

def valor_cupons(h,qtd):
    if dentro_do_horario(h,'20:00'):
        data=input('Qual o dia e o mes do seu aniversario?')
        if data=='25/04':
            qtd=qtd-1
        valor=valor_promocional(qtd)
    else:
        valor=qtd*20
    return valor

horario=input('Horario de entrada? (hh:mm)')
sexo=input('Sexo? (m ou f)')
qtd=int(input('Quantos cupons?'))
ingresso=valor_ingresso(horario,sexo)
cupons=valor_cupons(horario,qtd)
print('Total a pagar:')
print('Ingresso: R$%.2f'%ingresso)
print('Cupons: R$%.2f'%cupons)"""

#3
def inverte(s):
    principal=s[1:-1]
    return s[-1]+principal+s[0]

def replica(s):
    return (s[0]+s[-1])*3

def nomeParteSobrenome(s1,s2):
    if len(s2)<len(s1):
        return False
    if s2[0:len(s1)]==s1: 
        return True
    return nomeParteSobrenome(s1,s2[1:])

def temEspaco(s):
    if not s:
        return False
    if s[0]==' ':
        return True
    return temEspaco(s[1:])

def cria_senha(nome,sobrenome):
    if nomeParteSobrenome(nome,sobrenome):
        parte1=replica(nome)
        senha=parte1+sobrenome
    else:
        prefixo=inverte(nome[len(nome)//2:])
        sufixo=inverte(nome[0:len(nome)//2])
        if temEspaco(nome):
            senha=prefixo+sobrenome+sufixo
        else:
            senha=prefixo+sobrenome[-1::-1]+sufixo
    return senha

