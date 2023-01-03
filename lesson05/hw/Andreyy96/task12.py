def generate_matrix(n, m, min_value=0, max_value=100):
    import random
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
    print(f'Максимальный элемент среди минимальных {max(min(row) for row in matrix)}')

n = int(input('Введите количество столбцов '))
m = int(input('Введите количество строк '))

matrix = generate_matrix(n, m)
print_matrix(matrix)


