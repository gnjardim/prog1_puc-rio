'''
Lstrings = ['Oi', ['estamos', 'aprendendo', 'a trabalhar'], 'com', 'listas', ['de', 'strings']]

# 1
def ConcatLista(l):
    s = ''
    for el in l:
        if type(el) is list:
            s += ConcatLista(el)
            
        else:
            s += el
            
    return s

# 3
def MaiorLista(l):
    maior = ''
    for el in l:
        if type(el) is list:
            m = MaiorLista(el)
            if len(m) > len(maior):
                maior = m
                        
        else:
            if len(el) > len(maior):
                maior = el
                
    return maior

# 4
def NPalavras(l):
    n = 0
    for el in l:
        if type(el) is list:
            n += NPalavras(el)

        else:
            n += 1
            if ' ' in el:
                n += 1

    return n

# 5
def MaiusculaLista(l):
    for (i, el) in enumerate(l):
        if type(el) is list:
            MaiusculaLista(el)

        else:
            l[i] = el.upper()

    return
'''
# ---------------------------------------------
lista = ['q', 'q', 'q', 2, 3, 'q', 'q', 'q']

s = [1]*3
lista[:3] = s
lista[-1:-4:-1] = s

# ---------------------------------------------
string = 'quantas vezes a palavra será replicada?'

def RepString(st):
    
    lista_string = st.split()
    tam = len(lista_string)
    rep = lista_string[(tam//2):(tam//2 + 1)]*tam

    nova_string = ' '.join(lista_string[:tam//2]) + ' ' + ' '.join(rep) + ' ' + ' '.join(lista_string[tam//2+1:])

    return nova_string

