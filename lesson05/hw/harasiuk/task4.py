import random
list1 = []
listmax = []
listmin = []
for value in range(0, 20):
    list1.append(random.randint(-5, 5))
for value in range(len(list1)):
    if list1[value] > 0:
        listmax.append(list1[value])
    elif list1[value] < 0:
        listmin.append(list1[value])
print(list1)
print(listmin)
print(listmax)