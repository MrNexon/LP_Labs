def more_10_sum(s: list):
    r = 0
    for el in s:
        r += (el > 10) * el
    return r


def in_1_10_sum(s: list):
    r = 0
    for el in s:
        r += (1 <= el <= 10) * el
    return r


def less_10_multi(s: list):
    r = 1
    for el in s:
        if el < 10:
            r *= el
    return r


s = []
i = 0

while True:
    c = input('S({0}): '.format(i))
    if c == '':
        break

    s += [int(c)]
    i += 1

print('Сумма больше 10:', more_10_sum(s))
print('Сумма от 1 до 10:', in_1_10_sum(s))
print('Произведение меньше 10:', less_10_multi(s))
