import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

last_del = 0

root = tk.Tk()
root.title('Лабораторная работа 7 | Задание 2-4')
root.configure(bg='grey85')
root.resizable(1, 1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=6)
root.rowconfigure(2, weight=1)

s = ttk.Style()
print(s.theme_names())
s.theme_use('classic')

fileControl = ttk.Frame(root)
fileControl.columnconfigure(0, weight=1)
fileControl.columnconfigure(1, weight=1)
fileControl.columnconfigure(2, weight=1)
fileControl.grid(row=1)

filePathValue = tk.StringVar()

filePath = ttk.Entry(fileControl, width=100, textvariable=filePathValue)
filePath.grid(column=0, row=0, sticky=tk.NE)

tableFrame = ttk.Frame(root)
tableFrame.grid(column=0, row=0, sticky=tk.EW, ipadx=10, ipady=10)
fileControl.columnconfigure(0, weight=1)

file = None
dict_students = {}
header = []


def openFileEvent():
    global filePathValue
    dlg = tk.filedialog.Open(filetypes=[('CSV Table', '*.csv')])
    fl = dlg.show()
    filePathValue.set(fl)


def readFile():
    global file, dict_students, header
    file = open(filePathValue.get(), "r")

    students = []
    file_data = file.read().splitlines()
    header = file_data[0].split(';')

    for raw in file_data[1:]:
        splited = raw.split(';')
        students += [splited]

    dict_students = {}
    for i in students:
        dict_students[int(i[0])] = i[1:]

    printTable()


def sortDict():
    global dict_students
    st = []

    for i in dict_students:
        st += [[i] + dict_students.get(i)]

    st.sort(key=lambda d: d[2])

    dict_students = {}
    for i in st:
        dict_students[int(i[0])] = i[1:]
    printTable()


def printTable():
    global tableFrame
    tableFrame.children.clear()

    print(header)

    table_header = ttk.Frame(tableFrame)
    for i in range(len(header)):
        ttk.Label(table_header, text=header[i], width=30).grid(column=i, row=0, sticky=tk.NW, pady=10)
    table_header.grid(row=0)

    for i in range(len(dict_students)):
        table_row = ttk.Frame(tableFrame)
        key = int(list(dict_students.keys())[i])

        ttk.Label(table_row, text=key, width=30).grid(column=0, row=0, sticky=tk.NW, pady=10)

        for j in range(len(dict_students.get(key))):
            ttk.Label(table_row, text=dict_students.get(key)[j], width=30).grid(column=j + 1, row=0, sticky=tk.NW,
                                                                                pady=10)
        table_row.grid(row=i + 1)


def oddAge():
    for i in dict_students:
        dict_students.get(i)[1] = str(int(dict_students.get(i)[1]) - 1)

    printTable()


def save():
    f = open(filePathValue.get(), "w")
    raw = ';'.join(header) + '\n'
    for i in dict_students:
        raw += '{0};{1}\n'.format(i, ';'.join(dict_students.get(i)))

    f.write(raw)

buttons = ttk.Frame(fileControl)
ttk.Button(buttons, text="Открыть файл", command=openFileEvent).grid(column=0, row=0, sticky=tk.NE)
ttk.Button(buttons, text="Прочитать", command=readFile).grid(column=1, row=0, sticky=tk.NE)
ttk.Button(buttons, text="Сортировать", command=sortDict).grid(column=2, row=0, sticky=tk.NE)
ttk.Button(buttons, text="Уменьшить возвраст на 1", command=oddAge).grid(column=3, row=0, sticky=tk.NE)
ttk.Button(buttons, text="Сохранить", command=save).grid(column=4, row=0, sticky=tk.NE)
buttons.grid(row=1, sticky=tk.NE)

root.mainloop()
