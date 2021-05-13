st = input('Строка: ')

def st_number(s: str):
    ret = ''
    for i in [*s]:
        if 48 <= ord(i) < 57:
            ret += i
    return ret


def st_string(s: str):
    ret = ''
    for i in [*s]:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 1040 <= ord(i) <= 1071 or 1072 <= ord(i) <= 1103:
            ret += i
    return ret


def st_l(s: str):
    ret = ''
    for i in [*s]:
        if i == 'Л':
            ret += i
    return ret


print(st_number(st))
print(st_string(st))
print(st_l(st))
print('--------------------')
print(st_number(st))
print(st_string(st))