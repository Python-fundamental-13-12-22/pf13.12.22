# Сформувати матрицю з чисел від 0 до 999, вивести її на екран. Порахувати кількість двозначних чисел в ній.
n = 3
m = 5
import random
p = [[random.randint(0, 999) for i in range(n)] for j in range(m)]
for i in range(n):
    print(' '.join(map(str, p[i])))
cd = []
for i in range(len(p)):
    for j in range(len(p[i])):
        if 100 > p[i][j] > 9:
            cd.append(p[i][j])
print(len(cd), 'двозначні числа в цій матриці')
