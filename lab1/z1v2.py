import math

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))
k = int(input('k: '))

d1 = (a ** 2) - (b ** 3) - (c ** 3) * (a ** 2)
d2 = b - c + c * (k - d / (b ** 3))
d3 = k / b - k / a

try:
    print(math.fabs((d1 * d2 - d3 * c) ** 2 - 20000))
except ArithmeticError:
    print('Деление на 0')