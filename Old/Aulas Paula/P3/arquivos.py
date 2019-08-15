def lista_aprovados(nomeArq):
    arq=open(nomeArq,'r')
    for linha in arq:
        lAluno=linha.split(',')
        nome=lAluno[0]
        nota1=float(lAluno[1])
        nota2=float(lAluno[2])
        media=(nota1+nota2)/2
        if media>=5:
            print(nome)
    arq.close()
    return

arq='dados.txt'
lista_aprovados(arq)

#ex inicial 1
"""coringa=int(input('Número coringa?'))
arq=open('numeros.txt','r')
arq2=open('saida.txt','w') #cria um novo arquivo chamado saida.txt
multiplos=list()
for linha in arq:
    num=int(linha)
    if num%coringa==0:
        arq2.write(linha) #numeros vem com \n
arq.close()
arq2.close()"""

#ex 2
def montaLista():
    lNotas=list()
    arqP=open('p1.txt','r')
    arqT=open('t1.txt','r')
    for linhaP in arqP:
        lP=linhaP.split(' ')
        matr=int(lP[0])
        p1=float(lP[1])
        linhaT=arqT.readline() #le uma linha por vez. lembra da ultima linha que leu
        lT=linhaT.split(' ')
        t1=float(lT[1])
        media=p1*0.8+t1*0.2
        lNotas.append([matr,media,[p1,t1]])
    arqP.close()
    arqT.close()
    return lNotas

def escreveArq(lAlunos):
    arqP=open('Preocupacoes.txt','w')
    arqN=open('Notas.txt','w')
    for el in lAlunos:
        arqN.write('Matricula:%d  Media:%.1f  P1:%.1f  T1%.1f\n'%(el[0],el[1],el[2][0],el[2][1]))
        if el[2][0]<4 and el[2][1]>7:
            arqP.write('%d %.1f\n'%(el[0],el[1]))
    arqP.close()
    arqN.close()
    return

lista=montaLista()
print(lista)
escreveArq(lista)

                  

