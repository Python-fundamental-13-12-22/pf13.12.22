def arithmetic(a,b,c):
    result = 0
    if c == "+":
        result = a + b
    elif c == "-":
        result = a - b
    elif c == "*":
        result = a * b
    elif c == "/":
        result = a / b
    else:
        result = 'Невідома арифметична операція'
    return result
a = int(input('Введіть перше число: '))
b = int(input('Введіть друге число: '))
с = str(input('Введіть арифметичну операцію: '))
print(arithmetic(a,b,с))



