# Дві матриці заповнюються введенням з клавіатури. В елементи третьої матриці такої ж розмірності записати більші з
# відповідних елементів перших двох.
n = 3
m = 3
a = [[int(input('Введіть число 1 матриці :  ')) for i in range(n)] for j in range(m)]
for i in range(n):
    print(' '.join(map(str, a[i])))
print()
b = [[int(input('Введіть число 2 матриці  :  ')) for i in range(n)] for j in range(m)]
for i in range(n):
    print(' '.join(map(str, b[i])))
print()
matrix = []
for j in range(m):
    row = []
    for i in range(n):
        if a[j][i] >= b[j][i]:
            row.append(a[j][i])
        else:
            row.append(b[j][i])
    matrix.append(row)
for i in range(n):
    print(' '.join(map(str, matrix[i])))
