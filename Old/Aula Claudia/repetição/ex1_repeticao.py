def partidas(time1,gol1,time2,gol2):
    if gol1>gol2:
        print('Time vencedor foi o ',time1)
        return False
    elif gol1<gol2:
        print('Time vencedor foi o ',time2)
        return False
    else:
        print("Empate")
        return True
numeroDeJogos = 0
numeroDeJogosEmpatados = 0
gol=0
media = 0
n = int(input("Quantas partidas tiveram?"))
while numeroDeJogos<n:
    time1 = str(input("Qual o nome do time 1?"))
    time2 = str(input("Qual o nome do time 2?"))
    gols1 = int(input("Quantos gols o time 1 fez?"))
    gols2 = int(input("Quantos gols o time 2 fez?"))
    deuEmpate = partidas(time1,gols1,time2,gols2)
    if deuEmpate:
        numeroDeJogosEmpatados += 1
    numeroDeJogos+=1
    gols = gols1+gols2 + gols
print("O total de jogos empatados foi %d"%numeroDeJogosEmpatados)
print("O total de gols foi %d"%gols)
print("A media de gols foi %d"%(gols/n))

    
    
