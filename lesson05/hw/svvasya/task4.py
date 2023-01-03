import random

a = [random.randint(-5, 5) for i in range(20)]
a_d = []
a_v = []
count_0 = 0
for i in range(0,20):
    if a[i] > 0:
        a_d.append(a[i])
    elif a[i] < 0:
        a_v.append(a[i])

print('a = ', a)
print(f'Додатні = ', a_d)
print(f'''Від'ємні = ''', a_v)


