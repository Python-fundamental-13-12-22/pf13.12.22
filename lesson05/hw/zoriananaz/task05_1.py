#1. Заповнити один список випадковими числами, інший - введеними з клавіатури числами,
#в третій записати суми відповідних елементів перших двох. Вивести вміст списків на екран.
import random
list_1 = []
list_2 = []
list_sum = []
n = int(input("Enter number for length:"))
for i in range(0, n):
    list_1.append(random.randint(1, n))
for i in range(0, n):
    list_2.append(int(input(f"Enter number:")))
for i in range(0, n):
    list_sum.append(list_1[i] + list_2[i])
print(f"First list {list_1}\n"
      f"Second list {list_2}\n"
      f"Final list {list_sum}")
