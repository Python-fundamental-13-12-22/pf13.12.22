import random

a1 = [random.randint(0, 20) for i in range(10)]
print('a1 = ', a1)
a2 = []
for a in a1:
    if a not in a2:
        a2.append(a)
print('Список унікальних a2 = ', a2)
