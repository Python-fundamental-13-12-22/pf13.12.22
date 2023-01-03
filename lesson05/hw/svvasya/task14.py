import random
a1 = [  [random.randint(0, 20) for i in range(10)],
        [random.randint(0, 20) for i in range(10)],
        [random.randint(0, 20) for i in range(10)],
        [random.randint(0, 20) for i in range(10)],
        [random.randint(0, 20) for i in range(10)],
        [random.randint(0, 20) for i in range(10)],
        [random.randint(0, 20) for i in range(10)],
        [random.randint(0, 20) for i in range(10)],
        [random.randint(0, 20) for i in range(10)],
        [random.randint(0, 20) for i in range(10)],
      ]
# вивід
print('---------- початкова матриця')
for i in range(len(a1)):
    for j in range(len(a1[i])):
         print(str(a1[i][j]).center(4), end = ' ')
    print()

# вивід
print('---------- головна діагональ матриця на 444')
for i in range(len(a1)):
    for j in range(len(a1[i])):
        if i==j:
            a1[i][j] = 444
        print(str(a1[i][j]).center(4), end = ' ')
    print()
print('---------- бічна діагональ матриця на 777')
for i in range(len(a1)):
    for j in range(len(a1[i])):
        if i+j == 9 :
            a1[i][j] = 777
        print(str(a1[i][j]).center(4), end = ' ')
    print()
