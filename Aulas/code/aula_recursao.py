def ExibeVertical(num):
    if num < 10:
        print(num)
        
    else:
        ExibeVertical(num//10)
        print(num%10)
        
    return


def ContaAlgarismo(num):
    if num < 10:
        return 1

    qt = ContaAlgarismo(num//10)
    return 1 + qt 


def ContaAlg2(num):
    if num < 10:
        if num == 2:
            return 1

        else:
            return 0

    if num%10 == 2:
        qt = 1 + ContaAlg2(num//10)

    else:    
        qt = ContaAlg2(num//10)
        
    return qt 


def TemAlg2(num):
    if num < 10:
        if num == 2:
            return True

        else:
            return False

    else:
        if num%10 == 2:
            qt = True

        else:    
            qt = TemAlg2(num//10)  

    return qt


def MenorAlg(num):
    if num < 10:
        return num

    else:
        menor = MenorAlg(num//10)
        
        if num%10 < menor:
            menor = num%10    

    return menor
            
        

        
        










        


    
