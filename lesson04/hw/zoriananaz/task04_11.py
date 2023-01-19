#11. Для чисел, що вводяться користувачем, визначити відсоток додатних та від’ємних чисел.
#При введенні числа 0 закінчити роботу.

negative_value = 0
positive_value = 0
while True:
    user_value = int(input(f"Enter number: "))
    if user_value < 0:
        negative_value += 1
    elif user_value > 0:
        positive_value += 1
    elif user_value == 0:
        all_number = positive_value + negative_value
        proc_negative = negative_value / all_number * 100
        proc_positive = positive_value / all_number * 100
        print(f"Procent negative values is {proc_negative:.2f}\n"
              f"Procent positive values is {proc_positive:.2f}")
        break
