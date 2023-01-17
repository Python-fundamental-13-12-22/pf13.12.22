def factorial(*arg):
    for i in arg:
        if i > 0 and type(i) == int:
            f = 1
            for j in range(1, i + 1):
                f = f * j
            print(f)

factorial(4, 7)
