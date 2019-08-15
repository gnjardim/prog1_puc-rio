"""def mediaPonderada(notaP,notaT):
    return notaP*0.85+notaT*0.15

matr=int(input('Qual a sua matricula?'))
conta7=0 #contador alunos com media maior que 7
totalAlunos=0 #contador numero total de alunos
somaMedias=0 #acumulador da soma das medias 
maiorMedia=-1 #comparador das medias para determinar maior media. Escolher valor que não faz parte do problema (existe nota 0 mas nao existe nota 1)
while matr!=0:
    totalAlunos+=1 #determina total de alunos
    notaP=float(input('Qual a nota da prova?'))
    notaTrab=float(input('Nota do trabalho?'))
    media=mediaPonderada(notaP,notaTrab)
    if media>7:
        conta7+=1 #determina alunos com media maior que 7
    print('Aluno %d teve média %.1f'%(matr,media))
    matr=int(input('Qual a sua matrícula?'))
    somaMedias+=media #acumula medias
    if media>maiorMedia: #determina maior media
        maiorMedia=media 
print('O total de alunos com nota>7 é',conta7)
mediaTurma=somaMedias/totalAlunos
print('A média da turma é %.1f'%mediaTurma)
print('A maior media foi %.1f'%maiorMedia)"""

#Exercicios do publico
#3
"""def respPositivas(num):
    jaFiz=0
    respPos=0
    while jaFiz<num:
        resp=input('Qual é a sua resposta para a questao?')
        if resp=='s':
            respPos+=1
        jaFiz+=1
    return respPos

def grupoRespostas(num,respSim):
    razao=respSim/num
    if razao>=2/3:
        grupo='Pró'
    elif razao<1/3:
        grupo='Contra'
    else:
        grupo='Neutro'
    print(grupo)
    return

num=int(input('Numero de respostas?'))
aluno=0
while aluno<400:
    matr=input('Qual a sua matricula?')
    respSim=respPositivas(num)
    print('O grupo do aluno %s é'%matr,end=': ')
    grupoRespostas(num,respSim)
    aluno+=1"""

#2
def produto_vencido(dia,mes,ano,diaVal,mesVal,anoVal):
    #retorna true se tiver vencido--> se data validade<data visita
    if ano>anoVal:
        return True
    if ano<anoVal:
        return False
    if mes>mesVal:
        return True
    if mes<mesVal:
        return False
    if dia>diaVal:
        return True
    return False

def calcula_multa(qtdConf,qtdVenc):
    razao=qtdVenc/qtdConf
    if qtdVenc==0:
        multa=0
    elif razao<=0.10:
        multa=100
    elif razao<=0.30:
        multa=10000
    else:
        multa=100000
    return multa

dia=int(input('Dia da visita?'))
mes=int(input('Mes da visita?'))
ano=int(input('Ano da visita?'))
nome=input('Qual o produto?')
contaProd=0
contaVenc=0
while nome!='':
    contaProd+=1
    diaVal=int(input('Dia da validade?'))
    mesVal=int(input('Mes da validade?'))
    anoVal=int(input('Ano de validade?'))
    if (produto_vencido(dia,mes,ano,diaVal,mesVal,anoVal)):
        print('Fora da validade')
        contaVenc+=1
    else:
        print('Dentro da validade')
    nome=input('Qual o produto?')

multa=calcula+multa(contaProd,contaVenc)
if multa==0:
    print('Supermercado isento de multas')
else:
    print('Valor da multa: R$%.2f'%multa)

