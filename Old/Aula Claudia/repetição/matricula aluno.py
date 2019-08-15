'''matricula=int(input('qual matricula? ou 0 se quiser parar '))
while matricula!=0:
    prova=float(input('nota da prova: '))
    mediaTrab=float(input('Qual media dos trabalhos? '))
    mediaFinal=0.85*prova+0.15*mediaTrab
    print('Matrícula: %d \nNota prova: %.1f\nMédia dos trabalhos: %.1f\nMédia Final: %.1f'%(matricula,prova,mediaTrab,mediaFinal))
    matricula=int(input('\nQual matricula? ou 0 se quiser parar'))'''


def mediaPond(npr,ntrab):
    return npr*0.85+ntrab*0.15
def obtemNotaValida(mens):
    nota=float(input(mens))
    while nota<0 and nota>10:
        print('\nvalor invalido')
        nota=float(input(mens))
        return nota
totmed=0
qtAl=0
matr=int(input('Matricula? 0 finaliza'))
while matr!=0:
    npr=obtemNotaValida('\t\tNota da prova?')
    ntrab=obtemNotaValida('\t\tMedia de trabalho?')
    med=mediaPond(npr,ntrab)
    print('Matricula: %d - media %.1f'%(matr,med))
    totmed+=med
    qtAl+=1

    matr=int(input('\tMatricula? 0 Finaliza'))

medTurma=totmed/qtAl
print('Media da turma: %.1f'%(medTurma))
