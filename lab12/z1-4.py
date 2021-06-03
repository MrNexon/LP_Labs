import sqlite3
import tkinter as tk
from tkinter import ttk

from prettytable import PrettyTable

conn = sqlite3.connect("data.db")
cursor = conn.cursor()


def z1():
    return {
        'header': ['id', 'Название', 'Часов лекций', 'Часов практических', 'Курсовая работа', 'Форма контроля'],
        'data': cursor.execute("""SELECT * FROM discipline WHERE control_form = 'Экзамен' AND coursework = true""")
    }


def z2():
    res = cursor.execute("""SELECT department.*, count(department_discipline.department_id)
FROM department_discipline JOIN department on department.id = department_discipline.department_id
GROUP BY department_discipline.department_id""")
    d = []
    for i in res:
        if i[3] > 5:
            d += i
    return {
        'header': ['id', 'Название', 'Количество преподователей', 'Количество дисциплин'],
        'data': [d]
    }


def z3():
    return {
        'header': ['id', 'Название', 'Количество преподователей'],
        'data': cursor.execute("""SELECT * FROM department WHERE id >= 10 and id <= 20""")
    }


def drawTable(data_dict):
    print(data_dict)
    label.config(state=tk.NORMAL)
    label.delete(1.0, tk.END)

    tableData = PrettyTable()
    tableData.field_names = data_dict['header']

    for i in data_dict['data']:
        tableData.add_row(i)

    label.insert(1.0, tableData)
    label.config(state=tk.DISABLED)


root = tk.Tk()
root.title('Лабораторная работа 12')
root.configure(bg='grey85')

s = ttk.Style()
s.theme_use('classic')

label = tk.Text(root, width=150)
label.pack()

ttk.Button(root, text='Задание 1', command=lambda: drawTable(z1())).pack()
ttk.Button(root, text='Задание 2', command=lambda: drawTable(z2())).pack()
ttk.Button(root, text='Задание 3', command=lambda: drawTable(z3())).pack()

root.mainloop()
