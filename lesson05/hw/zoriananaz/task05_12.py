#12. Знайти максимальний елемент серед мінімальних елементів стовпців матриці.

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


m = generate_matrix(4, 5)
print(m)
print_matrix(m)

some = []
for i in range(len(m)):
    a = min(m[i])
    some.append(a)
print(some)
print(max(some))
