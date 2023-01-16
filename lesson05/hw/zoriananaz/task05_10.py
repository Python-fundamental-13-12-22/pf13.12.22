#10. Сформувати матрицю з чисел від 0 до 999, вивести її на екран.
# Порахувати кількість двозначних чисел в ній.
def generate_matrix(n=10, m=10, min_value=0, max_value=999):
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
m_x = generate_matrix(4, 4, 4)
print_matrix(m_x)
count = 0
for d in range(4):
    for p in range(4):
        if 9 < m_x[d][p] < 100:
            count += 1
print(count)
