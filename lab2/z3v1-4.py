import random


def random_s(n: int):
    sr = ''
    for i in range(0, n):
        sr += chr(random.randint(1040, 1071))

    return sr


def random_n(n: int):
    sr = ''
    for i in range(0, n):
        sr += 'r'

    return sr


def random_number(n: int):
    sr = []
    for i in range(0, n - 1):
        sr += [random.randint(0, 9)]

    sr.insert(random.randint(0, n - 1), 3)
    return ''.join(map(str, sr))


def random_sn(n: int):
    sr = []
    rands = random.randint(1, n - 1)
    sr += [*random_s(rands)]
    sr += [*random_number(n - rands)]
    random.shuffle(sr)
    return ''.join(sr)


print(random_s(5))
print(random_n(10))
print(random_number(6))
print(random_sn(8))