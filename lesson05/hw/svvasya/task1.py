import random

a1 = [random.randint(0, 100) for i in range(10)]
b1 = []
for i in range(0,10):
    a = int(input('Введіть число '))
    b1.append(a)
print('a1 = ', a1)
print('b1 = ', b1)
c1 = []
for i in range(10):
    c1.append(a1[i] + b1[i])
print('c1 = ', c1)
