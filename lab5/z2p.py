f = open("students.csv", "r")

students = []

for raw in f.read().splitlines()[1:]:
    splited = raw.split(';')
    students += [splited]


students.sort(key=lambda s: s[3])
for s in students:
    print(s)
