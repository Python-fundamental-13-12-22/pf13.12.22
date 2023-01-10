input_string = input("Введіть дійсні числа через пробіл:")
numbers_list = list(map(int, input_string.split()))
print(f"Список введених чисел: {numbers_list}")

s = 0
m = 1
for i in numbers_list:
    s = s + i
print(f"Сума елементів: {s}")

for i in numbers_list:
    m = m * i
print(f"Добуток елементів: {m}")
