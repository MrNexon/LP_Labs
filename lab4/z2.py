import random


def var1(li: list):
    r = li[2:] + [random.randint(-10, 0), random.randint(-10, 0)]
    print(r)


def var2(li: list):
    r = li[::2] + [random.randint(-10, 0), random.randint(-10, 0)]
    print(r)


def var3(li: list):
    r = li[:4] + l[9:] + [random.randint(-10, 0), random.randint(-10, 0)]
    print(r)

def var4(li: list):
    r = [random.randint(-10, 0) for i in range(5)] + li[1::2]
    print(r)


l = [random.randint(0, 50) for i in range(10)]
print(l)
print('--------------')
var1(l)
print('--------------')
var2(l)
print('--------------')
var3(l)
print('--------------')
var4(l)