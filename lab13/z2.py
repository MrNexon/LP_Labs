import PySimpleGUI as sg


class Train:
    def __init__(self, way, number, time):
        self.way = way
        self.number = number
        self.time = time


s = [
    Train("Moscow", "4231", "10:00"),
    Train("Rostov-on-Don", "6543", "11:35"),
    Train("Kislovodsk", "1364", "16:40"),
    Train("Krasnodar", "7895", "6:14"),
    Train("Vladivostok", "6546", "22:59")
]


def Launcher():
    form = sg.FlexForm('Lab13')

    layout = [
        [sg.Output(size=(88, 20))],
        [sg.ReadFormButton('Вывод всех')],
        [sg.ReadFormButton('Сортировать по номерам')],
        [sg.Text('Номер поезда'), sg.InputText(), sg.ReadFormButton('Вывод')],
        [sg.ReadFormButton('Сортировать по пункту назначения')]
    ]

    form.Layout(layout)

    while True:
        (button, value) = form.Read()
        if button == sg.WIN_CLOSED:
            break

        if button == 'Вывод всех':
            for i in s:
                print(i.way, i.number, i.time)
            print('-' * 20)
        elif button == 'Сортировать по номерам':
            s.sort(key=lambda x: x.number)
            for i in s:
                print(i.way, i.number, i.time)
            print('-' * 20)
        elif button == 'Вывод':
            for i in s:
                if value[0] == i.number:
                    print(i.way, i.number, i.time)

            s.sort(key=lambda x: x.way + x.time)
            print('-' * 20)
        elif button == 'Сортировать по пункту назначения':
            s.sort(key=lambda x: x.way + x.time)
            for i in s:
                print(i.way, i.number, i.time)
            print('-' * 20)


Launcher()