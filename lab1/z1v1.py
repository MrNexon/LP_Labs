import math

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
k = int(input('k: '))

try:
    d1 = (a ** 2) / (b ** 2) + (c ** 2) * (a ** 2)
    d2 = a + b + c * (k - a / (b ** 3))
    d3 = k / b - k / a

    print(math.fabs(d1 / d2 + c + d3 * c))
except ArithmeticError:
    print('Деление на 0')
