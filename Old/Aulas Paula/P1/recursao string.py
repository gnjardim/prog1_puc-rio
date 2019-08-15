#Com string conseguimos retirar ou o primeiro ou o segundo caracter
#s=s[0]+s[1:] ou s[:-1]+s[-1]
#com numeros interiso só conseguimos retirar o ultimo algarismo

def contaCaracteres(s):
    if s=='': #mais elegante: if not s: (string vazia é vista como falso)
        return 0
    return 1+contaCaracteres(s[1:]) #ou s[:-1]

def contaLetrasMaiusc(s):
    if not s:
        return 0
    ult=s[-1] #ou s[0]
    if 'A'<=ult<='Z':
        return 1+contaLetrasMaiusc(s[:-1]) #ou s[1:]
    else:
        return contaLetrasMaiusc(s[:-1]) #ou s[1:]

#Exercicios em sala

#1
def exibirVertical(s):
    if not s: 
        return
    print(s[0])
    exibirVertical(s[1:])
    return

"""def exibirVertical(s):
    print(s[0])
    exibirVertical(s[1:])
    return""" #3-> da erro

#2
def duplicarCaract(s):
    if not s:
        return ''
    return s[0]*2+duplicarCaract(s[1:])

#3
def vogal(s):
    if s[0]=='a' or s[0]=='e' or s[0]=='i' or s[0]=='o' or s[0]=='u' or\
       s[0]=='A' or s[0]=='E' or s[0]=='I' or s[0]=='O' or s[0]=='U':
        return True
    return False

def duplicarVogal(s):
    if not s:
        return''
    if vogal(s[0]):
        return s[0]*2+duplicarVogal(s[1:])
    else:
        return s[0]+duplicarVogal(s[1:])

print(duplicarVogal('Maria'))

#4
def inserirHashtag(s):
    if not s:
        return ''
    if s[0]==' ':
        return '#'+inserirHashtag(s[1:])
    else:
        return s[0]+inserirHashtag(s[1:])


