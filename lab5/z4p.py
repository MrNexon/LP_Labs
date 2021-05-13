f = open("students.csv", "r")

students = []

for raw in f.read().splitlines()[1:]:
    splitted = raw.split(';')
    students += [splitted]

f.close()

group = input("Группа?\n>")
for v in students:
    if group == v[3]:
        v[2] = int(v[2]) + 1

print(students)



ans = input("Сохранить в файл?\n>")
if ans == "Да":
    f = open("students.csv", "w")
    raw = "No;ФИО;Возраст;Группа\n"
    for s in students:
        for v in s:
            raw += str(v)
            raw += ';'
        raw += '\n'
    f.write(raw)

