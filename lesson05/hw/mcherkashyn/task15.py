import numpy as np
def generate_matrix(n=3, m=3, min_value=0, max_value=100):
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

n = 3 #рядків
m = 3 #стовпців
matrix = generate_matrix(n, m)
print_matrix(matrix)

np_array = np.array(matrix, dtype=np.int64)
result = np_array[:, np_array[0].argsort()]
print("Відсортована матриця")
print_matrix(result)
