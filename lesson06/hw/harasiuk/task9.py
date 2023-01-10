def calc_factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * calc_factorial(n-1)


x = int(input("input x\n"))
print(calc_factorial(x))
