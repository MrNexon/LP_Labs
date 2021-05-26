import re
from tkinter import ttk

import tkinter as tk

data_arr = [
    [
        1,
        'Белякова Ефим Святославович',
        18,
        'ВКБ13'
    ],
    [
        2,
        'Курдус Аким Юрьевич',
        15,
        'ВКБ13'
    ],
    [
        3,
        'Иванов Максим Сергеевич',
        22,
        'ЭИНГПАЛ12'
    ],
    [
        4,
        'Иванов Тимур Варельевич',
        23,
        'ВКБ11'
    ],
]


def arrayToDictionary(t: list):
    d = dict()
    for i in t:
        d[i[0]] = i[1:]
    return d


data_dict = arrayToDictionary(data_arr)


def z2_1FindByFIO(tdict: dict, fio: str):
    for i in tdict.keys():
        if tdict.get(i)[0] == fio:
            tdict.get(i)[1] += 1

    return tdict


def z2_2ReplaceByFIO(tdict: dict, fio1: str, fio2: str):
    for i in tdict.keys():
        if tdict.get(i)[0] == fio1:
            tdict.get(i)[0] = fio2

    return tdict


def z2_3FindById(tdict: dict, id: int):
    tdict.get(id)[1] += 1

    return tdict


def z2_4ReplaceGroupByFIO(tdict: dict, fio: str, group: str):
    for i in tdict.keys():
        if tdict.get(i)[0] == fio:
            tdict.get(i)[2] = group

    return tdict


def z2_5DeleteById(tdict: dict, id: int):
    tdict.pop(id)

    return tdict


def z2_6LimitBy22(tdict: dict):
    for i in tdict.keys():
        if tdict.get(i)[1] == 22:
            tdict.get(i)[1] -= 1

    return tdict


def z2_7DeleteBy23(tdict: dict):
    nd = dict(tdict)
    for i in nd.keys():
        if nd.get(i)[1] == 23:
            tdict.pop(i)

    return tdict


def z2_8AddAgeByIvanov(tdict: dict):
    for i in tdict.keys():
        if re.match("^[а-я]* ", tdict.get(i)[0], flags=re.IGNORECASE):
            tdict.get(i)[1] += 1

    return tdict


def z2_9ReplaceLNToSidorov(tdict: dict):
    for i in tdict.keys():
        tdict.get(i)[0] = re.sub("^[а-я]* ", 'Сидоров ', tdict.get(i)[0], flags=re.IGNORECASE)

    return tdict


def z2_10SwapFIOasGroup(tdict: dict):
    nd = dict(tdict)
    for i in nd.keys():
        nd[i] = nd.get(i)[::-1]

    return nd


# -----------------------------------------------------------

def z3_1FindByGroup(tdict: dict):
    nd = {}
    for i in tdict.keys():
        if tdict[i][2] == 'ВКБ13':
            nd[i] = tdict[i]
    return nd


def z3_2FindById(tdict: dict):
    nd = {}
    for i in tdict.keys():
        if 1 <= i <= 10:
            nd[i] = tdict[i]
    return nd


def z3_3FindByAge(tdict: dict):
    nd = {}
    for i in tdict.keys():
        if tdict[i][1] == 22:
            nd[i] = tdict[i]
    return nd


def z3_4FindByIvanov(tdict: dict):
    nd = {}
    for i in tdict.keys():
        if re.match("^Иванов ", tdict.get(i)[0], flags=re.IGNORECASE):
            nd[i] = tdict[i]
    return nd


def z3_5FindByEndA(tdict: dict):
    nd = {}
    for i in tdict.keys():
        if re.match("^[а-я]*а ", tdict.get(i)[0], flags=re.IGNORECASE):
            nd[i] = tdict[i]
    return nd


def z3_6FindByOdd(tdict: dict):
    nd = {}
    for i in tdict.keys():
        if tdict[i][1] % 2 == 0:
            nd[i] = tdict[i]
    return nd


def z3_7FindByExist5(tdict: dict):
    nd = {}
    for i in tdict.keys():
        if re.match("\d*5\d*", str(tdict.get(i)[1]), flags=re.IGNORECASE):
            nd[i] = tdict[i]
    return nd


def z3_8FindByLen7(tdict: dict):
    nd = {}
    for i in tdict.keys():
        if len(tdict.get(i)[2]) > 7:
            nd[i] = tdict[i]
    return nd


def z3_9FindByIdOdd(tdict: dict):
    nd = {}
    for i in tdict.keys():
        if i % 2 == 0:
            nd[i] = tdict[i]
    return nd


def z3_10FindByEnd1(tdict: dict):
    nd = {}
    for i in tdict.keys():
        if re.match("[а-я0-9]*1$", tdict.get(i)[2], flags=re.IGNORECASE):
            nd[i] = tdict[i]
    return nd


root = tk.Tk()
root.title('Лабораторная работа 8')
root.configure(bg='grey85')

s = ttk.Style()
s.theme_use('classic')

tableFrame = ttk.Frame(root)
tableFrame.grid(column=0, row=0, sticky=tk.EW, ipadx=10, ipady=10)
tableFrame.columnconfigure(0, weight=1)
tableFrame.columnconfigure(1, weight=1)
tableFrame.columnconfigure(2, weight=1)
tableFrame.columnconfigure(3, weight=1)


def drawTable(dtd):
    ttk.Label(tableFrame, text='№', width=5).grid(column=0, row=0, sticky=tk.NW, pady=10)
    ttk.Label(tableFrame, text='ФИО', width=30).grid(column=1, row=0, sticky=tk.NW, pady=10)
    ttk.Label(tableFrame, text='Возраст', width=30).grid(column=2, row=0, sticky=tk.NW, pady=10)
    ttk.Label(tableFrame, text='Группа', width=30).grid(column=3, row=0, sticky=tk.NW, pady=10)

    for i in dtd:
        ttk.Label(tableFrame, text=i, width=5).grid(column=0, row=i + 1, sticky=tk.NW, pady=10)
        ttk.Label(tableFrame, text=dtd[i][0], width=30).grid(column=1, row=i + 1, sticky=tk.NW, pady=10)
        ttk.Label(tableFrame, text=dtd[i][1], width=30).grid(column=2, row=i + 1, sticky=tk.NW, pady=10)
        ttk.Label(tableFrame, text=dtd[i][2], width=30).grid(column=3, row=i + 1, sticky=tk.NW, pady=10)


drawTable(data_dict)


def callFunc(func, args):
    drawTable(func(*args))


buttonFrame = ttk.Frame(root)
buttonFrame.grid(column=0, row=2, sticky=tk.SW, ipadx=0, ipady=10)

z2_1 = ttk.Frame(buttonFrame)
z21FIO = ttk.Entry(z2_1)
z21FIO.grid(column=0, row=0)
ttk.Button(z2_1, text="Увеличить на 1",
           command=lambda: callFunc(z2_1FindByFIO, [data_dict, z21FIO.get()])).grid(column=1,
                                                                                    row=0,
                                                                                    sticky=tk.NW)
z2_1.grid(column=0, row=0)

z2_2 = ttk.Frame(buttonFrame)
z22fromFIO = ttk.Entry(z2_2)
z22toFIO = ttk.Entry(z2_2)
z22fromFIO.grid(column=0, row=0)
z22toFIO.grid(column=1, row=0)

ttk.Button(z2_2, text="Изменить ФИО", command=lambda: callFunc(z2_2ReplaceByFIO, [data_dict, z22fromFIO.get(), z22toFIO.get()])).grid(column=2, row=0, sticky=tk.NW)
z2_2.grid(column=0, row=1)

z2_3 = ttk.Frame(buttonFrame)
z23Numb = ttk.Entry(z2_3)
z23Numb.grid(column=0, row=0)
ttk.Button(z2_3, text="Увеличить возраст", command=lambda: callFunc(z2_3FindById, [data_dict, int(z23Numb.get())])).grid(column=1, row=0, sticky=tk.NW)
z2_3.grid(column=0, row=2)

z2_4 = ttk.Frame(buttonFrame)
z24FIO = ttk.Entry(z2_4)
z24FIO.grid(column=0, row=0)
z24Num = ttk.Entry(z2_4)
z24Num.grid(column=1, row=0)
ttk.Button(z2_4, text="Изменить группу", command=lambda: callFunc(z2_4ReplaceGroupByFIO, [data_dict, z24FIO.get(), z24Num.get()])).grid(column=2, row=0, sticky=tk.NW)
z2_4.grid(column=0, row=3)

z2_5 = ttk.Frame(buttonFrame)
z25Num = ttk.Entry(z2_5)
z25Num.grid(column=0, row=0)
ttk.Button(z2_5, text="Удалить студента", command=lambda: callFunc(z2_5DeleteById, [data_dict, int(z25Num.get())])).grid(column=1, row=0, sticky=tk.NW)
z2_5.grid(column=0, row=4)

ttk.Button(buttonFrame, text="Уменьшить возраст (22)", command=lambda: callFunc(z2_6LimitBy22, [data_dict])).grid(column=0, row=5, sticky=tk.NW)
ttk.Button(buttonFrame, text="Удалить студента (23)", command=lambda: callFunc(z2_7DeleteBy23, [data_dict])).grid(column=0, row=6, sticky=tk.NW)
ttk.Button(buttonFrame, text="Увеличить возраст у Иванов", command=lambda: callFunc(z2_8AddAgeByIvanov, [data_dict])).grid(column=0, row=7, sticky=tk.NW)
ttk.Button(buttonFrame, text="Иванов на Сидоров", command=lambda: callFunc(z2_9ReplaceLNToSidorov, [data_dict])).grid(column=0, row=8, sticky=tk.NW)
ttk.Button(buttonFrame, text="ФИО и Группа местами", command=lambda: callFunc(z2_10SwapFIOasGroup, [data_dict])).grid(column=0, row=9, sticky=tk.NW)

root.mainloop()
