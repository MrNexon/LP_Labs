class Student:
    def __init__(self, raw: str):
        temp = raw.split(';')
        self.number = temp[0],
        self.lastName, self.firstName, self.secondName = temp[1].split(' ')
        self.age = int(temp[2])
        self.studyGroup = temp[3]


def var1(li: list):
    li.sort(key=lambda student: student.lastName)
    printInfo(li)


def var2(li: list):
    li.sort(key=lambda student: student.age)
    printInfo(li)


def var3(li: list):
    li.sort(key=lambda student: student.studyGroup)
    printInfo(li)


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


def save(li: list):
    fo = open('students.csv', 'w')
    fo.write('№;ФИО;Возраст;Группа\n')
    for i in li:
        fo.write('{0};{1};{2};{3}\n'.format(str(i.number[0]), '{0} {1} {2}'.format(i.lastName, i.firstName, i.secondName),
                                         i.age, i.studyGroup))
    fo.close()


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


def modifyAll(li: list, add: bool):
    for i in li:
        if add:
            i.age += 1
        else:
            i.age -= 1


def modifyGroup(li: list, add: bool):
    studyGroup = input('Группа: ')

    for i in li:
        if studyGroup == i.studyGroup:
            if add:
                i.age += 1
            else:
                i.age -= 1


while True:
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

    command = input('Команда: ')
    if command == 'Выход':
        break

    if command == 'Все +1':
        modifyAll(table, True)

    if command == 'Все -1':
        modifyAll(table, False)

    if command == 'Группа +1':
        modifyGroup(table, True)

    if command == 'Группа -1':
        modifyGroup(table, False)

    if command == 'Сохранить':
        save(table)
        print('Файл был успешно сохранен!')

f.close()
