# 14. У матриці 10x10 поміняти значення елементів у кожному рядку, розташовані
# відповідно на головній та бічній діагоналях.


def generate_matrix(n=10, m=10, min_value=0, max_value=100):
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


mtx = generate_matrix(10, 10, 0, 100)
print_matrix(mtx)

mtx_final = mtx[:]
for i in range(10):
    mtx_final[i][i], mtx_final[10 - i - 1][i] = mtx_final[10 - i - 1][i],  mtx_final[i][i]
print()
print_matrix(mtx_final)
