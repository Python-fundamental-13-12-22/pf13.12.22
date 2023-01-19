#9. Порахувати суми кожного рядка і кожного стовпця матриці.
# Доповнити її стовпцем, який містить суми елементів рядків
# та рядком, елементами якого є суми елементів стовпців.
def generate_matrix(n=3, m=3, min_value=0, max_value=10):
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


m_x = generate_matrix(3, 3, 3)
print_matrix(m_x)


list_1 = []
for i in range(3):
    list_1.append(sum(m_x[i]))
list_j = m_x[0][:]

for i in range(1, 3):
    for j in range(3):
        list_j[j] += m_x[i][j]

for i in range(3):
    m_x[i].append(list_1[i])
m_x.append(list_j)
print()
print_matrix(m_x)
