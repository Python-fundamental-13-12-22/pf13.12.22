# Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список. Порахувати кількість додатних,
# від’ємних і нульових елементів. Вивести на екран елементи списку і пораховані кількості.
import random
a = []
for i in range(20):
    x = random.randrange(-5, 4)
    a.append(x)
print(a)
print(a.count(0), 'нулів')
dod = []
vid = []
for i in range(20):
    if a[i] > 0:
        dod.append(a[i])
    elif a[i] < 0:
        vid.append(a[i])
print(len(dod), 'додатних')
print(len(vid), "від'ємних")
