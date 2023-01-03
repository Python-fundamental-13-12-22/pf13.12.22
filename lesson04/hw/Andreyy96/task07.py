multipel_number = 0
for i in range(0, 11):
    number = int(input('Введить натуральеое число блольше 2: ')) % 5
    if number == 0:
        multipel_number += 1
        print(multipel_number)
    elif number != 0:
        continue
