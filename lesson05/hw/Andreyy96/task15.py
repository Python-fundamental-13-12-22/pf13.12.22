import random

def generate_matrix(n, m, min_value=0, max_value=100):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randint(min_value, max_value))
        matrix.append(row)

    return matrix

def sort_matrix(matrix, n, m):
    k = m - 1
    while k >= 0:
        ind = 0
        for j in range(1, k + 1):
            if matrix[0][j] > matrix[0][ind]:
                ind = j
        for i in range(n):
            matrix2 = matrix[i][ind]
            matrix[i][ind] = matrix[i][k]
            matrix[i][k] = matrix2
        k -= 1

    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

def print_sort_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

n = int(input('Введите количество столбцов '))
m = int(input('Введите количество строк '))

matrix = generate_matrix(n, m)
print_matrix(matrix)

print()
print('---------------------------------------')
print()

sort_matrix = sort_matrix(matrix, n, m)
print_sort_matrix(sort_matrix)
