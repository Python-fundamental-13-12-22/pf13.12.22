# TASK 1

year = int(input('Введіть рік, який вас цікавить: '))
if year%4==0 and year%100!=0 or year%400 ==0:
    print('It is a leap year!')
else:
    print('This is not a leap year!')

# TASK 2

year = int(input('Введіть рік: '))
month = int(input('Вкажіть місяць: '))
day = int(input('Введіть день: '))
if 0< year < 10000 and 1 <= month <=12 and 1<= day <= 31:
    print('Дата є коректною!')
else:
    print('Нажаль дата не коректна')

# TASK 3
a = int(input('Введіть число а: '))
b = int(input('Введіть число в: '))
c = int(input('Введіть число с: '))
d = b**b - 4*a*c
if d == 0:
    х1 = -b/2*a
    print('Рівняння має 1 корінь: ', f'{x1:.1f}')
elif d > 0:
    x1 = (-b+d**0.5)/2*a
    x2 = (-b-d**0.5)/2*a
    print('Рівняння має 2 корені: ', f'{x1:.1f}','та', f'{x2:.1f}')
else:
    print('Рівняння не має коренів')

# TASK 4

a = int(input('Введіть число a: '))
b = int(input('Введіть число b: '))
c = int(input('Введіть число c: '))
if a + b > c and b + c > a and c + a > b:
    p = a + b + c
    s = (p/2*(p/2-a)*(p/2-b)*(p/2-c))**0.5
    print('Периметр трикутника дорівнює: ', p,'\n'
          'Площа трикутника дорівнює: ' f'{s:.2f}')
else:
    print('Трикутник не можна побудувати')

# TASK 5

k = int(input('Введіть число від 1 до 365: '))
n = k%7
if n == 1:
    print('Понеділок')
elif n == 2:
    print('Вівторок')
elif n == 3:
    print('Середа')
elif n == 4:
    print('Четвер')
elif n == 5:
    print("П'ятниця")
elif n == 6:
    print('Субота')
else:
    n == 0
    print('Неділя')

# TASK  6

import random
fortune = random.randint (1,101)
for c in range (1,11):
    number = int(input('Введіть число від 1 до 100: '))
    if number > fortune:
        print('Нажаль, число більше загаданого')
    elif number < fortune:
        print('Це число є меншим за загадане')
    else:
        number == fortune
        print('Окей ви вгадали!')
        break
print('Ось, яке число загадав компьютер: ', fortune)

# TASK 7

total_numbers = 0
for c in range (1,11):
    number = int(input('Введіть число більше 2: '))
    if number > 2 and number % 5 == 0:
        total_numbers += 1
print('Серед чисел, що ви ввели', total_numbers, 'з них є кратними 5-ти')

# TASK 8

for c in range (1, 10):
    for d in range(1, 10):
        print(c, '*', d, '=', c*d)

# Task 9

for i in range(5):
    for j in range(7):
        if i == 0 or i == 4 or j == 0 or j == 6:
            print('#', end='')
        else:
            print('-', end='')
    print()

# TASK 10
p = int(input('Введіть перше число: '))
h = int(input('ВВедіть друге число: '))
quantity = int(input('Скільки чисел ві хочете порахувати: '))
amount = 0
multiplication = 1
diapason = 0
for c in range (quantity):
    number = int(input('Введіть число: '))
    if number < p:
        amount += number
    if number > h:
        multiplication *= number
    if p < number < h:
        diapason += 1
    if number == p or number == h:
        break
print('Сума чисел, які меншими за 1е введене число складає: ', amount)
print('Добуток чисел, що більші за 2е введене число дорівнює: ', multiplication)
print('Кількість чисел, які знаходяться в діапазоні між 1м та 2м введеним числом є: ', diapason, 'шт')

# TASK 11

quantity = int(input('Скільки чисел ви хочете ввести?: '))
positive_number = 0
negative_number = 0
for c in range (quantity):
    number = int(input('Введіть додатнє або від"ємне число: '))
    if number > 0:
        positive_number += 1
    elif number < 0:
        negative_number += 1
    else:
        break
print('Відсоток додатніх чисел складає:', f'{positive_number/quantity:.0%}')
print('Від"ємних чисел є', f'{negative_number/quantity:.0%}')