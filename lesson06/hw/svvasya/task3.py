import math
def square(a):
    result = []
    result.append(a * a)
    result.append(4 * a)
    result.append(math.sqrt((a*a + a*a)))
    return tuple(result)
a = int(input('Введіть сторону квадрата '))
print(square(a))

