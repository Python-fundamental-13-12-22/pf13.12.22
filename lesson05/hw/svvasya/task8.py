import random
a1 = [random.randint(0, 20) for i in range(10)]
print('a1 = ', a1)
#max = 0
#index = 0
#for i in range(0, 20):
#    if a1[i] > max:
#        max = a1[i]
#        index = i
max_item = max(a1)
max_item_index = a1.index(max_item)
min_item = min(a1)
min_item_index = a1.index(min_item)
a1[max_item_index] = min_item
a1[min_item_index] = max_item
print(a1)

