# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
first_value = input()
second_value = input()

first_value, second_value = second_value, first_value

print(first_value)
print(second_value)

