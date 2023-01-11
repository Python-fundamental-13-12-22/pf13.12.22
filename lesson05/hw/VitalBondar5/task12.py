# Знайти максимальний елемент серед мінімальних елементів стовпців матриці.
n = 4
m = 4
import random
a = [[random.randint(1, 9) for i in range(n)] for j in range(m)]
for i in range(n):
    print(' '.join(map(str, a[i])))
print()
c = [min(a[0][j], a[n-1][j]) for j in range(m)]
print(max(c))
