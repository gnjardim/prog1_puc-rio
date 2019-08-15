#Exercicio
""""def IMC(massa,altura):
    return massa/altura**2

def exibeDados(nome,idade,altura,peso):
    imc=IMC(peso,altura)
    print('Nome: %s'%nome)
    print('Idade: %d'%idade)
    print('Altura: %4.2f'%altura)
    print('Peso: %5.1f'%peso)
    print('IMC: %4.1f'%imc)
    return

nome=input('Seu nome?')
idade=int(input('Idade?'))
altura=float(input('Altura?'))
peso=float(input('Peso?'))
exibeDados(nome,idade,altura,peso)"""

#exrcicio 6
def Aumenta(texto):
    meio=len(texto)//2
    return texto[:meio]+texto+texto[meio:]

nomeCompl=input('Qual seu nome completo?')
print(Aumenta(nomeCompl))


