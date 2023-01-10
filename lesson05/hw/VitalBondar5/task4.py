# 4. Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один помістити тільки додатні, у другий - тільки
# від’ємні. Числа, рівні нулю, ігнорувати. Вивести на екран всі згенеровані випадкові числа і елементи обох списків.
import random
a = []
for i in range(20):
    x = random.randrange(-5, 5)
    a.append(x)
print(a)
dod = []
vid = []
for i in range(20):
    if a[i] > 0:
        dod.append(a[i])
    elif a[i] < 0:
        vid.append(a[i])
print(dod, 'додатні')
print(vid, "від'ємні")
