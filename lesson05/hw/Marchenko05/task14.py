import random

def generate_matrix1(n=10, m=10, min_value=0, max_value=100):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randint(min_value, max_value))
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

def print_trans_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i][j] = 123
            elif i + j == 9:
                matrix[i][j] = 321
            print(matrix[i][j], end="\t")
        print()

matrix = generate_matrix1()
print_matrix(matrix)
print()
print_trans_matrix(matrix)
