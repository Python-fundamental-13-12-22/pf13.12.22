# Порахувати суми кожного рядка і кожного стовпця матриці. Доповнити її стовпцем, який містить суми елементів рядків
# та рядком, елементами якого є суми елементів стовпців.
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

n = 5
m = generate_matrix(n, n)
print_matrix(m)

vector1 = []
for i in range(n):
    vector1.append(sum(m[i]))

vector2 = m[0][:]
for i in range(1,n):
    for j in range(n):
        vector2[j] += m[i][j]

for i in range(n):
    m[i].append(vector1[i])
# m.append(vector2)
print()
print_matrix(m)