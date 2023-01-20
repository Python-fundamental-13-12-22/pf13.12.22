# 12. Знайти максимальний елемент серед мінімальних елементів стовпців матриці.

def generate_matrix(n=5, m=5, min_value=0, max_value=100):
    import random
    matrix = []
    for a in range(n):
        row = []
        for b in range(m):
            row.append(random.randint(min_value, max_value))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for a in range(len(matrix)):
        for b in range(len(matrix[i])):
            print(matrix[a][b], end="\t")
        print()
    print()


mtx = generate_matrix()
print_matrix(mtx)

some = []
for i in range(len(mtx)):
    r = []
    for j in range(len(mtx[i])):
        r.append(mtx[j][i])
    some.append(min(r))
print(f"list of min values {some}")
print(f"Max value in list of min values is {max(some)}")
