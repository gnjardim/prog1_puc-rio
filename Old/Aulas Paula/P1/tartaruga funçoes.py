import turtle
def DesenhaQuadrado(tart,lado):
    """Quadrado"""
    tart.fd(lado)
    tart.rt(90)
    tart.fd(lado)
    tart.rt(90)
    tart.fd(lado)
    tart.rt(90)
    tart.fd(lado)
    tart.rt(90)
    return

def Desloca(tart,dist):
    tart.penup()
    tart.fd(dist)
    tart.pendown()
    return

def DesenhaQuadradoColorido(tart,lado,cor):
    """Desenha quadrado colorido"""
    tart.begin_fill()
    tart.fillcolor(cor)
    tart.fd(lado)
    tart.lt(90)
    tart.fd(lado)
    tart.lt(90)
    tart.fd(lado)
    tart.lt(90)
    tart.fd(lado)
    tart.lt(90)
    tart.end_fill()
    return

jade=turtle.Turtle()
DesenhaQuadrado(jade,100)
Desloca(jade,100)
DesenhaQuadrado(jade,50)
Desloca(jade,50)
DesenhaQuadrado(jade,25)
    
    
