
def Horario(minutos):
    h=minutos//60
    m=minutos%60
    return str(h)+'h'+str(m)+'min'

def percentual(tempoReuniao,tempoProjeto):
    return tempoReuniao/(tempoReuniao+tempoProjeto)*100

def exibir(dep,reuniao,projeto):
    percent=percentual(reuniao,projeto)
    print('Dep:%s Tempo em reunião:%dh:%dmin Em projeto:%dh:%dmin %.2f%% em reunião'\
          %(dep,reuniao//60,reuniao%60,projeto//60,projeto%60,percent))
    return
        

print('Maria tem %.2f anos e nasceu em %s'%(20,'agosto'))
dep=input('Dep?')
reuniao=int(input('quanto tempo (em minutos) você esteve em reunião?'))
projeto=int(input('quanto tempo você esteve em projeto?'))
exibir(dep,reuniao,projeto)

