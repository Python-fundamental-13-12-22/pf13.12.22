"""13. Дві матриці заповнюються введенням з клавіатури.
В елементи третьої матриці такої ж розмірності записати більші з відповідних елементів перших двох."""


matr_1 = []
matr_2 = []
for i in range(3):
    matr_1.append([0] * 3)

for i in range(3):
    for j in range(3):
        matr_1[i][j] = int(input(":"))
print(matr_1)

for i in range(3):
    matr_2.append([0] * 3)

for i in range(3):
    for j in range(3):
        matr_2[i][j] = int(input(":"))
print(matr_2)

matrix_sum = []
for i in range(3):
    matr_2.append([0] * 3)
print(matrix_sum)

for i in range(3):
    for j in range(3):
        matrix_sum.append(matr_1[i][j] + matr_2[i][j])
print(matrix_sum)
