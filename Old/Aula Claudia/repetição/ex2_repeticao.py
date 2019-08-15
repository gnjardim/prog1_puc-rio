
def montanteFinal(valor,juros,qtMes):
    mes=1
    while mes<=qtMes:
        if mes%3==0:
            juros=juros+juros*0.002
        if mes%2==0:
            juros=juros+juros*0.02        
        print('Mês %d) '%(mes),end=' ')
        print('Taxa de juros utilizada: %.3f%%'%(juros), end=' - ')
        if valor%13==0:
            valor=valor+1000
            print('Houve a incorporação de um prêmio de R$1000,00.', end= ' - ')
        valor=valor+valor*juros
        print('Montante reajustado: R$%.2f'%(valor))
        mes+=1

valor=float(input('Valor inicial a ser aplicado: '))
jurosIni=float(input('Percentual da taxa de juros inicial: '))
juros=jurosIni/100
qtMes=int(input('Aplicar quantos meses? '))
montanteFinal(valor,juros,qtMes)
