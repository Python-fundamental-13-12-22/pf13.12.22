#1. Заповнити один список випадковими числами, інший - введеними з клавіатури числами,
#в третій записати суми відповідних елементів перших двох. Вивести вміст списків на екран.
import random
list_1 = []
list_2 = []
list_sum = []
i = 0
for i in range(0, 10):
    list_1.append(random.randint(1, 10))
for i in range(0, 10):
    list_2.append(int(input(f"Enter number:")))
for i in range(0, 10):
    list_sum.append(list_1[i] + list_2[i])
print(list_1)
print(list_2)
print(list_sum)
