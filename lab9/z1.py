from tkinter import ttk

import tkinter as tk

from prettytable import PrettyTable

data_dict = {
    1: ['Беляков Ефим Свястославович', 18, 'ВКБ13'],
    2: ['Курдус Аким Юрьевич', 18, 'ВКБ12'],
    3: ['Жинкин Даниил Романович', 21, 'ВКБ11'],
    4: ['Боруля Максим Сергеевич', 15, 'ВКБ12'],
}

tableData = PrettyTable()
tableData.field_names = ['№', 'ФИО', 'Возраст', 'Группа']


def addUser():
    data_dict[int(id.get())] = [fio.get(), age.get(), group.get()]
    return data_dict


def updateUser():
    data_dict[int(id.get())] = [fio.get(), age.get(), group.get()]
    return data_dict


def deleteUser():
    data_dict.pop(int(id.get()))
    return data_dict


def getUser():
    return {int(id.get()): data_dict[int(id.get())]}


root = tk.Tk()
root.title('Лабораторная работа 9')
root.configure(bg='grey85')

s = ttk.Style()
s.theme_use('classic')

label = tk.Text(root, width=92)
label.pack()


def drawTable(dd):
    tableData.clear_rows()
    print(dd)
    for i in dd:
        user = dd[i]
        tableData.add_row([i, user[0], user[1], user[2]])
    label.delete(1.0, tk.END)
    label.insert(1.0, tableData)



id = tk.StringVar()
fio = tk.StringVar()
age = tk.StringVar()
group = tk.StringVar()

restFrame = ttk.Frame(root)
ttk.Entry(restFrame, width=5, textvariable=id).grid(column=0, row=0)
ttk.Entry(restFrame, textvariable=fio).grid(column=1, row=0)
ttk.Entry(restFrame, width=10, textvariable=age).grid(column=2, row=0)
ttk.Entry(restFrame, width=15, textvariable=group).grid(column=3, row=0)
ttk.Button(restFrame, text='Создать', command=lambda: drawTable(addUser())).grid(column=6, row=0)
ttk.Button(restFrame, text='Обновить', command=lambda: drawTable(updateUser())).grid(column=7, row=0)
ttk.Button(restFrame, text='Удалить', command=lambda: drawTable(deleteUser())).grid(column=8, row=0)
ttk.Button(restFrame, text='Выбрать', command=lambda: drawTable(getUser())).grid(column=9, row=0)
restFrame.pack()

drawTable(data_dict)

root.mainloop()
