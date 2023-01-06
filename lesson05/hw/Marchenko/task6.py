import random

list1 = []
list2 = []

for i in range(1, 11):
    list1.append(random.randint(1, 20))

for index in range(len(list1)):
    if list1[index] % 2 == 0:
        index_element = list1.index(list1[index])
        list2.append(index_element)
    else:
        continue

print(list1)
print(f'Індекс парних елементів : {list2}')
