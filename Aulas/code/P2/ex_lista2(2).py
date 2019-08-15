### 3 -------------------------------------------------------
'''
def caractereNumerico(string):
    for s in string:
        if s in '0123456789':
            return True

    return False


def caractereMaiusculo(string):
    for s in string:
        if 'A' <= s <= 'Z':
            return True

    return False


def caractereEspecial(string):
    for s in string:
        if s in '!$@#%()':
            return True

    return False


def classificaUmaSenha(senha):
    crit1 = caractereNumerico(senha)
    crit2 = caractereMaiusculo(senha)
    crit3 = caractereEspecial(senha)

    if crit1:
        if crit2 and crit3:
            seg = "FORTE"

        else:
            seg = "MÉDIO"

    elif crit2:
        seg = "RAZOÁVEL"

    elif crit3:
        seg = "FRACO"

    else:
        seg = "MUITO FRACO"

    return seg


def classificaTodasSenhas(q_dep):
    cont = 0
    abx_medio = 0

    while cont < q_dep:
        snh = input("Digite sua senha para depósito %d: " % (cont+1))
        nivel = classificaUmaSenha(snh)
        print("Nível de segurança: %s" % nivel)

        if nivel == "RAZOÁVEL" or nivel == "FRACO" or nivel == "MUITO FRACO":
            abx_medio += 1

        cont += 1

    return abx_medio


def determinaQtdDepositos(categoria):
    if categoria == "Aluno":
        deps = 1

    elif categoria == "Professor":
        deps = 2

    elif categoria == "Pesquisador":
        deps = 3

    else:
        deps = 4

    return deps

cont_cat = 0
a_medio = 0
cat = input("\nDigite sua categoria: ")

while cat != "FIM":
    q_deps = determinaQtdDepositos(cat)

    a_medio += classificaTodasSenhas(q_deps)
    cont_cat += q_deps

    cat = input("\nDigite sua categoria: ")

print("O percentual de senhas com nível de segurança inferior ao nível MÉDIO é de %.1f %%" % ((a_medio/cont_cat)*100))
'''


### 4 -------------------------------------------------------
def contaCaracteres(l):
    caract = 0
    
    for el in l:
        if type(el) is list:
            caract += contaCaracteres(el)

        elif type(el) is str:
            caract += len(el)

    return caract

lista = ["ano", 2016, ["saúde",2,7.2,'a?'], 'mais 1 email: feliz!']
contaCaracteres(lista)
        
    
