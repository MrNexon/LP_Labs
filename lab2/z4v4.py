st = input('Строка: ')

retd = ''
for i in [*st]:
    if 48 <= ord(i) < 57:
        retd += i

rets = ''
for i in [*st]:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 1040 <= ord(i) <= 1071 or 1072 <= ord(i) <= 1103:
        rets += i

print(retd)
print(rets)