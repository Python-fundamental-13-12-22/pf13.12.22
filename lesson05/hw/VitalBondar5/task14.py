# У матриці 10x10 поміняти значення елементів у кожному рядку, розташовані відповідно на головній та бічній діагоналях.
n = 20
m = 20
import random
a = [[random.randint(1, 99) for i in range(n)] for j in range(m)]
for i in range(n):
    print(' '.join(map(str, a[i])))
print()
for j in range(m):
    for i in range(n):
        if i == j:
            a[j][i], a[j][n-1-i] = a[j][n-1-i], a[j][i]
for i in range(n):
    print(' '.join(map(str, a[i])))
