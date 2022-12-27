#Задано чотирицифрове натуральне число.

some_number = input()

#- Знайти добуток цифр цього числа.

product_of_numbers = int(some_number[0]) * int(some_number[1]) * int(some_number[2]) * int(some_number[3])

# - Записати число в реверсному порядку.

some_number_reverse = int(some_number[::-1])

# - Посортувати цифри, що входять в дане число

sorted_data = sorted(some_number)
string_data = " ".join(map(str,sorted_data))
sorted_number = int(string_data.replace(" ",""))

print(product_of_numbers)
print(some_number_reverse)
print(sorted_number)