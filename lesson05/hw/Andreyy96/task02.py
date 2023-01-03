list1 = []

for i in range(1, 7):
    number = int(input('Введите число от 1 до 10: '))
    if number < 0:
        print('Число не может быть отрицательным')
        number = int(input('Введите число от 1 до 10: '))
    else:
        list1.append(number)

print(list1)

sum_list = sum(list1)
print(f'Cумма списка {sum_list}')

dobutok_list = 1
for i in list1:
    dobutok_list *= i
print(f'Произведение списка {dobutok_list}')
