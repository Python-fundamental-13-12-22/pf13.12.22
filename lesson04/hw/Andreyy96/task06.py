import random
random_number = random.randint(1, 100)
attempt = 0

while attempt != 10:
    choose_number = int(input('Введите число от 1 до 100: '))
    if choose_number == random_number:
        print(f'Вы угадали число {random_number}')
    elif choose_number > random_number and choose_number < 100:
        print('Введено больше число')
        attempt += 1
    elif choose_number < random_number and choose_number > 0:
        print('Введено меньше число')
        attempt += 1
    elif choose_number > 100 or choose_number < 0:
        print('Введено число за диапозоном')
print(f'А было загадано {random_number}')
