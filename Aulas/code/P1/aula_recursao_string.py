'''
def ContaMaiuscula(s):
    if s == '':
        return 0

    if 'A' <= s[0] <= 'Z':
        return 1 + ContaMaiuscula(s[1:])
    else:
        return ContaMaiuscula(s[1:])

def ExibeVertical(s):
    if s == '':
        return

    print(s[0])
    ExibeVertical(s[1:])
    return

def RepCaract(s):
    if s == '':
        return ''

    return 2*s[0] + RepCaract(s[1:])   


def RepVogal(s):
    if s == '':
        return ''

    if s[0] in 'aeiouAEIOU':
        ns = 2*s[0] + RepVogal(s[1:])
    else:
        ns = s[0] + RepVogal(s[1:])
    return ns


def SubEspaco(s):
    if s == '':
        return ''

    if s[0] == ' ':
        ns = '#' + SubEspaco(s[1:])
    else:
        ns = s[0] + SubEspaco(s[1:])
    return ns


def String2em1(s1, s2):
    if s1 == '':
        return 0

    if s1[:len(s2)] == s2:
        return 1 + String2em1(s1[1:], s2)
    else:
        return String2em1(s1[1:], s2)
'''

def StringEmPos(s1, k):
    if s1 == '':
        return 0

    if 'c' in s1[k:]:
        return 1 + StringEmPos(s1[1:], k)
    else:
        return StringEmPos(s1[1:], k)









