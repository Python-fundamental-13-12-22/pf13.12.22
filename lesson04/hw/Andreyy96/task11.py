positive_numbers = 0
negative_numbers = 0
numbers = int(input('Введите число: '))

while numbers != 0:
    if numbers >= 0:
        positive_numbers += 1
    else:
        negative_numbers += 1
    numbers = int(input('Введите число: '))

sum_numbers = negative_numbers + positive_numbers

print(f'Процент положительных чисел:  {(positive_numbers/sum_numbers) * 100} %')
print(f'Процент отрицательных чисел:  {(negative_numbers/sum_numbers) * 100} %')
