import random

number_cycle = 8
list1 = []

for i in range(number_cycle):
    list1.append(random.randint(1, 100))
print(f'Перший список {list1}')
list2 = []

for j in range(number_cycle):
    number = int(input('Введіть число від 1 до 100: '))
    list2.append(number)
print(f'Другий список {list2}')

list3 = []
for l in range(number_cycle):
        list3.append(list1[l] + list2[l])
print(f'Сума списків : {list3}')
