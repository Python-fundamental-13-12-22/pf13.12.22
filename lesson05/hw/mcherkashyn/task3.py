import random

randomlist = []

for i in range(20):
    n = random.randint(-5, 4)
    randomlist.append(n)
print(f"Список випадкових чисел: {randomlist}")

z = 0
s = 0
l = 0
for i in randomlist:
    if i == 0:
        z = z + 1
    elif i > 0:
        s = s + 1
    elif i < 0:
        l = l + 1

print(f"Кількість нулів: {z}")
print(f"Кількість додатніх чисел: {s}")
print(f"Кількість від'ємних чисел: {l}")
