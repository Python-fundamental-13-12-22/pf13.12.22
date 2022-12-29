# ##4
import math
a = int(input('Введіть a '))
b = int(input('Введіть b '))
c = int(input('Введіть c '))
if (a+b) > c and (c+b) > a and (a+c) > b:
    p=a+b+c
    print("p=", p, "s=", math.sqrt(p/2*(p/2-a)*(p/2-b)*(p/2-c)))
else:
    print("Трикутник не можна побудувати")
