def is_prime(number):
    p = 0
    for i in range(2, number // 2+1):
        if number % i == 0:
            p +=1
    if p <= 0:
        key = True
    else:
        key = False

    return key

number = int(input('Введите число от 0 до 1000: '))
print(f'Число {number} простое?')
print(is_prime(number))
