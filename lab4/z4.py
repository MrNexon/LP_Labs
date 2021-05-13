my_len = [['БО - 331101', ['Акулов Алена', 'Бабушкина Ксения']],
          ['БО - 331101', ['Акулова Алена', 'Пабушкина Асения']]]


def var1(l: list):
    for i in l:
        print(i[0])
        for j in i[1]:
            if j[0] == 'А':
                print('\t', j)


def var2(l: list):
    for i in l:
        print(i[0])
        for j in i[1]:
            if len(j.split(' ')[0]) < 7:
                print('\t', j)


def var3(l: list):
    for i in l:
        print(i[0])
        for j in i[1]:
            f, n = j.split(' ')
            if f[0] == 'П' and n[0] == 'А':
                print('\t', j)


def var4(l: list):
    for i in l:
        print(i[0])
        for j in i[1][::2]:
            print('\t', j)


print('-----------------')
var1(my_len)
print('-----------------')
var2(my_len)
print('-----------------')
var3(my_len)
print('-----------------')
var4(my_len)
