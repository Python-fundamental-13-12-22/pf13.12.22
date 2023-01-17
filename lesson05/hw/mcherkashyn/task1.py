import random

input_string = input("Введіть числа через пробіл:")
numbers_list = list(map(int, input_string.split()))
print(f"Список введених чисел: {numbers_list}")

randomlist = []

for i in range(len(numbers_list)):
    n = random.randint(1,100)
    randomlist.append(n)
print(f"Список випадкових чисел: {randomlist}")

result_list = len(randomlist) < len(numbers_list) and randomlist or numbers_list

result = []
for i in range(0, len(result_list)):
    result.append(randomlist[i] + numbers_list[i])
print(f"Список доданих чисел : {result}")
