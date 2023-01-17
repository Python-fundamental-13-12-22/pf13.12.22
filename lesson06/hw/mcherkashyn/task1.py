def arithmetic(a, b, c):
    if c == "+":
        result = a + b
    elif c == "-":
        result = a - b
    elif c == "*":
        result = a * b
    elif c == "/":
        result = a / b
    else:
        result = "Невідома операція"
    return result

print(arithmetic(2, 3, "+"))
