# TASK 1

import random
list1 = []
list2 = []
list3 = []

for a in range(10):
    list1.append(random.randint(1,100))
for b in range(10):
    numbers = int(input('Ведіть будь-яке число: '))
    list2.append(numbers)
for c in range(10):
    list3.append(list1[c]+list2[c])

print ('Перший список: ', list1)
print ('Другий список: ', list2)
print ('Третій список: ', list3)

# TASK 2

list = []

while True:
    numbers = int(input('Введіть декілька дійсних чисел (Для завершення введіть 0): '))
    if numbers <= 0:
        break
    list.append(numbers)
sum = 0
multiplication = 1
for c in list:
    sum += c
    multiplication *= c

print('Ваш список чисел: ', list)
print('Сума чисел: ', sum)
print('Добуток чисел: ', multiplication)

# TASK 3

import random

list = []
for c in range(20):
    list.append(random.randint(-4,5))

negative = 0
positive = 0
zero = 0
for number in list:
    if number < 0:
        negative += 1
    elif number > 0:
        positive += 1
    else:
        zero += 1
print('Список чисел: ', list)
print('Кількість від"ємних чисел: ', negative)
print('Кількість додатніх чисел: ', positive)
print('Кількість нульових чисел: ', zero)

# TASK 4

import random

list = []
positive_numbers = []
negative_numbers = []
for c in range(20):
    list.append(random.randint(-5,5))
for number in list:
    if number < 0:
        negative_numbers.append(number)
    elif number > 0:
        positive_numbers.append(number)
print('Усі сгенеровані числа: ', list)
print('Усі додатні числа: ', positive_numbers)
print('Усі від"ємні числа: ', negative_numbers)

# TASK 5

import random

list = []
positive_list = []
for c in range(20):
    list.append(random.randint(-50,50))
print('Загальний список чисел: ',list)
for number in list:
    if number > 0:
        positive_list.append(number)
print('Список додатніх чисел із загального списку: ',positive_list)

# TASK 6

import random

list = []
list2 = []
for c in range(20):
    list.append(random.randint(1,50))
for number in range(len(list)):
    if list[number] % 2 == 0:
        list2.append(number)
print('Список №1', list)
print('Індекси парних чисел', list2)

# TASK 7

import random

list = []
uniq_list = []

for c in range(20):
    list.append(random.randint(1,100))
for number in list:
    if list.count(number) == 1:
        uniq_list.append(number)
print('Список випадкових чисел', list)
print('Список унікальних чисел', uniq_list)

# TASK 8

import random

list = []
for c in range(20):
    list.append(random.randint(1,30))
print('Список випадкових чисел: ',list)
min_num = min(list)
max_num = max(list)
min_index = list.index(min_num)
max_index = list.index(max_num)
list[min_index], list[max_index] = list[max_index], list[min_index]
print('Список зі зміненими елементами: ',list)

# TASK 9

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
row_sums = []
col_sums = []

for row in matrix:
    row_sums.append(sum(row))

for col in range(len(matrix[0])):
    col_sums.append(sum(row[col] for row in matrix))

for i, row in enumerate(matrix):
    matrix[i].append(row_sums[i])
matrix.append(col_sums)

for count, row in enumerate(matrix):
    if count == 0:
        print(str(row))
    elif count ==3:
        print(str(row))
    else:
        print(row)

# TASK 10

matrix = []

for i in range(0, 999, 10):
  sublist = []
  for j in range(i, i+10):
    sublist.append(j)
  matrix.append(sublist)


for i, sublist in enumerate(matrix):
  if i < len(matrix) - 1:
    print(sublist)
  else:
    print(sublist)

count = 0
for sublist in matrix:
  for element in sublist:
    if element >= 10 and element < 100:
      count += 1

print('Кількість двозначних чисел: ',count)

# TASK 11

matrix = [[0] * 4 for i in range(5)]
for i in range(5):
  for j in range(3):
    matrix[i][j] = int(input(f'Введіть число [{i}][{j}]: '))
for i in range(5):
  matrix[i][3] = sum(matrix[i][:3])
for row in matrix:
  print(row)

# TASK 12

import random
matrix = []
for j in range(10):
    row = []
    for i in range(5):
        row.append(random.randint(1,40))
    matrix.append(row)
for i, row in enumerate(matrix):
    print(row)
max_min = -1
for i in range(10):
  min_element = 41
for j in range(5):
    if matrix[i][j] < min_element:
        min_element = matrix[i][j]
    if min_element > max_min:
        max_min = min_element
print('Максимальний елемент серед мінімальних є: ', max_min)

# TASK 13

rows = int(input('Введіть розмір матриці: '))
cols = int(input('Введіть розмір матриці: '))
matrix1 = [[int(input(f'Введіть число [{i}][{j}] для 1 матриці: ')) for j in range(cols)] for i in range(rows)]
matrix2 = [[int(input(f'Введіть число [{i}][{j}] для 2 матриці: ')) for j in range(cols)] for i in range(rows)]
matrix3 = [[max(matrix1[i][j], matrix2[i][j]) for j in range(cols)] for i in range(rows)]
print(matrix1)
print(matrix2)
for row in matrix3:
  print(row)

# TASK 14

import random
matrix = []
for j in range(10):
  row = []
  for i in range(10):
    row.append(random.randint(1, 10))
  matrix.append(row)
for i, row in enumerate(matrix):
  print(row)
for i in range(10):
  matrix[i][i], matrix[i][9 - i] = matrix[i][9 - i], matrix[i][i]
print()
print('Модифікована матриця: ')
for row in matrix:
  print(row)

# TASK 15

import random
matrix = []
for j in range(5):
    row = []
    for i in range(5):
        row.append(random.randint(1,10))
    matrix.append(row)
for i, row in enumerate(matrix):
    print(row)
matrix[0] = sorted(matrix[0])
print()
print('Модифікована матриця: ')
for row in matrix:
    print(row)
