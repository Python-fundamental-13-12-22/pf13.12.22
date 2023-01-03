import random
list1 = []
list2 = []
list3 = []
for value in range(0, 10):
    list1.append(random.randint(1, 100))
for value in range(0, 10):
    list2.append(int(input(f"input list2[{value}]\n")))
for value in range(0, 10):
    list3.append(list1[value]+list2[value])
print(list1)
print(list2)
print(list3)
