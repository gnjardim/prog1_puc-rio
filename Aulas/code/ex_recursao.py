'''
# 1
def RecursaoQuad():
    nums = 1000
    while nums < 10000:
        if (nums//100 + nums%100)**2 == nums:
            print(nums)
        nums += 1
    return
    
RecursaoQuad()
'''
'''
# 2
def DivNum(n1, n2):
    if n1 > n2:
        t = n1
        w = n2
        n2 = t
    
    while n1 < n2:
        div = n1//10
        if n1%10 != 0 and n1%div == 0:
            print(n1)
        n1 += 1
    return

DivNum(10, 99)
'''
# 3
def RetornaGrupo(n_questoes, q_sim):
    if q_sim/n_questoes > 2/3:
        grupo = "pró"
        
    elif q_sim/n_questoes < 1/3:
        grupo = "contra"
        
    else:
        grupo = "neutro"
    print("Seu grupo é: %s" % grupo)
    return 

def CapRespostas(n_questoes):
    cont = 0
    q_sim = 0
    
    while cont < n_questoes:
        resp = input("Questão %d: s ou n? " % cont)

        if resp == 's':
            q_sim += 1
            
        cont += 1
    return q_sim

quant = int(input("Quantas perguntas? "))
cont = 0
while cont < 400:
    matricula = input("Qual sua matrícula: ")
    q_sim = CapRespostas(quant)
    print("Aluno: %s" % matricula)
    RetornaGrupo(n_questoes, q_sim)
    cont += 1
        
            
        
    
