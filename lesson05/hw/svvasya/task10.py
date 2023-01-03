import random
a1 = [  [random.randint(0, 999) for i in range(6)],
        [random.randint(0, 999) for i in range(6)],
        [random.randint(0, 999) for i in range(6)],
        [random.randint(0, 999) for i in range(6)],
        [random.randint(0, 999) for i in range(6)],
        [random.randint(0, 999) for i in range(6)],
      ]
# вивід
print('---------- початкова матриця')
for i in range(len(a1)):
    for j in range(len(a1[i])):
        print(a1[i][j], end = ' ')
    print()
count_dv = 0
for i in range(len(a1)):
    for j in range(len(a1[i])):
        if a1[i][j] // 100 == 0 and a1[i][j] // 10 != 0 :
            count_dv += 1
print(count_dv)

