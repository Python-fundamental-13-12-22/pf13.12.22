def generate_matrix(n, m, min_value = 10, max_value = 10):
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

m = generate_matrix(3, 3, 0, 10)
m1 = m.copy()
print_matrix(m)
row2 =[]
for i in range(len(m)):
    l2 = 0
    row = []
    lenrad = 0
    for j in range(len(m[i])):
        row.append(m[i][j])
        lenrad = lenrad + row[j]
        l2 = l2 + m[j][i]
        if j == len(m[i]) - 1:
            m[i].append(lenrad)
    row2.append(l2)
l2 = 0
for i in range(len(m)):
    k = len(m[i])
    l2 = l2 + m[i][k-1]
row2.append(l2)
m.append(row2)
print_matrix(m)
