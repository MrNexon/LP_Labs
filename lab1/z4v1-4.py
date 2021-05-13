def s_max(s: list):
    return max(s)


def s_min(s: list):
    return min(s)


def s_average(s: list):
    sum = 0
    for i in s:
        sum += i

    return sum / len(s)


def s_medium(s: list):
    i = len(s) // 2
    return s[i]


s = []
i = 0

while True:
    c = input('S({0}): '.format(i))
    if c == '':
        break

    s += [int(c)]
    i += 1

print('Максимальное: ', s_max(s))
print('Минимальное: ', s_min(s))
print('Среднее арифметическое: ', s_average(s))
print('Посеридине: ', s_medium(s))