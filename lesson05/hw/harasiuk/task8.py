import random
list1 = []
for value in range(0, 20):
    list1.append(random.randint(-100, 100))
print(list1)
imin = list1.index(min(list1))
imax = list1.index(max(list1))
list1[imin], list1[imax] = list1[imax], list1[imin]
print(list1)
