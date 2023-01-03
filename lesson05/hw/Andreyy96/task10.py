import random

def generate_matrix(n=7, m=7, min_value=0, max_value=999):
    count = 0
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            number = int(random.randint(min_value, max_value))
            if 9 < number < 100:
                count += 1
            row.append(number)
        matrix.append(row)

    return  matrix, count

def print_matrix(matrix, count):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()
    print(f'Количество двузначных чисел: {count}')

    return matrix

m, count = generate_matrix()
print_matrix(m, count)
