import turtle
import random

### 1
def detY(a, b, x):
    return a*x + b

def traca_Reta(tart, x1, y1, x2, y2, cor):
    tart.color(cor)
    tart.up()
    tart.goto(x1,y1)
    tart.down()
    tart.goto(x2,y2)
    return

def desenha_Reta(tart, a, b, cor):
    x1 = random.randint(-10, -1)
    x2 = random.randint(1, 10)

    y1 = detY(a, b, x1)
    y2 = detY(a, b, x2)

    traca_Reta(tart, x1, y1, x2, y2, cor)
    return

def retas_CoefAngulares_Diferentes(tart, a, b):
    if a>0:
        desenha_Reta(tart, a, b, 'black')
        desenha_Reta(tart, -a, b, 'grey')
    else: 
        desenha_Reta(tart, -a, b, 'black')
        desenha_Reta(tart, a, b, 'grey')
    return

'''
tartaruga = turtle.Turtle()
retas_CoefAngulares_Diferentes(tartaruga, -2, 40)
'''


