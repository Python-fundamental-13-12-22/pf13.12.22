import random
a1 = [  [random.randint(0, 20) for i in range(5)],
        [random.randint(0, 20) for i in range(5)],
        [random.randint(0, 20) for i in range(5)],
        [random.randint(0, 20) for i in range(5)],
        [random.randint(0, 20) for i in range(5)],

      ]
# вивід
print('---------- початкова матриця')
for i in range(len(a1)):
    for j in range(len(a1[i])):
         print(str(a1[i][j]).center(4), end = ' ')
    print()
a1[0].sort()
print('---------- перестановка стовбців матриці')
for i in range(len(a1)):
    for j in range(len(a1[i])):
         print(str(a1[i][j]).center(4), end = ' ')
    print()
