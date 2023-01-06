import random

number_cycle = 20
list = []

for i in range(number_cycle):
    list.append(random.randint(-100, 100))
print(f'Повний список :  {list}')

j = 0
while number_cycle > j:
    if list[j] < 0:
        del list[j]
        number_cycle -= 1
    else:
        j += 1
print(f'Без мінусових чисел : {list}')
