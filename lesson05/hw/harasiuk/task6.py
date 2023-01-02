import random
list1 = []
list2 = []
for value in range(0, 20):
    list1.append(random.randint(-5, 5))
print(list1)
for value in range(len(list1)):
    if list1[value] % 2 == 0:
        list2.append(value)
print(list2)
