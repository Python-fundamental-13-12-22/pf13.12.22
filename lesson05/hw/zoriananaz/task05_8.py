#8. У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.
import random
rand_list = []
for i in range(10):
    n = random.randint(1, 10)
    rand_list.append(n)

rand_list_copy = rand_list[:]
max_val = max(rand_list_copy)
ind_max_val = rand_list_copy.index(max_val)
min_val = min(rand_list_copy)
ind_min_val = rand_list_copy.index(min_val)
rand_list_copy.insert(ind_max_val, min_val)
rand_list_copy.insert(ind_min_val, max_val)
print(f"Initial list is {rand_list}\n"
      f"Max value is {max_val}\n"
      f"Index max value is {ind_max_val}\n"
      f"Min value is {min_val}\n"
      f"Index min value is {ind_min_val}\n"
      f"Update list {rand_list_copy}")
