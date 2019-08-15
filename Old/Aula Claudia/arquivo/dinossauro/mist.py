import turtle
pat = turtle.Turtle()
arq = open("misterio.txt","r")
for linha in arq:
  linha = linha.strip() # para tirar o newline
  if linha == "CIMA":
    pat.up()
  elif linha == "BAIXO":
    pat.down()
  else:
    posicao = linha.find(" ")
    x = int(linha[:posicao])
    y = int(linha[posicao+1:])
    pat.goto(x,y)
pat.hideturtle()
