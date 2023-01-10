# Змінити послідовність стовпців матриці так, щоб елементи її першого рядка були відсортовані за зростанням.
n = 4
m = 4
import random
a = [[random.randint(1, 99) for i in range(n)] for j in range(m)]
for i in range(n):
    print(' '.join(map(str, a[i])))
print()
b = a[0].copy()
print(b)
b.sort(reverse=False)
print(b)
# поки не дійшло як переставити елементи нижніх рядків по індексах нового.
# c = []
# for i in range(n):
#     if b[i] != a[0][i]:
#         print(a[0][i])
#         print(i)
#         k = i
#         c.append(k)
# print(c)
#
# v = a[0]
# for i in range(n):
#     l = i
#     for j in range(i + 1, m):
#         if v[j] < v[l]:
#             l = j
#     a[i][l], a[i][j] = a[i][j], a[i][l]


# for i in range(n):
#     a[i][2], a[i][3] = a[i][3], a[i][2]

a[0] = b
for i in range(n):
    print(' '.join(map(str, a[i])))
print()

