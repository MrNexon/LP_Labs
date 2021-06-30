import PySimpleGUI as sg


class Simple:
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def print(self):
        print(self.one, self.two)

    def change1(self, new):
        self.one = new

    def change2(self, new):
        self.two = new

    def sum(self):
        return self.one + self.two

    def more(self):
        return max(self.one, self.two)


s = Simple(1, 3)


def Launcher():
    form = sg.FlexForm('Lab13')

    layout = [
        [sg.Output(size=(88, 20))],
        [sg.ReadFormButton('Вывод'), sg.ReadFormButton('Сумма'), sg.ReadFormButton('Макс')]
    ]

    form.Layout(layout)

    while True:
        (button, value) = form.Read()
        if button == sg.WIN_CLOSED:
            break

        if button == 'Вывод':
            s.print()
            print('-' * 20)
        elif button == 'Сумма':
            print(s.sum())
            print('-' * 20)
        elif button == 'Макс':
            print(s.more())
            print('-' * 20)


Launcher()
