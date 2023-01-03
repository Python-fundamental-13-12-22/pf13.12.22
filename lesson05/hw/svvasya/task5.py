import random

a = [random.randint(-5, 5) for i in range(20)]
print('a = ', a)
a_v = [value for value in a if value < 0 ]
print(f'''Від'ємні = ''', a_v)


