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
def max_values (matrix):
    a = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            max_i = matrix[i].index(max(matrix[i]))
        max_i_tuple = (i,max_i,max(matrix[i]))
        a.append(max_i_tuple)
    return tuple(a)
matrix = generate_matrix()
print_matrix(matrix)
print(max_values(matrix))