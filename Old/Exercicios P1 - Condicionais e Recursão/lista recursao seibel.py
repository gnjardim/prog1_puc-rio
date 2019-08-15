#Lista de recursao do Seibel

#1
def quantos3e4(n):
    if n<10:
        if n==3 or n==4:
            return 1
        else:
            return 0
    return quantos3e4(n%10)+quantos3e4(n//10)

#2
def string(n):
    if n<10:
        return '%d'%n
    return string(n//10)+string(n%10)

#3 
def posicaoMenor(n1,n2):
    if n1<10:
        if n1<n2:
            return True
        return False
    if n1%10<n2%10: #se isso for verdade, verifique o resto. Se nao NAO PRECISA VERIFICAR O RESTO POIS JA SE TORNA FALSO
        return posicaoMenor(n1//10,n2//10)
    return False

#4
def inverter(n):
    if n<10:
        return n
    return int(str(n%10)+str(inverter(n//10)))

#5
def exibirCrescente(n):
    if n<10:
        print(n)
        return
    exibirCrescente(n//10)
    print(n)
    return

#6
def mudarBase(n,b):
    if n<b:
        return str(n)
    return mudarBase(n//b,b)+str(n%b)

#7 - recebe um numero e uma base e retorna o numero na base 10

                   
#8
def elimina_alg(n,digito):
    if n==0:
        return 0
    if n%10==digito:
        return elimina_alg(n//10,digito)
    return elimina_alg(n//10,digito)*10+n%10                 

#9
def novoAlg(n):
    if n<=8:
        return n+1
    if n==9:
        return 0
    return int(str(novoAlg(n//10))+str(novoAlg(n%10)))

#10 - recebe string e exibe cada palavra em uma nova linha (palavras separadas por espaco ou virgula)
def separa(s):
    if not s:
        return
    if s[0]!=' ' and s[0]!=',':
        print(s[0],end='') #end='' faz com que o print nao adicione uma nova linha
    else:
        print('\n')
        #print() -> nao pula linha
    separa(s[1:])
    return

#11
def quantasPalavras(s):
    if not s:
        return 1
    if s[0]==' ' or s[0]==',':
        return 1+quantasPalavras(s[1:])
    else:
        return quantasPalavras(s[1:])

#12
def temCaractere(s,c):
    if not s:
        return False
    if s[0]==c:
        return True
    return temCaractere(s[1:],c)

#13
def quantosCaracteres(s,c):
    if not s:
        return 0
    if s[0]==c:
        return 1+quantosCaracteres(s[1:],c)
    return quantosCaracteres(s[1:],c)

#solucao da lista:
def contaCar(c,s):
    if s=='':
        return 0
    qtd=contaCar(c,s[1:])
    if s[0]==c:
        qtd+=1
    return qtd
    
#14
def verificarNumero(s):
    if not s:
        return ''
    if s[0]<'0' or s[0]>'9':
        return 'Erro'
    if verificarNumero(s[1:])=='Erro':
        return 'Erro'
    return int(s[0]+str(verificarNumero(s[1:])))

#15 - igual a 13

#16
def duplica(s):
    if not s:
        return ''
    return s[0]*2+duplica(s[1:])

#17
def duplicaAlg(s):
    if not s:
        return ''
    if '0'<=s[0]<='9':
        return s[0]*2+duplicaAlg(s[1:])
    return s[0]+duplicaAlg(s[1:])

#18 - so funciona se a string for perfeitamente simetrica
def palindromo(s):
    if not s:
        return True
    if s[0]==s[-1]:
        return palindromo(s[1:-1])
    return False

#19
def indice(s,c):
    if not s:
        return -1
    if s[0]==c:
        return 0
    cont=indice(s[1:],c)
    if cont==-1:
        return -1
    return 1+cont

#20
def MDC(x,y):
    if x%y==0:
        return y
    return MDC(y,x%y)

    
    
        

    
