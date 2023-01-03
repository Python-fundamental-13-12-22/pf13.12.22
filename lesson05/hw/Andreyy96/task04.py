import random

negative_list = []
positive_list = []
cycle_number = 15

for i in range(cycle_number):
    number = random.randint(-5, 5)
    print(number, end='\t')
    if number > 0:
        positive_list.append(number)
    elif number < 0:
        negative_list.append(number)
    elif number == 0:
        continue
    else:
        break

print()
print(positive_list)
print(negative_list)
