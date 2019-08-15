#1

"""n=int(input('Número de pessoas inscritas?'))
conta=0
somaNota=0
contaManha=0
while conta<n:
    matr=int(input('Matrícula?'))
    turno=int(input('Turno? 1=manhã 2-tarde 3-noite'))
    if turno==1: # ou fazer uma função pra isso
        mensagem='Bom dia'
    elif turno==2:
        mensagem='Boa tarde'
    else:
        mensagem='Boa noite'
    print('Matrícula: %d, %s'%(matr,mensagem))
    nota=int(input('Nota pro professor?'))
    if turno==3:
        nota2=int(input('Qual a outra nota?'))
        nota=(nota+nota2)/2
    elif turno==1:
        if nota<5:
            contaManha+=1
    somaNota+=nota
    conta+=1
notaFinal=somaNota/n
print('Nota do professor: %.1f'%notaFinal)
print('Pessoas de manhã que atribuíram nota menor que 5: %d'%contaManha)"""

#2
zodiaco=['Macao','Galo','Cao','Porco','Rato','Boi','Tigre','Coelho','Dragao','Serpente','Cavalo','Carneiro']
aniversarios=['05/08/1997','18/06/1963','02/07/1967','21/10/2014','04/12/2016']
def exibirSignos(Lzod,Laniver):
    for el in Laniver:
        ano=int(el[6:])
        ciclo=ano%12
        signo=Lzod[ciclo]
        print('Signo do membr@ nascid@ em %s: %s'%(el,signo))
    return

#3
def mesmos_elementos(l1,l2):
    for el in l1:
        if el not in l2:
            return False
    return True

def exibaVencedores(lres,ljogadores):
    for jogador in ljogadores:
        if mesmos_elementos(jogador[1],lres):
            print('Jogador vencedor: %s'%jogador[0])
    return

Lres=[5,12,27,34,49,57]
Ljog=[['1234',[57,34,49,27,12,5]],['6543',[33,12,5,67,8,9]],['4321',[5,12,27,34,49,55]]]
exibaVencedores(Lres,Ljog)

#4

def temNumero(s):
    for letra in s:
        if '0'<letra<'9':
            return True
    return False

def temMaiusculo(s):
    for letra in s:
        if 'A'<letra<'Z':
            return True
    return False

def temCaracterEsp(s):
    caract='!$@#%()'
    for letra in s:
        if letra in caract:
            return True
    return False

def classificaUmaSenha(s):
    if temNumero(s) and temMaiusculo(s) and temCaracterEsp(s):
        nivel='FORTE'
    elif temNumero(s):
        nivel='MEDIO'
    elif temMaiusculo(s):
        nivel='RAZOAVEL'
    elif temCaracterEsp(s):
        nivel='FRACO'
    else:
        nivel='MUITO FRACO'
    return nivel

def classificaTodasSenhas(qtd):
    contaInf=0
    for senha in range(qtd):
        senha=input('Informe a senha')
        nivel=classificaUmaSenha(senha)
        print(nivel)
        if nivel=='MUITO FRACO' or nivel=='FRACO':
            contaInf+=1
    return contaInf

def determinaQtdDepositos(categoria):
    if categoria=='Aluno':
        qtd=1
    elif categoria=='Coordenador':
        qtd=4
    else:
        qtd=2
    return qtd

"""somaQtdSenhas=0
somaSenhasInf=0
categoria=input('Categoria do usuario?')
while categoria!='FIM':
    depositos=determinaQtdDepositos(categoria)
    totalInf=classificaTodasSenhas(depositos)
    somaQtdSenhas+=depositos
    somaSenhasInf+=totalInf
    categoria=input('Categoria do usuario?')
percentual=(somaSenhasInf/somaQtdSenhas*100)
print('Percentual de senhas com nivel de seguranca inferior a MEDIO: %.0f%%'%percentual)"""

#5
def classificaDBO(valDBO,lClass):
    val=int(valDBO)
    if val>4:
        val=4
    return lClass[val]
#poderia ter deixado com if/elif/else

def buscaMaior(lista):
    maior=-1
    for el in lista:
        if type(el)==float:
            if el>maior:
                maior=el
        else:
            maiorLocal=buscaMaior(el)
            if maiorLocal>maior:
                maior=maiorLocal
    return maior

def busca_maior(ldbo):
    if not ldbo:
        return -1
    maior=busca_maior(ldbo[1:])
    if type(ldbo[0])==list:
        m=busca_maior(ldbo[0])
        if m>maior:
            maior=m
    elif ldbo[0]>maior:
        maior=ldbo[0]
    return maior

def piorClassificacao(listaVal):
    lClass=['muito limpo','limpo','razoavel','ruim','pessimo']
    maior=buscaMaior(listaVal)
    classificacao=classificaDBO(maior,lClass)
    return classificacao

def classificaRios(listaRios):
    novaL=list()
    for el in listaRios:
        classif=piorClassificacao(el[1])
        novaL.append([el[0],classif])
    return novaL

lDBO=[['Rio AMAZONAS', [3.9, [2.7,2.3, 2.3, 5.6],1.0,[2.0,2.0], 2.0]],

     	  ['Rio URUGUAI', [[1.9, 1.8], 1.8, 0.3, 1.6, [1.0, 2.0, 1.9, 2.0]]],

        ['Rio TIETE', [3.9, [2.7, 3.0, 3.8, 2.3], [1.6, 1.0],[1.0, 2.0], 2.5]],

        ['Rio GUANDU', [4.0, [2.7, 7.8, 2.3, 5.6], [1.0, 9.0], 2.0, 2.0]],

        ['Rio DA PRATA', [0.02, [0.1, 0.1, 0.1], 0.05, 0.09, 0.08]],

        ['Rio TIETE', [1.8, 1.0, 0.8, 4.0, 3.0]],

        ['Rio NEGRO', [[1.9, 1.8], 1.8, 0.3, 1.6, [1.0, 1.8, 1.9, 1.9]]]]
      
