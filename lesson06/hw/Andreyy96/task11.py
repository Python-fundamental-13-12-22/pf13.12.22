def greatest_common_denominator(n1, n2, n3):
    if n1 > n2 > n3:
        temp = n3
    elif n3 > n2 > n1:
        temp = n1
    else:
        temp = n2

    for i in range(1, temp + 1):
        if n1 % i == 0 and n2 % i == 0 and n3 % i == 0:
            print(f'Делители: {i}')
            common_denominator = i
    return common_denominator

n1 = int(input('Введите число n1: '))
n2 = int(input('Введите число n2: '))
n3 = int(input('Введите число n3: '))
common = greatest_common_denominator(n1, n2, n3)
print(f'Общий делитель: {common}')
