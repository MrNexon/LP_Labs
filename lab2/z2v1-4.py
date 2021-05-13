def len_in_5_10(s: list):
    t = []
    for el in s:
        if 5 <= len(el) <= 10:
            t += [el]

    return t


def len_less_10(s: list):
    t = []
    for el in s:
        if len(el) < 10:
            t += [el]

    return t


def r_end_str(s: list):
    t = []
    for el in s:
        if el[len(el) - 1] == 'r':
            t += [el]

    return t


def r_start_str(s: list):
    t = []
    for el in s:
        if el[0] == 'r':
            t += [el]

    return t


s = []
i = 0

while True:
    c = input('S({0}): '.format(i))
    if c == 'end':
        break

    s += [c]
    i += 1

print('-------------------------')
print(*len_in_5_10(s), sep='\n')
print('-------------------------')
print(*len_less_10(s), sep='\n')
print('-------------------------')
print(*r_end_str(s), sep=', ')
print('-------------------------')
print(*r_start_str(s), sep=', ')