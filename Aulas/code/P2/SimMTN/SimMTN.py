def busca(materia, lista):
    for (pos, m) in enumerate(lista):
        if m[0] == materia:
            return pos

    return None


def le_arq_disciplinas():
    al_discip = list()
    arq = open("disciplinas.txt", "r")

    for linha in arq:
        mat = linha.split()
        mat = mat[0]

        disc = arq.readline()
        alunos = disc.split()

        for (pos, al) in enumerate(alunos):
            alunos[pos] = int(al)

        al_discip.append([mat, alunos])

    arq.close()
    return al_discip


def atualiza_situacao(l):
    arq = open("solicitacoes.txt", "r")
    
    for linha in arq:
        mat = linha.split()
        mat = mat[0]

        disc = arq.readline()
        solic = disc.split()
        aluno = int(solic[0])
        
        pos_de = descobre_pos_turnos(solic[1])
        pos_para = descobre_pos_turnos(solic[2])

        pos = busca(mat, l)
        l[pos][1][pos_de] -= 1
        l[pos][1][pos_para] += 1

    arq.close()
    return


def gera_arq_atual(l):
    arq = open("atual.txt", "w")

    for disc in l:
        arq.write("%s " % disc[0])

        for alunos in disc[1]:
            arq.write("%d " % alunos)

        arq.write("\n")

    arq.close()
    return


def descobre_pos_turnos(turno):
    mtn = ['M','T','N']

    return mtn.index(turno)
    
        
l = le_arq_disciplinas()
atualiza_situacao(l)
gera_arq_atual(l)
        

        

        
