"""def calcula_media(a,b):
    return (a+b)/2

def testa_aprovado(n1,n2):
    med=calcula_media(n1,n2)
    print('Média: %.1f'%med)
    if med<5 or n1<3.0 or n2<3.0:
        print('Está na final')
        if (n1<2 or n2<2) and n2<n1: #use parenteses 
            print('precisa de atenção')
    return 
    
testa_aprovado(8.0,1.5)
testa_aprovado(2.8,4.0)
testa_aprovado(4.0,5.0)

def testa_aprovado_bool(n1,n2):
    med=calcula_media(n1,n2)
    return med>=5.0 and n1>=3.0 and n2>=3.0

if testa_aprovado_bool(3.6,7.2):
    print('Está aprovado')"""

#Exercicio: função booleana triangulo equilatero

def equilatero(l1,l2,l3):
    return l1==l2==l3  # podera ser if (l1==l2) and (l2==l3)

if equilatero(3,3,4):
    print('E equilátero')

def isosceles_nao_eq(l1,l2,l3):
    return ((l1==l2) or (l2==l3) or (l1==l3)) and (not equilatero(l1,l2,l3))

if isosceles_nao_eq(3,3,3):
    print('É isosceles não equilátero')
    
#Exercicio ano bissexto

def testa_bissexto():
    ano=int(input('Digite o ano'))
    if ano%4==0 and (ano%100!=0 or ano%400==0):
        print('É bissexto')
    return

testa_bissexto()

