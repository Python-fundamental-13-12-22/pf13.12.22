import random

randomlist = []

for i in range(20):
    n = random.randint(-100, 100)
    randomlist.append(n)
print(f"Список випадкових чисел: {randomlist}")

r = randomlist[:]
for item in randomlist:
    if item < 0:
        r.remove(item)
print(f"Список додатніх випадкових чисел: {r}")
