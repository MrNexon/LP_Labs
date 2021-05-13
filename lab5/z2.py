class Student:
    def __init__(self, raw: str):
        temp = raw.split(';')
        self.number = temp[0],
        self.lastName, self.firstName, self.secondName = temp[1].split(' ')
        self.age = int(temp[2])
        self.studyGroup = temp[3]


def var1(li: list):
    printInfo(sorted(li, key=lambda student: student.lastName))


def var2(li: list):
    printInfo(sorted(li, key=lambda student: student.age))


def var3(li: list):
    printInfo(sorted(li, key=lambda student: student.studyGroup))


def var4(li: list):
    r = []
    for i in li:
        if i.age > 22:
            r += [i]
    printInfo(r)


def printInfo(li: list):
    print('{0:^3}| {1:30}|{2:^15}| {3:16}'.format('№', 'ФИО', 'Возраст (Лет)', 'Группа'))
    for i in li:
        print('{0:^3}| {1:30}|{2:^15}| {3:16}'.format(str(i.number[0]),
                                                      '{0} {1} {2}'.format(i.lastName, i.firstName, i.secondName),
                                                      i.age, i.studyGroup))


f = open('students.csv', 'r')
table = []
i = 0

number = ''
fio = ''
age = ''
group = ''

for l in f:
    if i == 0:
        number, fio, age, group = l.replace('\n', '').split(';')
    else:
        table += [Student(l.replace('\n', ''))]
    i += 1

print('----------------------Исходная таблица-------------------------')
printInfo(table)
print()
print('--------------------------Вариант 1----------------------------')
var1(table)
print()
print('--------------------------Вариант 2----------------------------')
var2(table)
print()
print('--------------------------Вариант 3----------------------------')
var3(table)
print()
print('--------------------------Вариант 4----------------------------')
var4(table)
print()
