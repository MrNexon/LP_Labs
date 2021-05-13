my_len = [
    [
        'БО - 331101',
        [
            'Акулова Алена',
            'Бабушкина Ксения'
        ]
    ],
    [
        'ОБ - 331102',
        [
            'Акулова Алена',
            'Бабушкина Ксения',
        ]
    ]
]


def var3(l: list):
    for i in l:
        print(i[0])
        for j in i[1]:
            print('\t', j)


def var2(l: list):
    for i in l:
        if i[0] == 'БО - 331101':
            print('{0}:'.format(i[0]), end=' ')
            print(*i[1], sep=', ')


def var1(l: list):
    for i in l:
        if i[0] == 'БО - 331101':
            print(i[0])
            for j in i[1]:
                print('\t', j)


def var4(l: list):
    for i in l:
        if i[0][0:2] == 'БО':
            print('{0}:'.format(i[0]), end=' ')
            print(*i[1], sep=', ')


print('-----------------')
var1(my_len)

print('-----------------')
var2(my_len)

print('-----------------')
var3(my_len)

print('-----------------')
var4(my_len)
