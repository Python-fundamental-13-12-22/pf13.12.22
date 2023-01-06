import random

list1 = []

for i in range(1, 11):
    list1.append(random.randint(1, 20))
print(f'Повний список : {list1}')

list2 = []
for j in range(len(list1)):
    element = list1.count(list1[j])
    print(element, end=' ')
    if element <= 1:
        list2.append(list1[j])
    else:
        continue
print()
print(f'Список з унікальними елементами : {list2}')
