p = 20
h = 30
sum_number = 0
dobutok_number = 1
numbers_in_the_range = 0
number = int(input('Введиет число: '))

while number != p or number != h:
    if number > p and number < h:
        numbers_in_the_range += 1
    elif number < p:
        sum_number += number
    elif number > h:
        dobutok_number *= number
    elif number == p or number == h:
        break
    else:
        pass

    number = int(input('Введиет число: '))

print(f'Сумма чисел которые меньше p: {sum_number}')
print(f'Произведение чисел которые больше h: {dobutok_number}')
print(f'Количество чисел в диапозоне p и h: {numbers_in_the_range}')
