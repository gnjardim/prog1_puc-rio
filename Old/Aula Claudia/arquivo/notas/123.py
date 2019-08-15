'''arqE=open('C:\\Users\\PUC\\Desktop\\Notas.txt','r')
nota=arqE.read()
while nota:
    nota=nota.strip()
    print(notas)
    nota=arqE.read()'''


'''arqE=open('C:\\Users\\PUC\\Desktop\\Notas.txt','r')
for linha in arqE:
    linha=linha.strip()
    print(linha)'''
    
arqE=open('Notas.txt','r')
arqS=open('Em_G4','w')
for linha in arqE:
    linha=linha.strip()
    lvals=linha.split(',')
    nome=lvals[0]
    n=float(lvals[1])
    if n<5 :
        arqS.write('%s está na G4\n'%(nome))
arqE.close()
arqS.close()
