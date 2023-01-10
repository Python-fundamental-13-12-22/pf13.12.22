import random

randomlist = []
for i in range(10):
    n = random.randint(1, 100)
    randomlist.append(n)
print(f"Список випадкових чисел: {randomlist}")

max = max(randomlist)
min = min(randomlist)

for i in range(len(randomlist)):
    if randomlist[i] == max:
        randomlist[i] = min
    elif randomlist[i] == min:
        randomlist[i] = max
print(f"Змінений список випадкових чисел: {randomlist}")
