a = []
for i in range(4):
    #a.append([a1=input() for i in range(4)])
    a.append(list(map(int, input('введіть 4 числа через пробіл ').split())))

# сума рядків
s = 0
for i in range(len(a)):
    s_r = 0
    for j in range(len(a[i])):
        s_st = 0
        s_r += a[i][j]
    a[i].append(s_r)
    print(f" Сума {i} рядка {s_r}")
# вивід
print('----------')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()
