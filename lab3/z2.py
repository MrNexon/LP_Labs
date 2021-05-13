def var1(t: list):
    for i in range(0, len(t)):
        if i == 0:
            print('{0:30}\t{1:20}\t{2:15}'.format(t[i][0] + t[i][1] + t[i][2], t[i][4], t[i][3]))
        else:
            print('{0:30}\t{1:20}\t{2:15}'.format(
                '{0} {1} {2}'.format(
                    t[i][0],
                    t[i][1],
                    t[i][2]
                ),
                t[i][4],
                t[i][3])
            )


def var2(t: list):
    for i in range(0, len(t)):
        if i == 0:
            print('{0:30}\t{1:20}\t{2:15}'.format(t[i][0] + t[i][1] + t[i][2], t[i][3], t[i][4]))
        else:
            print('{0:30}\t{1:20}\t{2:15}'.format('{0} {1} {2}'.format(t[i][0], t[i][1], t[i][2]), t[i][3], t[i][4]))


def var3(t: list):
    for i in range(0, len(t)):
        if i == 0:
            print('{0:10}\t{1:10}\t{2:10}\t{3:^30}'.format(t[i][0], t[i][1], t[i][2], 'О студенте'))
        else:
            print('{0:10}\t{1:10}\t{2:10}\t{3:^30}'.format(t[i][0], t[i][1], t[i][2],
                                                           '{0}, {1}'.format(t[i][4], t[i][3])))


def var4(t: list):
    for i in range(0, len(t)):
        if i == 0:
            print('{0:30}\t{1:^30}'.format(t[i][0] + t[i][1] + t[i][2], 'О студенте'))
        else:
            print('{0:30}\t{1:^30}'.format('{0} {1} {2}'.format(t[i][0], t[i][1], t[i][2]),
                                           '{0}, {1}'.format(t[i][4], t[i][3])))


table = []
s = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'
table = s.split(';_')

for i in range(0, len(table)):
    table[i] = table[i].split(';')

var1(table)
var2(table)
var3(table)
var4(table)

#print('help me. He wil kill me, if i gonna tell you about this mistakes')
