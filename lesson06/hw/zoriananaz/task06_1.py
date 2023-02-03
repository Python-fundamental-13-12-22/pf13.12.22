"""1. Написати функцію `arithmetic`, яка приймає 3 аргументи: перші 2 - числа, третій - операцію,
яка повинна бути здійснена над ними.
Якщо третій аргумент +, додати їх;
якщо -, то відняти; * - помножити;
   / - розділити (перше на друге).
   В інших випадках повернути рядок "Невідома операція"."""


def arithmetic(num1, num2, operation):
    if operation == "+":
        result = num1 + num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    else:
        result = "error"

    return result


print(arithmetic(3, 2, "+"))
print(arithmetic(3, 2, "-"))
print(arithmetic(3, 2, "/"))
print(arithmetic(3, 2, "*"))
print(arithmetic(3, 2, ","))
