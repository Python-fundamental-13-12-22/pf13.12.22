import random
list1 = []
list2 = []
for value in range(0, 20):
    list1.append(random.randint(-5, 5))
print(list1)
for value in range(len(list1)):
    if list1.count(list1[value]) == 1:
        list2.append(list1[value])
print(list2)
