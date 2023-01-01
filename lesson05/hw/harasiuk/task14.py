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

m = generate_matrix(10, 10, 1, 20)
print('m =')
print_matrix(m)
for i in range(len(m)):
    m[i][i], m[10-i-1][i] = m[10-i-1][i], m[i][i]
print("m new =")
print_matrix(m)
