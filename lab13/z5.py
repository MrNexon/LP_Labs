import PySimpleGUI as sg


class Buyer:
    def __init__(self, name, street, card, number):
        self.name = name
        self.street = street
        self.card = card
        self.number = number

    def set_name(self, name):
        self.name = name

    def set_street(self, street):
        self.street = street

    def set_card(self, card):
        self.card = card

    def set_number(self, number):
        self.number = number

    def get_name(self):
        return self.name

    def get_street(self):
        return self.street

    def get_card(self):
        return self.card

    def get_number(self):
        return int(self.number)

    def print(self):
        print(self.name, self.street, self.card, self.number)


s = [
    Buyer("Иванов Иван Иванович", "Ленина", "2288000045678965", "147852"),
    Buyer("Сидоров Сидр Сидорович", "Ларина", "1332000012345652", "369852"),
    Buyer("Андропов Антон Андропович", "Нагибина", "4569000085218523", "78964123")
]


def Launcher():
    form = sg.FlexForm('Lab13')

    layout = [
        [sg.Output(size=(88, 20))],
        [sg.ReadFormButton('Вывод'), sg.ReadFormButton('Сортировать')],
        [sg.Text('Диапазон'), sg.InputText(), sg.InputText(), sg.ReadFormButton('Вывод по диапазону')],
    ]

    form.Layout(layout)

    while True:
        (button, value) = form.Read()
        if button == sg.WIN_CLOSED:
            break

        if button == 'Вывод':
            for i in s:
                i.print()
            print('-' * 20)
        elif button == 'Сортировать':
            s.sort(key=lambda x: x.get_name())
            for i in s:
                i.print()
            print('-' * 20)
        elif button == 'Вывод по диапазону':
            a = int(value[0])
            b = int(value[1])
            for i in s:
                if a < i.get_number() < b:
                    i.print()
            print('-' * 20)


Launcher()
