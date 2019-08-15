### 1 ------------------------------------------------------
def ParcelaCompra(valor):
    if valor <= 200:
        q_parcela = 2
               
    elif valor <= 600:
        q_parcela = 4
        
    elif valor <= 1400:
        q_parcela = 8

    else:
        q_parcela = 10
        
    val_parcela = valor/q_parcela
    return print("Quantidade de parcelas: %d, Valor das parcelas: %.2f" %
                (q_parcela, val_parcela))

ParcelaCompra(1400.01)
        
### 2 ------------------------------------------------------
def AprovaAluno():

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    n_faltas = int(input("Faltas: "))

    nota_f = (nota1 + nota2)/2
    print("Sua média é: %.2f" % nota_f)
    
    if nota_f >= 5 and n_faltas < 15:
        print("Parabéns, aprovado")

        if nota_f > 9:
            print("Gostaria de ser monitor no próximo semestre?")

    return

AprovaAluno() 

### 3 ------------------------------------------------------
def AlertaSaldo(saldo, v_saque):

    n_saldo = saldo - v_saque
    print("Novo saldo: %.2f" % n_saldo)

    if n_saldo < 0:
        print("Alerta: saldo negativo")

        if n_saldo < -10000:
            print("Compareça a agência")

    return

AlertaSaldo(0, 100000)


    
    
