# 7. У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран.
import random
a = [0]*10
for i in range(10):
    a[i] = random.randint(-5, 5)
print(a)
b = []
for x in a:
    if x not in b:
        b.append(x)
print(b)
