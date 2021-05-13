import math

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))
f = int(input('f: '))

try:
    d1 = a - b * c * (d ** 3) + ((c ** 5) - (a ** 2)) / a + (f ** 3) * (a - 213)
    print(math.fabs(d1))
except ArithmeticError:
    print('Деление на 0')
