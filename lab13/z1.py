import PySimpleGUI as sg


class Student:
    def __init__(self, fio, group, progress):
        self.fio = fio
        self.group = group
        self.progress = progress

    def middle(self):
        return sum([(i + 1) * self.progress[i] for i in range(len(self.progress))]) / sum(self.progress)


s = [
    Student("Аргишев тимур ", "ВКБ-13", [0, 0, 1, 2, 3]),
    Student("Боруля Максим ", "ВКБ-13", [1, 0, 3, 2, 1]),
    Student("Беляков Ефим ", "ВКБ-13", [0, 0, 1, 4, 2]),
    Student("Курдус Аким", "ВКБ-13", [0, 0, 0, 5, 0]),
    Student("Ивахненко Юля", "ВКБ-13", [0, 1, 6, 2, 0]),
    Student("Журилко Григорий", "ВКБ-13", [0, 0, 1, 4, 5]),
    Student("Малышев Владислав", "ВКБ-13", [0, 0, 8, 4, 3]),
    Student("Петренко Данил", "ВКБ-13", [0, 0, 0, 0, 6]),
    Student("Жинкин Даниил", "ВКБ-13", [0, 2, 0, 4, 1]),
    Student("Шепило Алина", "ВКБ-13", [0, 0, 1, 7, 3])
]


def Launcher():
    form = sg.FlexForm('Lab13')

    layout = [
        [sg.Output(size=(88, 20))],
        [sg.ReadFormButton('Вывод всех'), sg.ReadFormButton('По возрастанию балла'), sg.ReadFormButton('Только 4 5')]
    ]

    form.Layout(layout)

    while True:
        (button, value) = form.Read()
        if button == sg.WIN_CLOSED:
            break

        if button == 'Вывод всех':
            for i in s:
                print(i.fio, i.group, i.progress, i.middle())
            print('-' * 20)
        elif button == 'По возрастанию балла':
            s.sort(key=lambda x: x.middle())
            for i in s:
                print(i.fio, i.group, i.progress, i.middle())
            print('-' * 20)
        elif button == 'Только 4 5':
            for i in s:
                if i.progress[0] == 0 and i.progress[1] == 0 and i.progress[2] == 0:
                    print(i.fio, i.group, i.progress, i.middle())
            print('-' * 20)


Launcher()
