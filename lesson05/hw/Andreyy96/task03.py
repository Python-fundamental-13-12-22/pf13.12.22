import random

number_cycle = 20
list1 = []

for i in range(number_cycle):
    list1.append(random.randint(-5, 4))
print(list1)

negative_numbers = 0
positive_numbers = 0
zero_numbers = 0
for j in range(len(list1)):
    if list1[j] < 0:
        negative_numbers += 1
    elif list1[j] > 0:
        positive_numbers += 1
    elif list1[j] == 0:
        zero_numbers += 1
    else:
        continue

print(f'Количество положительных чисел в списке: {positive_numbers}')
print(f'Количество отрицательных чисел в списке: {negative_numbers}')
print(f'Количество нулей в списке: {zero_numbers}')
