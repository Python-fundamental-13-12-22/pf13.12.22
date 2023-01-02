import random

a1 = [random.randint(0, 20) for i in range(10)]
print('a1 = ', a1)
a2 = []
for i in range(10):
    if a1[i] % 2 == 0:
        a2.append(i)
print('Список індексів парних a2 = ', a2)



