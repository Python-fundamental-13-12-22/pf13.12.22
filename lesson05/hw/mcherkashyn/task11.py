def input_matrix(n=5, m=3):
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

n = 5 #рядків
m = 3 #стовпців
m1 = input_matrix(n ,m)
print("Введена матриця:")
print_matrix(m1)

last_m = []
for i in range(n):
    last_m.append(sum(m1[i]))

for i in range(n):
    m1[i].append(last_m[i])

print("Змінена матриця:")
print_matrix(m1)
