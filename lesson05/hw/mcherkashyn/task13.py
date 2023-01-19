def input_matrix(n=3, m=3):
    matrix = []
    print(f"Ведіть {n * m} чисел матриці по одному числу:")
    for i in range(n):
        a = []
        for j in range(m):
            a.append(int(input()))
        matrix.append(a)
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

n = 3 #рядків
m = 3 #стовпців

print("Перша матриця")
m1 = input_matrix(n ,m)
print("Друга матриця")
m2 = input_matrix(n ,m)

print("Матриця 1:")
print_matrix(m1)
print("Матриця 2:")
print_matrix(m2)

def compare_lists(i1, j1):
    newl = []
    for i, j in zip(i1, j1):
        if i > j:
            newl.append(i)
        elif j > i:
            newl.append(j)
        elif j == i:
            newl.append(j)
    return(newl)

print("Матриця 3:")
for i1, j1 in zip(m1, m2):
    compare_lists(i1, j1)
    matrix = compare_lists(i1, j1)
    format = ' '.join(str(e) for e in matrix)
    print(format)
