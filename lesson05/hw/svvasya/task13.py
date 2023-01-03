a = []
print('ввід 1 матриці')
for i in range(2):
    #a.append([a1=input() for i in range(4)])
    a.append(list(map(int, input('введіть 4 числа через пробіл ').split())))
b = []
print('ввід 2 матриці')
for i in range(2):
    #a.append([a1=input() for i in range(4)])
    b.append(list(map(int, input('введіть 4 числа через пробіл ').split())))
c = []

# сума елементів
for i in range(len(a)):
    c1 = []
    for j in range(len(a[i])):
        c1.append(int(a[i][j])+int(b[i][j]))
    c.append(c1)
# вивід a
print('a ----------')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()
# вивід b
print('b ----------')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(b[i][j], end = ' ')
    print()
# вивід c
print('c ----------')
for i in range(len(a)):
   for j in range(len(a[i])):
      print(c[i][j], end = ' ')
   print()
