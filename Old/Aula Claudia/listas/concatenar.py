def concatenar(l):
    frase=' '
    for el in l:
        if type(el)==list:
            frase+=concatenar(el)
        else:
            frase+=el+' '
    return frase

Ls=['oi',['estamos','aprendendo','a trabalhar'],'com','lista',['de','string']]
print(concatenar(Ls))
