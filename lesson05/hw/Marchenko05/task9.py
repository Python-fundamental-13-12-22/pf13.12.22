import random

def generate_matrix(n=4, m=4, min_value=0, max_value=10):
    matrix = []
    for i in range(n):
        row = []
        sum_row = 0
        for j in range(m - 1):
            number = random.randint(min_value, max_value)
            sum_row += number
            row.append(number)
        row.append(sum_row)
        matrix.append(row)

    row_sum_colum = []
    for i in range(m):
        sum_colum = 0
        for j in range(n):
            sum_colum += matrix[j][i]
        row_sum_colum.append(sum_colum)
    matrix.append(row_sum_colum)

    return matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

m = generate_matrix()
print_matrix(m)
