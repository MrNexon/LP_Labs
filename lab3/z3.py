import re


def var1(l: list):
    for i in range(0, len(l)):
        if i == 0:
            print('{:30}\t{:10}\t{:20}'.format(l[i][0], l[i][1], l[i][2]))
        else:
            if re.match(r'^Петров', l[i][0]):
                print('{:30}\t{:10}\t{:20}'.format(l[i][0], l[i][1], l[i][2]))


def var2(l: list):
    for i in range(0, len(l)):
        if i == 0:
            print('{:30}\t{:10}\t{:20}'.format(l[i][0], l[i][1], l[i][2]))
        else:
            if re.match(r'^21', l[i][1]):
                print('{:30}\t{:10}\t{:20}'.format(l[i][0], l[i][1], l[i][2]))


def var3(l: list):
    for i in range(0, len(l)):
        if i == 0:
            print('{:30}\t{:10}\t{:20}'.format(l[i][0], l[i][1], l[i][2]))
        else:
            match = re.match(r'^\d+', l[i][1])
            if match and int(match[0]) > 21:
                print('{:30}\t{:10}\t{:20}'.format(l[i][0], l[i][1], l[i][2]))


def var4(l: list):
    for i in range(0, len(l)):
        if i == 0:
            print('{:30}\t{:10}\t{:20}'.format(l[i][0], l[i][1], l[i][2]))
        else:
            if re.match(r'^А|Б', l[i][0]):
                print('{:30}\t{:10}\t{:20}'.format(l[i][0], l[i][1], l[i][2]))


table = []
s = 'ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса'
table = s.split(';_')

for i in range(0, len(table)):
    table[i] = table[i].split(';')

print(table)

var1(table)
print('-----------------------------------')
var2(table)
print('-----------------------------------')
var3(table)
print('-----------------------------------')
var4(table)
print('-----------------------------------')
