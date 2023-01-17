# У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.
import random
a = [random.randint(-50, 50) for i in range(6)]
print(a)
b = max(a)
c = min(a)
a.insert(a.index(b), c)
a.pop(a.index(b))
a.insert(a.index(c), b)
a.pop(a.index(c))
print(a)
