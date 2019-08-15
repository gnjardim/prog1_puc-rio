'''
def preenche():
    lAluno = list()

    nome = input("Digite nome. Fim para finalizar. ")

    while nome != "Fim":
        lAluno += [nome]
        nome = input("Digite nome. Fim para finalizar. ")

    return lAluno

def exibe(l):
    l.sort()
    for el in l:
        print("%-20s |__||__||__||__||__|" % el)
    return

lista = preenche()
exibe(lista)    
'''

def processaInclusao(l, matr):
    if matr not in l:
        l.append(matr)
    else:
        print("Operação inválida. Aluno já inscrito")

    return l

def processaExclusao(l, matr):
    if matr in l:
        l.remove(matr)
    else:
        print("Operação inválida. Aluno não inscrito")

    return l


lista_i = list()
op = input("\nDigite operação: I - incluir, E - excluir, F - finalizar ")
while op != "F":
    mat = int(input("Digite matrícula: "))
    curso = input("Digite curso: ")

    if curso != "Engenharia":
        print("Não pode se inscrever")

    else:
        if op == "I":
            processaInclusao(lista_i, mat)

        else:
            processaExclusao(lista_i, mat)

    op = input("\nDigite operação: I - incluir, E - excluir, F - finalizar ")

