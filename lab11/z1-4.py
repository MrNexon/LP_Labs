import sqlite3
import tkinter as tk
from tkinter import ttk

from prettytable import PrettyTable

conn = sqlite3.connect("data.db")
cursor = conn.cursor()


def createTables():
    cursor.execute("""CREATE TABLE food(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    type TEXT NOT NULL,
    manufacturer TEXT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    name TEXT NOT NULL);""")

    cursor.execute("""
    CREATE TABLE animal( 
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    moniker TEXT NOT NULL, 
    age INT NOT NULL,
    gender BOOLEAN NOT NULL,
    food_id INTEGER NOT NULL,
    type TEXT NOT NULL,
    FOREIGN KEY (food_id) REFERENCES food(id));""")

    conn.commit()


def addAnimal():
    d = [
        animal_moniker.get(),
        animal_age.get(),
        animal_gender.get(),
        animal_food_id.get(),
        animal_type.get()
    ]
    cursor.executemany("""
    INSERT INTO animal(moniker, age, gender, food_id, type)
    VALUES (?,?,?,?,?);""", [d])

    conn.commit()


def deleteAnimal():
    cursor.executemany("""
    DELETE FROM animal
    WHERE id = ?;""", animal_id.get())

    conn.commit()


def updateAnimal():
    d1 = [
        animal_moniker.get(),
        animal_age.get(),
        animal_gender.get(),
        animal_food_id.get(),
        animal_type.get()
    ]
    d = [*d1, animal_id.get()]
    cursor.executemany("""
    UPDATE animal
    SET moniker = ?, age = ?, gender = ?, food_id = ?, type = ?
    WHERE id = ?""", [d])

    conn.commit()


def upsertAnimal(tdict):
    for i in tdict:
        cursor.execute("""
        INSERT INTO animal
        VALUES(:id, :moniker, :age, :gender, :food_id, :type) 
        ON CONFLICT(id) 
        DO UPDATE SET moniker = :moniker, age = :age, gender = :gender, food_id = :food_id, type = :type;""", i)

        conn.commit()


def addFood():
    d = [
        food_type.get(),
        food_manufacturer.get(),
        food_price.get(),
        food_name.get()
    ]
    cursor.executemany("""
    INSERT INTO food(type, manufacturer, price, name)
    VALUES (?, ?, ?, ?);""", [d])

    conn.commit()


def deleteFood():
    cursor.executemany("""
    DELETE FROM food
    WHERE id = ?;""", food_id.get())

    conn.commit()


def updateFood():
    d1 = [
        food_type.get(),
        food_manufacturer.get(),
        food_price.get(),
        food_name.get()
    ]
    d = [*d1, food_id.get()]
    cursor.executemany("""
    UPDATE food
    SET type = ?, manufacturer = ?, price = ?, name = ?
    WHERE id = ?""", [d])

    conn.commit()


def upsertFood(tdict):
    for i in tdict:
        cursor.execute("""
        INSERT INTO food
        VALUES(:id, :type, :manufacturer, :price, :name) 
        ON CONFLICT(id) 
        DO UPDATE SET type = :type, manufacturer = :manufacturer, price = :price, name = :name;""", i)

        conn.commit()


def select():
    return {'header': ['id', 'Кличка', 'Пол', 'Возраст', 'Название корма', 'Цена корма'],
            'data': cursor.execute("""
    SELECT 
        animal.id,
        animal.moniker,
       animal.gender,
       animal.age,
       food.name,
       food.price
    FROM animal JOIN food on food.id = animal.food_id""")}


def group():
    return {'header': ['id', 'Тип', 'Изготовитель', 'Цена', 'Имя', 'Количество животных'],
            'data': cursor.execute("""
    SELECT food.*, count(food.id)
    FROM animal JOIN food on food.id = animal.food_id
    GROUP BY food.id
""")}


def drawTable(data_dict):
    label.config(state=tk.NORMAL)
    label.delete(1.0, tk.END)

    tableData = PrettyTable()
    tableData.field_names = data_dict['header']

    for i in data_dict['data']:
        tableData.add_row(i)

    label.insert(1.0, tableData)
    label.config(state=tk.DISABLED)


def animalDump():
    return {
        'header': ['id', 'moniker', 'age', 'gender', 'food_id', 'type'],
        'data': cursor.execute("""SELECT * FROM animal""")
    }


def foodDump():
    return {
        'header': ['id', 'type', 'manufacturer', 'price', 'name'],
        'data': cursor.execute("""SELECT * FROM food""")
    }


def saveToFile(name, data):
    fo = open('{0}.csv'.format(name), 'w')
    fo.write(';'.join(map(str, data['header'])) + '\n')
    for i in data['data']:
        fo.write(';'.join(map(str, [*i])) + '\n')
    fo.close()


def save():
    saveToFile('animal', animalDump())
    saveToFile('food', foodDump())


def loadFiles():
    upsertAnimal(loadData(open('animal.csv', 'r')))
    upsertFood(loadData(open('food.csv', 'r')))


def loadData(file):
    data = []
    keys = []
    i = 0

    for l in file:
        if i == 0:
            keys = l.replace('\n', '').split(';')
        else:
            data.insert(i - 1, {})
            k = 0
            for j in l.replace('\n', '').split(';'):
                data[i - 1][keys[k]] = j
                k += 1
        i += 1

    return data


root = tk.Tk()
root.title('Лабораторная работа 11')
root.configure(bg='grey85')

s = ttk.Style()
s.theme_use('classic')

label = tk.Text(root, width=150)
label.pack()

ttk.Button(root, text='Вывести животных', command=lambda: drawTable(select())).pack()
ttk.Button(root, text='Вывести информацию о количестве животных по корму', command=lambda: drawTable(group())).pack()

animal_id = tk.StringVar()
animal_moniker = tk.StringVar()
animal_age = tk.StringVar()
animal_gender = tk.StringVar()
animal_food_id = tk.StringVar()
animal_type = tk.StringVar()

restAnimalFrame = ttk.Frame(root)
ttk.Label(root, text='Операции для таблицы animal').pack()
ttk.Entry(restAnimalFrame, width=5, textvariable=animal_id).grid(column=0, row=0)
ttk.Entry(restAnimalFrame, textvariable=animal_moniker).grid(column=1, row=0)
ttk.Entry(restAnimalFrame, width=10, textvariable=animal_age).grid(column=2, row=0)
ttk.Entry(restAnimalFrame, width=10, textvariable=animal_gender).grid(column=3, row=0)
ttk.Entry(restAnimalFrame, width=10, textvariable=animal_food_id).grid(column=4, row=0)
ttk.Entry(restAnimalFrame, textvariable=animal_type).grid(column=5, row=0)
ttk.Button(restAnimalFrame, text='Создать', command=addAnimal).grid(column=6, row=0)
ttk.Button(restAnimalFrame, text='Обновить', command=updateAnimal).grid(column=7, row=0)
ttk.Button(restAnimalFrame, text='Удалить', command=deleteAnimal).grid(column=8, row=0)
restAnimalFrame.pack()

food_id = tk.StringVar()
food_type = tk.StringVar()
food_manufacturer = tk.StringVar()
food_price = tk.StringVar()
food_name = tk.StringVar()

restAnimalFrame = ttk.Frame(root)
ttk.Label(root, text='Операции для таблицы food').pack()
ttk.Entry(restAnimalFrame, width=5, textvariable=food_id).grid(column=0, row=0)
ttk.Entry(restAnimalFrame, textvariable=food_type).grid(column=1, row=0)
ttk.Entry(restAnimalFrame, textvariable=food_manufacturer).grid(column=2, row=0)
ttk.Entry(restAnimalFrame, width=15, textvariable=food_price).grid(column=3, row=0)
ttk.Entry(restAnimalFrame, width=40, textvariable=food_name).grid(column=4, row=0)
ttk.Button(restAnimalFrame, text='Создать', command=addFood).grid(column=5, row=0)
ttk.Button(restAnimalFrame, text='Обновить', command=updateFood).grid(column=6, row=0)
ttk.Button(restAnimalFrame, text='Удалить', command=deleteFood).grid(column=7, row=0)
restAnimalFrame.pack()

ttk.Button(root, text='Сохранить в CSV', command=save).pack()
ttk.Button(root, text='Считать из CSV', command=loadFiles).pack()

root.mainloop()
