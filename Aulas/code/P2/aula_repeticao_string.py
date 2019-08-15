def eh_reversa(s1, s2):
    if len(s1) != len(s2):
        return False

    ini = 0
    fim = -1
    
    while ini < len(s1):
        if s1[ini] != s2[fim]:
            return False

        ini += 1
        fim -= 1

    return True
        

