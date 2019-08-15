'''
# abrindo arquivos
arq = open("dados.txt", "r")
texto = arq.read()
print(texto)
arq.close()


# repetição
arq = open("dados.txt", "r")
linha = arq.readline()
while linha != '':
    print(linha)
    linha = arq.readline()

arq.close()

    
# lista
arq = open("dados.txt", "r")
for linha in arq:
    linha = linha.strip()
    print(linha)

arq.close()
'''

# escrevendo em arquivo
arq = open("dados.txt", "w")
arq.write("uma string\n")
arq.write("outra string\n")
arq.write("mais uma string\n")
arq.write("ultima string\n")
arq.close()


# funções
def lista_aprovados(arq):
    arquivo = open(arq, "r")
    
    for linha in arquivo:
        l_aluno = linha.split(",")

        nome = l_aluno[0]
        nota1 = float(l_aluno[1])
        nota2 = float(l_aluno[2])

        media = (nota1+nota2)/2
        if media >= 5:
            print("%-10s está aprovado(a)" % nome)

    arquivo.close()
    return
        
lista_aprovados("alunos.txt")





