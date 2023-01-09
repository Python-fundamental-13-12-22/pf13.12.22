def season(number):
    if number == 1 or number == 2 or number == 12:
        seaz = 'Зима'
    elif 3 <= number <= 5:
        seaz = 'Весна'
    elif 6 <= number <= 8:
        seaz = 'Літо'
    elif 9 <= number <= 12:
        seaz = 'Осінь'
    else:
        seaz = 'Некоректний ввід'
    return seaz

number = int(input('Введіть номер місяця від 1 до 12 '))
print(season(number))
