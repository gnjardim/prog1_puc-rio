'''
Faça uma função para permitir que um usuário altere sua senha.
Esta função receba uma lista com seu login e uma sublista com suas
últimas senhas, na ordem inversa à criada
( isto é, a 1ª senha da lista é a senha atual que foi criada por último) 
Para alterar sua senha, o usuário deverá digitar seu login,
caso esteja correto, o usuário deverá, digitar a senha  atual.
Se ela estiver correta, o usuário  poderá alterar sua senha,
digitando duas vezes a nova senha.
Esta nova senha será aceita como atual, caso ela não seja igual às
5 últimas senhas.


Para testar sua função considere a seguinte lista de usuários:
lUser=[ 	['huguinho', ['12345','2134','123','55555','aaaa']],
		['luisinho', ['2345','bbbb','bbcc']],
		['zezinho', ['1111']],
		['lala',  ['12345','2134','bbbbb','aaaa']],
		['lele',  ['2345','bbbb']],
		['lili',  ['oi','tchau','secreta']]
	  ]
'''

def busca(l,elem):
    for (i,val) in enumerate(l):
        if elem == val[0]:
            return i
    return None

def validaNovaSenha(senhas):
    novaSenha=input('Nova Senha: ')
    while novaSenha in senhas:
        novaSenha=input('Senha já utilizada. Digite outra Senha: ')
    return novaSenha

def criaNovaSenha(senhas):
    novaSenha1= validaNovaSenha(senhas)
    novaSenha2= input('Confirma nova Senha: ')
    while novaSenha1 !=novaSenha2:
         novaSenha1= validaNovaSenha(senhas)
         novaSenha2= input('Confirma nova Senha: ')
    return novaSenha1

def atualiza(senhas,senha):
    senhas.insert(0,senha)
    if len(senhas)>5:
        senhas.pop()
        
        
def alteraSenha(lUser):
    login=input('Login: ')
    resp= busca(lUser,login)
    if resp==None:
        print('Vc não é cadastrado')
        return
    senhas=lUser[resp][1]
    senhaAnt=input('Senha: ')
    if senhaAnt != senhas[0]:
        print('Senha inválida')
        return
    novaSenha=criaNovaSenha(senhas)
    atualiza(senhas,novaSenha)
    
    
    
lUser=[ 	['huguinho', ['12345','2134','123','55555','aaaa']],
		['luisinho', ['2345','bbbb','bbcc']],
		['zezinho', ['1111']],
		['lala',  ['12345','2134','bbbbb','aaaa']],
		['lele',  ['2345','bbbb']],
		['lili',  ['oi','tchau','secreta']]
	  ]

for i in range(4):
    alteraSenha(lUser)
    print('\nLista de users\n',lUser)
