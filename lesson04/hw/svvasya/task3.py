# ##3
import math
a = int(input('Введіть a '))
b = int(input('Введіть b '))
c = int(input('Введіть c '))

d = b*b - 4*a*c
if d>=0:
    x1 = -b-math.sqrt(d)/2*a
    x2 = -b+math.sqrt(d)/2*a
    print('Корені рівняння: ',x1 ,x2)
else:
    print('Рівняння не має коренів')
