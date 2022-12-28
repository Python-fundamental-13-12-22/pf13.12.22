a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a == 0 or b == 0 or c == 0:
    print('Длина стороны не может быть меньше или равной 0')
elif (a + b) > c and (b + c) > a and (a + c) > b:
    print('Из длины сторон можно построить треугольник')
    p = a + b + c
    print(f'p = {p}')
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f's = {s}')
else:
    print('Треугольник не может быть построен')
