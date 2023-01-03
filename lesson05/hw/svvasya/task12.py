import random
a1 = [  [random.randint(0, 20) for i in range(6)],
        [random.randint(0, 20) for i in range(6)],
        [random.randint(0, 20) for i in range(6)],
        [random.randint(0, 20) for i in range(6)],
        [random.randint(0, 20) for i in range(6)],
        [random.randint(0, 20) for i in range(6)],
      ]
# вивід
print('---------- початкова матриця')
for i in range(len(a1)):
    for j in range(len(a1[i])):
        print(a1[i][j], end = ' ')
    print()
b = []
for i in range(len(a1)):
    b.append(max(a1[i]))
print('b = ', b)
print(min(b))

