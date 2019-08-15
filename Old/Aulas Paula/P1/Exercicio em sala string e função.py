#Exercicio 1 publico

def junta(x,y):
    yInv=y[-1::-1]
    return x+yInv
    
def criarSenha(dia,mes,ano):
    a=junta(mes+'$',dia)
    b=junta('#'+dia+'!',mes)
    c='*'+ano
    return a+b+c

data='05/08/1997'
senha=criarSenha(data[0:2],data[3:5],data[6:])

#exercicio 2 publico

def erro_absoluto(exato,aprox):
    return abs(exato-aprox)

def erro_relativo(exato,aprox):
    erroAbs=erro_absoluto(exato,aprox)
    return erroAbs/aprox

def erro_percentual(exato,aprox):
    erroRel=erro_relativo(exato,aprox)
    return erroRel*100

x=5
y=5.02
erroPerc=erro_percentual(x,y)
