"""7. Вводяться десять натуральних чисел більше 2.
Порахувати, скільки серед них чисел, що кратні 5-ти. (не використовувати лісти)"""

ent_number = 0
count_numbers = 0
while ent_number < 10:
    number = int(input(f"Enter number: "))
    if number <= 2:
        print(f"Enter value bigger than 2")
        continue
    elif number % 5 == 0:
        count_numbers += 1
    ent_number += 1
print(count_numbers)


