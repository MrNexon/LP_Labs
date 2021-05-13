def even_i(s: list, even: bool):
    l = []
    for i in range(not even, len(s), 2):
        l += [s[i]]

    return l

s = []
i = 0

while True:
    c = input('S({0}): '.format(i))
    if c == '':
        break

    s += [c]
    i += 1
print('-----------------------------')
print(*even_i(s, True), sep='\n')
print('-----------------------------')
print(*even_i(s, False), sep='\n')
print('-----------------------------')
print(*even_i(s, True), sep=', ')
print('-----------------------------')
print(*even_i(s, False), sep=', ')
