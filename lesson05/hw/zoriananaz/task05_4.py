#4. Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один помістити тільки
#додатні, у другий - тільки від’ємні. Числа, рівні нулю, ігнорувати.
#Вивести на екран всі згенеровані випадкові числа і елементи обох списків.
import random
rand_list = []
positive_num_list = []
negative_num_list = []
positive_numbers = 0
for i in range(1, 21):
    n = random.randint(-5, 5)
    rand_list.append(n)
    if n > 0:
        positive_num_list.append(n)
    elif n < 0:
        negative_num_list.append(n)
    else:
        continue
print(f"{rand_list}\n"
      f"{positive_num_list}\n"
      f"{negative_num_list}")
