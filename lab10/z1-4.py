import PySimpleGUI as sg

def printMatrix(matrix):
    ans = ''
    for row in matrix:
        for x in row:
            ans += f'{x}\t'
        ans += '\n'
    return ans


matrix = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9, 7, 5, 3],
    [3, 1, 5, 3, 2, 6, 5, 7],
    [1, 7, 5, 9, 7, 3, 1, 5],
    [2, 6, 3, 5, 1, 7, 3, 2]
]


def z1():
    n = 8
    s = 0
    number = 1
    for i in range(n):
        print(number, "=", sum(matrix[i]))
        number = number + 1


z1()


def z2():
    z = [0 for i in matrix[0]]

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            z[i] += matrix[j][i]

    print(z)


z2()


def z3():
    r = [sum(i[::2]) for i in matrix]
    print(r)


z3()


def z4():
    z = []
    for i in range(8):  # i столбец
        k = 0
        for j in range(8):  # j строка
            if j % 2 == 0:
                k += matrix[j][i]
        z.append(k)
    print(z)


z4()
