import random
a1 = [[random.randint(0, 5) for i in range(6)],[random.randint(0, 5) for i in range(6)]]
# вивід
print('---------- початкова матриця')
for i in range(len(a1)):
    for j in range(len(a1[i])):
        print(a1[i][j], end = ' ')
    print()
# сума рядків
s = 0
for i in range(len(a1)):
    s_r = 0
    for j in range(len(a1[i])):
        s_st = 0
        s_r += a1[i][j]
    a1[i].append(s_r)
    print(f" Сума {i} рядка {s_r}")
print('---------- додати стовбець в матрицю ')
for i in range(len(a1)):
    for j in range(len(a1[i])):
        print(a1[i][j], end = ' ')
    print()
print('----------')
# сума стовбців
k_st = len(a1[0])
#print(k_st)
b1 = []
for i in range(k_st):
    s_st = 0
    for j in range(len(a1)):
        s_st += a1[j][i]
    b1.append(s_st)
    print(f" Сума {i} стовбця {s_st}")
a1.append(b1)
# вивід
print('---------- додати рядок в матрицю ')
for i in range(len(a1)):
    for j in range(len(a1[i])):
        print(a1[i][j], end = ' ')
    print()
