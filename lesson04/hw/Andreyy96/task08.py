a = 1

while a <= 9:
    b = 1
    while b <= 9:
        print(f'{b} * {a} = {a * b}', end="\t")
        b += 1
    print()
    a += 1
