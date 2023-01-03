def generate_matrix(n, m, min_value, max_value):
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

m = generate_matrix(10, 10, 0, 999)
print_matrix(m)
l = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        if 9 < m[i][j] < 100:
            l = l + 1
print(f"Кількість двохзначних чисел = {l}")
