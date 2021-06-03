import tkinter as tk
from tkinter import ttk

root = tk.Tk()  # Создаем окно
root.title('Лабораторная работа 7 | Задание 1')  # Задаем окну заголовок
root.configure(bg='grey85')  # BackGround

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=6)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

s = ttk.Style()
s.theme_use('classic')

ttk.Label(root, text="Словарь:").grid(column=0, row=0, sticky=tk.NW)

tableFrame = ttk.Frame(root)
tableFrame.grid(column=0, row=1, sticky=tk.EW, ipadx=10, ipady=10)
tableFrame.columnconfigure(0, weight=1)
tableFrame.columnconfigure(1, weight=1)

ttk.Label(tableFrame, text='Ключ:').grid(column=0, row=0, sticky=tk.NW, pady=10)
ttk.Label(tableFrame, text='Значение:').grid(column=1, row=0, sticky=tk.NW, pady=10)

buttonFrame = ttk.Frame(root)
buttonFrame.grid(column=0, row=2, sticky=tk.SW, ipadx=0, ipady=10)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)


def addEvent():
    global tableFrame
    last_row = len(tableFrame.children)

    row = ttk.Frame(tableFrame, name='row_{0}'.format(last_row))
    row.columnconfigure(0, weight=1)
    row.columnconfigure(1, weight=1)

    ttk.Entry(row, name='key').grid(column=0, row=0, sticky=tk.W)
    ttk.Entry(row, name='value').grid(column=1, row=0, sticky=tk.W)

    row.grid(column=0, columnspan=2, sticky=tk.EW)


def delEvent():
    global tableFrame
    last_el = len(tableFrame.children)
    tableFrame.children.get('row_{0}'.format(last_el - 1)).destroy()


def calculateEvent():
    global tableFrame, root
    count = 0
    d = {}

    for i in tableFrame.children:
        if str(i)[:3] == 'row':
            key = tableFrame.children.get(i).children.get('key').get()
            value = tableFrame.children.get(i).children.get('value').get()
            if key != '':
                d[key] = value

    print(d)
    ttk.Label(root, text='Количество ключей словаря: {0}'.format(len(d))).grid(column=0, row=3, sticky=tk.SW)


add = ttk.Button(buttonFrame, text="Добавить", command=addEvent)
delete = ttk.Button(buttonFrame, text="Удалить", command=delEvent)
calculate = ttk.Button(buttonFrame, text="Подсчитать", command=calculateEvent)

add.grid(column=0, row=0, sticky=tk.SW)
delete.grid(column=1, row=0, sticky=tk.SW)
calculate.grid(column=2, row=0, sticky=tk.SW)

root.mainloop()
