def arifmetic(a,b,operation):
    if operation == '+':
        return a+b
    elif operation == '-':
        return a-b
    elif operation == '*':
        return a*b
    elif operation == '**':
        return a**b
    elif operation == '/':
        return a/b
    else:
        return 'Invalid operation'
a=int(input("Enter a digit: "))
b=int(input("Enter a second digit: "))
operation=input("Enter a symbol(+,-,*,**,/): ")
result=arifmetic(a,b,operation)
print(f"The result: {result}")