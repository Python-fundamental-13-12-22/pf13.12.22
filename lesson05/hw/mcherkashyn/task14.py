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

n = 10 #рядків
m = 10 #стовпців
matrix = generate_matrix(n, m)
print_matrix(matrix)
print("Змінена матриця:")
for i in range(n):
    if i != (n / 2):
        temp = matrix[i][i]
        matrix[i][i] = matrix[i][n - i - 1]
        matrix[i][n - i - 1] = temp

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
