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


def max_values(matrix):
    crtj = []
    for i in range(len(matrix)):
        c1 = ()
        value = max(matrix[i])
        c1 = (i, matrix[i].index(value), value)
        crtj.append(c1)
    crtj = tuple(crtj)
    return crtj


n = int(input("input n\n"))
m = int(input("input m\n"))
matrix = generate_matrix(n,m)
print_matrix(matrix)
print_matrix(max_values(matrix))
