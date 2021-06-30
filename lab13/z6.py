import PySimpleGUI as sg


class Sub:
    def __init__(self, id, name, address, number, debit, credit, time_city, time_no_city):
        self.id = id
        self.name = name
        self.address = address
        self.number = number
        self.debit = debit
        self.credit = credit
        self.time_city = time_city
        self.time_no_city = time_no_city

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_number(self, number):
        self.number = number

    def set_debit(self, debit):
        self.debit = debit

    def set_credit(self, credit):
        self.credit = credit

    def set_time_city(self, time):
        self.time_city = time

    def set_time_no_city(self, time):
        self.time_no_city = time

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_number(self):
        return int(self.number)

    def get_debit(self):
        return int(self.debit)

    def get_credit(self):
        return int(self.credit)

    def get_time_city(self):
        return int(self.time_city)

    def get_time_no_city(self):
        return int(self.time_no_city)

    def print(self):
        print(self.id, self.name, self.address, self.number, self.debit, self.credit, self.time_city, self.time_no_city)


s = [
    Sub("01", "Andrey", "Lenina", "741258", "123", "1500", "3", "0"),
    Sub("02", "Ivan", "Nagibina", "369852", "799", "456", "0", "7"),
    Sub("03", "Sasha", "Larina", "456321", "741", "8000", "2", "1"),
]


def Launcher():
    form = sg.FlexForm('Lab13')

    layout = [
        [sg.Output(size=(88, 20))],
        [sg.ReadFormButton('Вывод'), sg.ReadFormButton('Пользовались междугородной связью'), sg.ReadFormButton('В алфавитном')],
        [sg.Text('Время городских переговоров >'), sg.InputText(), sg.ReadFormButton('Вывод по времени городских переговоров')],
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
        elif button == 'Пользовались междугородной связью':
            for i in s:
                if i.get_time_no_city() > 0:
                    i.print()

            print('-' * 20)
        elif button == 'В алфавитном':
            s.sort(key=lambda x: x.name)
            for i in s:
                i.print()
            print('-' * 20)
        elif button == 'Вывод по времени городских переговоров':
            a = int(value[0])
            for i in s:
                if i.get_time_city() > a:
                    i.print()

            print('-' * 20)


Launcher()
