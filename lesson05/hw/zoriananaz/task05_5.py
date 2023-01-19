#5. Заповнити список випадковими додатними і від’ємними цілими числами.
#Вивести його на екран.
#Видалити з списку всі від’ємні елементи і знову вивести.

import random
rand_list = []
update_list = []
for i in range(1, 30):
    n = random.randint(-10, 10)
    rand_list.append(n)
    if n > 0:
        update_list.append(n)
print(f"All numbers {rand_list}\n"
      f"Positive numbers {update_list}")
