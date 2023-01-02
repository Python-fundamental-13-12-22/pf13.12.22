import random

a = [random.randint(-5, 4) for i in range(20)]
count_d = 0
count_v = 0
count_0 = 0
for i in range(0,20):
    if a[i] > 0:
        count_d += 1
    elif a[i] < 0:
        count_v += 1
    elif a[i] == 0:
        count_0 += 1
print('a = ', a)
print(f'Кількість додатніх = ', count_d)
print(f'''Кількість від'ємних = ''', count_v)
print(f'Кількість нульових = ', count_0)

