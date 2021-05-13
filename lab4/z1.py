import random


def printMatrix(matrix: list):
    for i in range(0, len(matrix)):
        print(*matrix[i], sep='\t')


n = int(input('N: '))
l = [[random.randint(0, 100) for j in range(0, n)] for i in range(0, n)]

s = 0

for i in range(0, n):
        s += sum(i)

printMatrix(l)
print(s)
