import PySimpleGUI as sg


class Library:
    def __init__(self, books):
        self.books = books

    def find_by_writer(self, writer):
        return list(filter(lambda x: x.writer == writer, self.books))

    def find_by_year(self, year):
        return list(filter(lambda x: x.year == year, self.books))

    def add(self, book):
        self.books.append(book)

    def remove(self, book):
        self.books.remove(book)

    def sort_by_writer(self):
        self.books.sort(key=lambda x: x.writer)

    def sort_by_year(self):
        self.books.sort(key=lambda x: x.year)


class Book:
    def __init__(self, writer, name, year):
        self.writer = writer
        self.name = name
        self.year = year


l = Library([
    Book("Толстой", "Война и Мир", "1863"),
    Book("Пушкин", "Капитанкая дочка", "1841"),
    Book("Толстой", "Анна Каренина", "1878")
])


def Launcher():
    form = sg.FlexForm('Lab13')

    layout = [
        [sg.Output(size=(88, 20))],
        [sg.ReadFormButton('Вывод')],
        [sg.Text('Поиск по писателю'), sg.InputText(), sg.ReadFormButton('Поиск писателя')], #0
        [sg.Text('Поиск по году'), sg.InputText(), sg.ReadFormButton('Поиск года')], #1
        [sg.Text('Добавить книгу'), sg.InputText(), sg.InputText(), sg.InputText(), sg.ReadFormButton('Добавить')], #2, 3, 4
        [sg.ReadFormButton('Сортировать по писателю')],
        [sg.ReadFormButton('Сортировать по году')]
    ]

    form.Layout(layout)

    while True:
        (button, value) = form.Read()
        if button == sg.WIN_CLOSED:
            break

        if button == 'Вывод':
            for i in l.books:
                print(i.writer, i.name, i.year)
            print('-' * 20)
        elif button == 'Поиск писателя':
            for i in l.find_by_writer(value[0]):
                print(i.writer, i.name, i.year)
            print('-' * 20)
        elif button == 'Поиск года':
            for i in l.find_by_year(value[1]):
                print(i.writer, i.name, i.year)
            print('-' * 20)
        elif button == 'Добавить':
            l.add(Book(value[2], value[3], value[4]))
            for i in l.books:
                print(i.writer, i.name, i.year)
            print('-' * 20)
        elif button == 'Сортировать по писателю':
            l.sort_by_writer()
            for i in l.books:
                print(i.writer, i.name, i.year)

            print('-' * 20)
        elif button == 'Сортировать по году':
            l.sort_by_year()
            for i in l.books:
                print(i.writer, i.name, i.year)

            print('-' * 20)


Launcher()