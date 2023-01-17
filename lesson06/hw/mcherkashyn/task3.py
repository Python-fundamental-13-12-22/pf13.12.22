import math
def square(a):
    p = 4*a
    s = a**2
    d = a * math.sqrt(2)
    tuple = (p, s, round(d, 2))
    return tuple

print(square(2))
