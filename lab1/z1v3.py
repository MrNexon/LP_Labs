import math

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

try:
    d = 1 - a * (b ** c) - a * ((b ** 2) - (c ** 2)) + (b - c + a) * (12 + b) / (c - a)
    print(math.fabs(d))
except ArithmeticError:
    print('Деление на 0')

