'''
def Tabuada(n):
    mult = 1
    while mult <= 10:
        print("%d x %d = %d" % (mult, n, mult*n))
        mult += 1
    return


num = int(input("Número? "))

while num != 0:
    print("\n Tabuada do ", num)
    Tabuada(num)
    
    num = int(input("Número? ")) # se usuário quiser parar, diz 0
'''


'''
def TransfereFrasco(qt_orig):
    qt_novo = 0

    while (qt_orig - qt_novo > 10):
        qt_orig -= 10
        qt_novo += 10

        evap1 = qt_orig*0.035
        evap2 = qt_orig*0.012
        
        qt_orig -= evap1
        qt_novo -= evap2

    print("Quantidade no frasco original: %.2f \n Quantidade no frasco final: %.2f" % (qt_orig, qt_novo))
    return

def qtValida():
    qt = float(input("Quantidade no frasco original? "))

    while (qt < 40 or qt > 230):
        print("Quantidade inválida. Digite um valor entre 40 e 230")
        qt = float(input("Quantidade no frasco original? "))

    return qt

frasco_original = qtValida()
TransfereFrasco(frasco_original)
'''

'''
def NotaValida(tipo_nota):
    nota = float(input(tipo_nota))

    while (nota < 0 or nota > 10): # enquanto não for valor correto
        print("Nota inválida. Digite um valor entre 0 e 10")
        nota = float(input(tipo_nota))

    return nota



matric = int(input("Qual a matrícula? "))
n_alunos = 0
total_turma = 0
    
while matric != 0:
    prova = NotaValida("Nota da prova? ")
    trab = NotaValida("Nota do trabalho? ")
    media_f = 0.8*prova + 0.2*trab

    print("Média do aluno %d: %.1f" % (matric, media_f))
    matric = int(input("Qual a matrícula? "))

    n_alunos += 1
    total_turma += media_f


media_turma = total_turma/n_alunos
print("\n Média da Turma: %.1f" % media_turma)
'''


def produto_vencido(dia_visita, mes_visita, ano_visita, dia_validade, mes_validade, ano_validade):
    if ano_visita == ano_validade:

        if mes_visita == mes_validade:
            if dia_visita > dia_validade:
                valid = True
            else:
                valid = False

        elif mes_visita > mes_validade:
            valid = True

        else:
            valid = False

    elif ano_visita > ano_validade:
        valid = True

    else:
        valid = False

    return valid


def calcula_multa(qt_conf, qt_fora):
    if qt_fora == 0:
        multa = 0

    elif qt_fora/qt_conf <= 0.1:
        multa = 100

    elif qt_fora/qt_conf <= 0.3:
        multa = 10000

    else:
        multa = 100000

    return multa


dia_v = int(input("Dia da visita? "))
mes_v = int(input("Mês da visita? "))
ano_v = int(input("Ano da visita? "))

nome = input("\n Nome do produto: ")
n_vencidos = 0
n_produtos = 0

while nome != '':

    dia_val = int(input("Dia da validade? "))
    mes_val = int(input("Mês da validade? "))
    ano_val = int(input("Ano da validade? "))

    if produto_vencido(dia_v, mes_v, ano_v, dia_val, mes_val, ano_val):
        n_vencidos += 1

    n_produtos += 1
    nome = input("\n Nome do produto: ")

valor_multa = calcula_multa(n_produtos, n_vencidos)

if valor_multa == 0:
    print("Supermercado isento de multas")

else:
    print("Valor da multa: %d" % valor_multa)

        
