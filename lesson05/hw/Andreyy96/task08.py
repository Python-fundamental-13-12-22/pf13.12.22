import random

list1 = []

for i in range(1, 21):
    list1.append(random.randint(1, 20))
print(f'До {list1}')

min_number = list1.index(min(list1))
max_number = list1.index(max(list1))

print(f'Минимальный элемент {min_number} = {min(list1)}')
print(f'Максимальный элемент {max_number} = {max(list1)}')

list1[min_number], list1[max_number] = list1[max_number], list1[min_number]

print(f'После {list1}')
