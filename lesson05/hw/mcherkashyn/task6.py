import random

randomlist = []
randomlist2 = []

for i in range(20):
    n = random.randint(1, 100)
    randomlist.append(n)
    if randomlist[i] % 2 == 0:
        randomlist2.append(i)
print(f"Список випадкових чисел: {randomlist}")
print(f"Список парних випадкових чисел: {randomlist2}")
