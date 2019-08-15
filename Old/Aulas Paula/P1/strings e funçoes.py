#exercicio 3a

def stringPar(texto):
    return texto[::2]

def stringContrario(texto):
    return texto[-1::-1]

def gerarSenha(nome,data):
    par=stringPar(nome)
    dia=data[0:2]
    invpar=stringContrario(par) #nao precisa chamar a função <stringPar> de novo pq ja foi feito
    return par+dia+invpar

nome='Maria Haniya'
data='05/08/1997'
senha=gerarSenha(nome,data)


