list1 = []

for i in range(1, 7):
    number = int(input('Введіть число від 1 до 10: '))
    if number < 0:
        print('Число не може бути менше нуля')
        number = int(input('Введіть число від 1 до 10: '))
    else:
        list1.append(number)

print(list1)

sum_list = sum(list1)
print(f'Cума списку {sum_list}')

dobutok_list = 1
for i in list1:
    dobutok_list *= i
print(f'Добуток списка {dobutok_list}')
