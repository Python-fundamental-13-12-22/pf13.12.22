def generate_matrix1(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            number = int(input(f'Введіть число: '))
            row.append(number)
        matrix.append(row)

    return matrix

def generate_matrix2(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            number = int(input(f'Введіть число: '))
            row.append(number)
        matrix.append(row)

    return matrix

def generate_matrix3(n, m, m1, m2):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            if m1[i][j] >= m2[i][j]:
                row.append(m1[i][j])
            else:
                row.append(m2[i][j])
        matrix.append(row)

    return matrix

def print_matrix1(matrix):
    print('Перша матриця :')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

def print_matrix2(matrix):
    print('Друга матриця :')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

def print_matrix3(matrix):
    print('Третя матриця :')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

n = int(input('Введіть кількість стовпців : '))
m = int(input('Введіть кількість рядків : '))

m1 = generate_matrix1(n, m)
print()
m2 = generate_matrix2(n, m)
print()

print_matrix1(m1)
print_matrix2(m2)
print()

m3 = generate_matrix3(n, m, m1, m2)
print_matrix3(m3)
