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
m = generate_matrix()
print_matrix(m)
row2 = []
for i in range(len(m)):
    row = []
    for j in range(len(m[i])):
        row.append(m[j][i])
    row2.append(min(row))
print(max(row2))
print(row2)
