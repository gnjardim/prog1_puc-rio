### 1 ----------------------------------------------------
def SelecionaCaixa(a, b, c):
    d = (a**2 + b**2 + c**2)**(1/2)

    if d <= 10:
        esf = 10
        
    elif d <= 15:
        esf = 15
        
    elif d <= 20:
        esf = 20
        
    else:
        esf = 25

    return esf


cod = int(input("\nCódigo do brinquedo: "))
cont_10 = 0
cont_15 = 0
cont_20 = 0
cont_25 = 0

while cod >= 0:
    a_in = float(input("Largura da caixa: "))
    b_in = float(input("Comprimento da caixa: "))
    c_in = float(input("Altura da caixa: "))

    diametro = SelecionaCaixa(a_in, b_in, c_in)
    print("A esfera para embalar o brinquedo de código %d é a de: %d de diâmetro" % (cod, diametro))

    if diametro == 10:
        cont_10 += 1
    elif diametro == 15:
        cont_15 += 1
    elif diametro == 20:
        cont_20 += 1
    else:
        cont_25 += 1
        
    cod = int(input("\nCódigo do brinquedo: "))

print("\nNúmero de caixas com diâmetro 10: %d" % cont_10)
print("\nNúmero de caixas com diâmetro 15: %d" % cont_15)
print("\nNúmero de caixas com diâmetro 20: %d" % cont_20)
print("\nNúmero de caixas com diâmetro 25: %d" % cont_25)


### 2 ----------------------------------------------------
def Calcula_Prêmio(data_prom, data_nasc):
    dia_prom = int(data_prom[:2])
    mes_prom = int(data_prom[3:])

    dia_nasc = int(data_nasc[:2])
    mes_nasc = int(data_nasc[3:])

    if dia_prom == dia_nasc:
        if mes_prom == mes_nasc:
            premio = 30*(mes_nasc + dia_nasc)

        else:
            premio = 0.5*(dia_nasc)

    elif mes_prom == mes_nasc:
        premio = 20*mes_nasc

    else: 
        premio = 0

    return premio


data_promocao   = input("Data da promoção (dd/mm): ")
data_nascimento = input("Data de nascimento (dd/mm): ")

cont_pessoas = 0
total_premio = 0

while data_nascimento != "00/00":
    p = Calcula_Prêmio(data_promocao, data_nascimento)

    if p > 0:
        print("Seu prêmio é de: R$%.2f\n" % p)
        total_premio += p
        cont_pessoas += 1

    data_nascimento = input("Data de nascimento (dd/mm): ")

print("\nQuantidade de pessoas premiadas: %d" % cont_pessoas)
print("\nValor total distribuído: R$%.2f" % total_premio)
    

    






    
