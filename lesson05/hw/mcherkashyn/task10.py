def generate_matrix(n=5, m=5, min_value=0, max_value=999):
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

n = 5
m = generate_matrix(n, n)
print_matrix(m)

vector = []
count = 0

for i in range(n):
    for t in m[i]:
        if len(str(t)) == 2:
            count = count + 1
            vector.append(t)
print(f"Двозначні числа: {vector}")
print(f"Кількість двозначних чисел: {count}")
