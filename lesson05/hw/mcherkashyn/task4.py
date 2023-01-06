import random

randomlist = []
randomlist2 = []
randomlist3 = []

for i in range(20):
    n = random.randint(-5, 5)
    randomlist.append(n)
    if n > 0:
        randomlist2.append(n)
    elif n < 0:
        randomlist3.append(n)

print(f"Список випадкових чисел: {randomlist}")
print(f"Список випадкових додатніх чисел: {randomlist2}")
print(f"Список випадкових від'ємних чисел: {randomlist3}")
