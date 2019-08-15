# 1
'''
coringa = int(input("Número coringa: "))

arq_in = open("numeros.txt", "r")
arq_out = open("coringa.txt", "w")

for linha in arq_in:
    n = int(linha)
    
    if n%coringa == 0:        
        arq_out.write("%d \n" % n)
    
arq_in.close()
arq_out.close()
'''

# 2
arq_p1 = open("p1.txt", "r")
arq_t1 = open("t1.txt", "r")

lista_alunos = list()

def criaArquivos(l_alunos):
    preocup = open("Preocupacoes.txt", "w")
    notas = open("Notas.txt", "w")

    for aluno in lista_alunos:
        notas.write("%d, %.1f, %.1f, %.1f\n" % (aluno[0], aluno[1], aluno[2][0], aluno[2][1]))
        
        n_p1 = aluno[2][0]
        n_t1 = aluno[2][1]

        if n_p1 < 4 and n_t1 > 7:
            preocup.write("%d, %.1f" % (aluno[0], aluno[1]))

    preocup.close()
    notas.close()
    return


for linha_p1 in arq_p1:
    linha_t1 = arq_t1.readline()
    
    p1 = linha_p1.split(",")
    t1 = linha_t1.split(",")

    mat_p1 = int(p1[0])
    
    nota_p1 = float(p1[1])
    nota_t1 = float(t1[1])

    media_g1 = nota_p1*0.8 + nota_t1*0.2

    lista_alunos.append([mat_p1, media_g1, [nota_p1, nota_t1]])

criaArquivos(lista_alunos)

arq_p1.close()
arq_t1.close()

