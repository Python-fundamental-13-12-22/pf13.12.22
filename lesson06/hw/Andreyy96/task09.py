def factorial(number):
    if number == 0 or number == 1:
        return  1
    return factorial(number-1) * number

number = int(input('Введите число: '))
print(f'Факториал {number}: {factorial(number)}')