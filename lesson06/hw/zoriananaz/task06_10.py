"""10. Напишіть функцію `max_values` яка повертає кортеж елементами якого є кортежі
які містять індекси та максимальне значення `(i, j, value)`.
 Функція приймає двовимірний масив (матрицю) як аргумент."""


def generate_matrix(n=5, m=5, min_value=0, max_value=20):
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


mtx = generate_matrix(5, 5, 0, 20)
print_matrix(mtx)


def max_values(matrix):
    mtx_max_el = []
    row = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            max_el = max(matrix[i])
            if matrix[i][j] == max_el:
                row = (i, j, max_el)
        mtx_max_el.append(row)
    return tuple(mtx_max_el)


print(max_values(mtx))
