# 13. Дві матриці заповнюються введенням з клавіатури.
# В елементи третьої матриці такої ж розмірності записати більші з відповідних елементів перших двох.

matrx_1 = []
matrx_2 = []
# create first matrix
for i in range(3):
    matrx_1.append([0] * 3)
    for j in range(3):
        matrx_1[i][j] = int(input("enter value to first matrix: "))

# create second matrix
for i in range(3):
    matrx_2.append([0] * 3)
    for j in range(3):
        matrx_2[i][j] = int(input("enter value to second matrix: "))

# sum values
matrix_sum = []
for i in range(3):
    matrix_sum.append([0] * 3)
    for j in range(3):
        matrix_sum[i][j] = matrx_1[i][j] + matrx_2[i][j]


def print_matrix(m):
    for a in range(len(m)):
        for b in range(len(m[i])):
            print(m[a][b], end="\t")
        print()
    print()


print_matrix(matrx_1)
print_matrix(matrx_2)
print_matrix(matrix_sum)
