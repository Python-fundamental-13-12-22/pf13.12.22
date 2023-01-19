# 15. Змінити послідовність стовпців матриці так, щоб елементи її першого рядка були
# відсортовані за зростанням.


def generate_matrix(n=3, m=3, min_value=0, max_value=20):
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


mtx = generate_matrix(3, 3, 1, 20)
print_matrix(mtx)


mtx_result = mtx[:]

for i in range(len(mtx_result)):
    min_i = i
    for j in range(i + 1, len(mtx_result)):
        if mtx_result[0][j] < mtx_result[0][min_i]:
            min_i = j
    mtx_result[0][min_i], mtx_result[0][i] = mtx_result[0][i], mtx_result[0][min_i]
    for k in range(1, len(mtx_result)):
        mtx_result[k][min_i], mtx_result[k][i] = mtx_result[k][i], mtx_result[k][min_i]
print()
print_matrix(mtx_result)
