a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

discr = (b ** 2) - (4 * a * c)
print('Дискриминант = ' + str(discr))

if discr > 0:
    x1 = (-b + discr**0.5) / (2 * a)
    x2 = (-b - discr**0.5) / (2 * a)
    print(f'x1 = {str(x1)}')
    print(f'x2 = {str(x2)}')
elif discr == 0:
    x1 = -b / (2 * a)
    print(f'x1 = {str(x1)}')
else:
    print('Корней нет')
