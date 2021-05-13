st = input('Строка: ')


def st_number(s: str):
    ret = ''
    for i in [*s]:
        try:
            j = int(i)
            ret += str(j)
        except ValueError:
            continue
    return ret


def st_string(s: str):
    ret = ''
    for i in [*s]:
        try:
            int(i)
            continue
        except ValueError:
            ret += i
    return ret


def st_l(s: str):
    ret = ''
    for i in [*s]:
        try:
            int(i)
            continue
        except ValueError:
            if i == 'Л':
                ret += i
    return ret


print(st_number(st))
print(st_string(st))
print(st_l(st))
print('--------------------')
print(st_number(st))
print(st_string(st))