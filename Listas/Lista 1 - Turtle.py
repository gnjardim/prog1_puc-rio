import turtle

### 1 -------------------------------------------------------
# funções
def desenhaRetangulo(tar, cor, lado1, lado2):
    tar.color(cor)
    tar.fd(lado1)
    tar.rt(90)
    tar.fd(lado2)
    tar.rt(90)
    tar.fd(lado1)
    tar.rt(90)
    tar.fd(lado2)
    tar.rt(90)
    return

def desloca(tar, dist):
    tar.up()
    tar.fd(dist)
    tar.down()
    return

tartaruga = turtle.Turtle()
desenhaRetangulo(tartaruga, "yellow", 100, 50)
desloca(tartaruga, 50)
desenhaRetangulo(tartaruga, "blue", 100, 50)
desloca(tartaruga, 100)
tartaruga.rt(90)
desloca(tartaruga, 100)
tartaruga.rt(90)
desenhaRetangulo(tartaruga, "green", 100, 50)
desloca(tartaruga, 50)
desenhaRetangulo(tartaruga, "red", 100, 50)


### 2 -------------------------------------------------------
# funções
def ladoQuad(perim):
    lado = perim/4
    return lado

def diagonalQuad(lado):
    diagonal = lado/(2**(1/2))
    return diagonal

def metade(medida):
    met = medida/2
    return met

tartaruga = turtle.Turtle()

# medidas
lado_l = ladoQuad(160)
raio_inscr = metade(lado_l)
raio_circun = diagonalQuad(lado_l)

# quadrado
tartaruga.color("blue")
tartaruga.fd(lado_l)
tartaruga.lt(90)
tartaruga.fd(lado_l)
tartaruga.lt(90)
tartaruga.fd(lado_l)
tartaruga.lt(90)
tartaruga.fd(lado_l)
tartaruga.lt(90)

# desloca
tartaruga.up()
tartaruga.fd(metade(lado_l))
tartaruga.down()

# inscrita
tartaruga.color("red")
tartaruga.circle(raio_inscr)

# desloca
tartaruga.up()
tartaruga.rt(90)
tartaruga.fd(raio_circun - raio_inscr)
tartaruga.lt(90)
tartaruga.down()

# circunscrita
tartaruga.color("red")
tartaruga.circle(raio_circun)
