def generate_matrix(n=5, m=5, min_value=0, max_value=100):
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

def max_value(matrix):
    t_matrix = ()
    for i in range(len(matrix)):
        max_v = max(matrix[i])
        tuple_row = (matrix[i].index(max_v), i, max_v)
        t_matrix = t_matrix + (tuple_row,)

    return t_matrix

def print_max_matrix(tuple_matrix):
    for i in tuple_matrix:
        print(i)





matrix = generate_matrix()
print_matrix(matrix)
print()

tuple_matrix = max_value(matrix)
print_max_matrix(tuple_matrix)
