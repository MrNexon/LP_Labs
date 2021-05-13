import os

f = open("students.csv", "r")

students = []

for raw in f.read().splitlines()[1:]:
    splitted = raw.split(';')
    students.append(splitted)

group = input("Группа?\n>")
for v in students:
    if group == v[3]:
        v[2] = int(v[2]) + 1


print(*students, sep='\n')
