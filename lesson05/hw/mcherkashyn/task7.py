input_string = input("Введіть числа через пробіл:")
numbers_list = list(map(int, input_string.split()))
print(f"Список введених чисел:{numbers_list}")

uniqueNumbersList = []

for i in numbers_list:
    if numbers_list.count(i) == 1:
        uniqueNumbersList.append(i)
print(f"Список унікальних чисел:{uniqueNumbersList}")
