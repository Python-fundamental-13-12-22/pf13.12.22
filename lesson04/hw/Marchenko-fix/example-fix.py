# import math
# import random
#
# #task 1
# year = int(input("Enter year number:"))
# remainder = year % 4
#
# if remainder == 0:
#     print("It's a leap year!")
# elif remainder != 0:
#     print("This is not a leap year!")
#
# #task 2
# year = int(input("Введіть рік:"))
# month = int(input("Введіть номер місяця:"))
# day = int(input("Введіть число дня:"))
# date = f"{day}.{month}.{year}"
#
# if 1 <= month <= 12 and year > 0 and 1 <= day <= 31:
#     print(f"Дата: {date}")
# else:
#     print("Невірна дата")
#
# #task 3
# a = int(input("Введіть число a:"))
# b = int(input("Введіть число b:"))
# c = int(input("Введіть число c:"))
#
# d = (b**2) - (4*a*c)
#
# if d > 0:
#     x1 = ((-b - (math.sqrt(d))) / (2 * a))
#     x2 = ((-b + (math.sqrt(d))) / (2 * a))
#     print(f"Коренями є: {x1} and {x2})")
# elif d == 0:
#     x3 = ((-b - (math.sqrt(d))) / (2 * a))
#     print(f"Єдиний корінь: {x3}")
# else:
#     print("У цьому рівнянні немає коренів")
#
# #task 4
# a = int(input("Введіть число a:"))
# b = int(input("Введіть число b:"))
# c = int(input("Введіть число c:"))
#
# if a > 0 and b > 0 and c > 0:
#     p = (a + b + c)/2
#     s = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print(f"Периметр трекутника: {p} та площа: {s}")
#
# #task 5
# n = int(input("Введіть число, від 1 до 365:"))
# d = "понеділок", "вівторок", "середа", "четвер", "п'ятниця", "субота", "неділя"
# r = n % 7
# result = d[r - 1]
#
# print(f"День тижня:{result}")
#
# #task 6
# number = random.randint(1, 100)
#
# attempts = 0
#
# while attempts < 10:
#     attempt = input(f"Введіть число:")
#     attempt = int(attempt)
#     attempts = attempts + 1
#     if attempt == number:
#         print(f"Ви вгадали! Спроб: {attempts}")
#         break
#     elif attempt != number and attempt < number:
#         attempt_1 = number - attempt
#         print(f"Ваше число невірне, воно менше за потрібне на: {attempt_1}, спроб: {attempts}")
#     elif attempt != number and attempt > number:
#         attempt_2 = attempt - number
#         print(f"Ваше число невірне, воно більше за потрібне на: {attempt_2}, спроб: {attempts}")
# if attempt != number:
#     print(f"Ви не вгадали, потрібне число: {number}, спроб: {attempts}")
#
# #task 7
# foldNumbers = 0
# numbers = 0
#
# while numbers < 10:
#     number = int(input(f"Введіть число:"))
#     remainder = number % 5
#     numbers = numbers + 1
#     if remainder == 0 and number > 2:
#         foldNumbers = foldNumbers + 1
#         print(f"Це число кратне 5, введено кратних чисел: {foldNumbers}")
#     if remainder != 0 and number > 2:
#         print(f"Це число не кратне 5, введено кратних чисел: {foldNumbers}")
# print(f"Усього введено кратних чисел: {foldNumbers}")
#
# #task 8
# number = 2
# numbers = range(1, 10)
#
# for i in numbers:
#     result = number * i
#     print(number, "*", i, "=", result)
#
# #task 9
# N = 4 #висота
# M = 8 #довжина
#
# var = "@" + "%" * (M-2) + "@"
#
# print("@" * M)
# for i in range(N-2):
#     print(var)
# print("@" * M)
#
# #task 10
# P = 10
# H = 34
#
# input_string = input("Введіть числа через пробіл:")
# numbers_list = list(map(int, input_string.split()))
#
# sum = 0
# mul = 1
# num = 0
#
# for i in numbers_list:
#     if int(i) < P:
#         sum += i
#     elif int(i) > H:
#         mul *= i
#     elif P < i < H:
#         num = num + 1
#     elif i == H or i == P:
#         print("Припинення обчислення...")
#         break
# print(f"Сума чисел, які менше P: {sum}")
# print(f"Добуток чисел, які більші за H: {mul}")
# print(f"Кількість чисел, що знаходяться в діапазоні значень від P до H: {num}")
#
# #task 11
# input_string = input("Введіть числа через пробіл:")
# numbers_list = list(map(int, input_string.split()))
#
# list1 = []
# list2 = []
# for i in numbers_list:
#     if i > 0:
#         list1.append(int(i))
#     if i < 0:
#         list2.append(int(i))
#     elif i == 0:
#         print("Закінчення роботи...")
#         break
# percent=(len(list1)*100)/len(numbers_list)
# percent2=(len(list2)*100)/len(numbers_list)
# print(f"Відсоток від'ємних чисел: {percent2} %")
# print(f"Відсоток додатніх чисел: {percent} %")
