import math
def solve_quadric_equation(a, b, c):
    d = b * b - 4 * a * c
    if d > 0:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print(f'The solution are: x1 = {x1} ,x2 = {x2}')
    elif d == 0:
        x = -b - math.sqrt(d) / 2 * a
        print(f'The solution are: x = {x}')
    else:
        print('Рівняння не має коренів')

try:
    #solve_quadric_equation(1,5,6)
    #solve_quadric_equation(0, 8, 1)
    solve_quadric_equation(1,'abc', 5)
except ZeroDivisionError:
    print('Zero Division Error')
except:
    print('Could not convert string to float')
