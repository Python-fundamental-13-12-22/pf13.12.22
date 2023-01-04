def my_func(a, b, c):
    r = 0
    match c:
        case "+":
            r = a + b
        case "-":
            r = a - b
        case "*":
            r = a * b
        case "/":
            r = a / b
        case _:
            r = "Невідома операція"
    print(r)
    return r


a = int(input("input a\n"))
b = int(input("input b\n"))
c = input("input c\n")
my_func(a, b, c)
