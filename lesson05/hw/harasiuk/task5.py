import random
list1 = []
listmax = []
for value in range(0, 20):
    list1.append(random.randint(-100, 100))
print(list1)
for value in range(len(list1)):
    if list1[value] > 0:
        listmax.append(list1[value])
list1.clear()
list1.extend(listmax)
print(list1)
