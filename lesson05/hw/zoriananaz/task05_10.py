#10. Сформувати матрицю з чисел від 0 до 999, вивести її на екран.
# Порахувати кількість двозначних чисел в ній.
def generate_matrix(n=4, m=4, min_value=0, max_value=9):
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
m_x = generate_matrix(3, 3 ,3)
print_matrix(m_x)

for i in m_x:
    s = 0
    for j in i:
        s += j
    print(s)
for j in m_x:
    s = 0
    for i in j:
        s += i
    print(s)
