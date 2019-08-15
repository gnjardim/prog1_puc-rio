### 1
def areaRetangulo(lado1, lado2):
    return lado1*lado2

def hipotenusa(cateto1, cateto2):
    return (cateto1**2 + cateto2**2)**(1/2)

def areaTotal(a, b, c, d, e):
    area1 = areaRetangulo(a, b)
    area2 = areaRetangulo(c, d)

    area_triangulo = (areaRetangulo(a, d))/2
    hip = hipotenusa(a, d)

    area3 = areaRetangulo(e, hip)

    print("-- Área retângulos: %.2f, %.2f, %.2f -- Área triângulo: %.2f"
          % (area1, area2, area3, area_triangulo))
    return
'''
a_in = float(input("Lado A: "))
b_in = float(input("Lado B: "))
c_in = float(input("Lado C: "))
d_in = float(input("Lado D: "))
e_in = float(input("Lado E: "))

areaTotal(a_in, b_in, c_in, d_in, e_in)
'''


### 2
def descobre_x(ano):
    if ano >= 1900 and ano <=2199:
        x = 24

    elif ano >= 2200 and ano <= 2299:
        x = 25
        
    return x

def descobre_y(ano):
    if ano >= 1900 and ano <=2099:
        y = 5

    elif ano >= 2100 and ano <= 2199:
        y = 6

    elif ano >= 2200 and ano <= 2299:
        y = 7
               
    return y

def exibe_dia_mes(ano):
    a = ano%19
    b = ano%4
    c = ano%7

    x = descobre_x(ano)
    y = descobre_y(ano)

    d = (19*a + x)%30
    e = (2*b + 4*c + 6*d + y)%7

    if (d+e) > 9:
        dia = d + e - 9
        mes = 4

    elif (d+e) <= 9:
        dia = d + e + 22
        mes = 3

    if mes == 4 and dia == 26:
        dia = 19

    if mes == 4 and dia == 25 and d == 28 and a > 10:
        dia = 18

    print("%d/%d" % (dia, mes))
    return


### 4
def ConcatInv(string1, string2):
    return string1[1:] + string2[:0:-1]


### 5
def ConcatAleat(string1):
    rep = string1[0:2] + string1[len(string1)-1:len(string1)-3:-1]
    return string1+(rep*4)


### 6
def desconto_padrao(tarifa, q_inteiras):
    if q_inteiras <= 2:
        desconto = q_inteiras*tarifa*0.1

    elif q_inteiras <= 5:
        desconto = q_inteiras*tarifa*0.15

    else:
        desconto = q_inteiras*tarifa*0.2

    return desconto

def desconto_fidelidade(q_meia, q_inteiras):
    if 2*q_inteiras == q_meia:
        desconto = 200

    elif q_inteiras <= q_meia or q_inteiras > q_meia:
        desconto = 100

    return desconto

def desconto_passagens(tarifa, tipo_cliente, q_inteiras, q_meia):
    desconto_p = desconto_padrao(tarifa, q_inteiras)

    if tipo_cliente == "f":
        desconto_f = desconto_fidelidade(q_meia, q_inteiras)

    else:
        desconto_f = 0

    subtotal = tarifa*q_inteiras + (tarifa/2)*q_meia
    desconto_total = desconto_p + desconto_f
    total = subtotal - desconto_total

    print("Desconto: %.2f, Total a pagar: %.2f" % (desconto_total, total))
    return

### 7
def ExibeVert(num):
    if num < 10:
        print(num)

    else:
        ExibeVert(num//10)
        print(num)
        
    return


### 8
def ConcatStringP(s1, s2):
    if s1 == '':
        return '' + s2

    if s2 == '':
        return '' + s1
        
    else:
        return s1[0] + s2[0] + ConcatStringP(s1[1:], s2[1:])

    
### 10
def RepString(s):
    if s == '':
        return ''

    if s[0] in '1234567890':
        return 2*s[0] + RepString(s[1:])

    else:
        return s[0] + RepString(s[1:])
        

### 12
def PrefixString(s1, s2):
    if s1 == '':
        return False

    if s1[0] == s2[0]:
        prf = True

    else:
        prf = False

    prf = PrefixString(s1[1:], s2[1:])
    return prf
        













