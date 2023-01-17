def arithmetic(a, b, operation):
    result = 0
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        result = a / b
    else:
        print('Неизвестная операция')

    return result

a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
opeation = str(input('Введите арифметическую операцию +, -, *, /: '))

print(arithmetic(a, b, opeation))
