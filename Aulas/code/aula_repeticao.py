'''
def CalculaST(temp, vent):
    st = 33+(10*(vent**(1/2)) + 10.45 - vent)*(temp - 33)/22
    return st

cont = 0
while cont < 5:
    t = float(input("Temperatura? "))
    v = float(input("Velocidade? "))
    st = CalculaST(t, v)
    print("Sensação Térmica: %.2f" % st)
    cont = cont + 1  #cont += 1
'''

def CalculaLitros(peso):
    return 35*peso/1000

def ProcTurma(qtd_alunos):
    cont = 0
    qt_sup2 = 0
    total_litros = 0

    while cont < qtd_alunos:
        p = float(input("Peso do aluno " + str(cont+1) + ": "))
        agua = CalculaLitros(p)
        print("Aluno %d - Peso: %.2f - Litros de água: %.2f" %(cont+1, p, agua))

        if agua > 2:
            qt_sup2 += 1

        total_litros = total_litros + agua
        cont += 1

    print("O total de alunos que devem ingerir mais de 2 litros é: %d" % qt_sup2)
    print("Consumo total da turma: %.2f" % total_litros)
    print("Consumo médio por aluno: %.2f" % (total_litros/qtd_alunos))
    
    return total_litros

nTurmas = 0
total_litros = 0
while(nTurmas < 5):
    print('\n Turma %d' % (nTurmas + 1))
    alunos = int(input("Quantos alunos?"))
    litro_turma = ProcTurma(alunos)

    total_litros += litro_turma
    nTurmas = nTurmas + 1

print("\n Total de litros das 5 turmas: %.2f" % total_litros)
    
    
