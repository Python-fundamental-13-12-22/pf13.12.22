a = []
d = 1
s = 0
for i in range(10):
    b = float(input('Введіть число '))
    a.append(b)
for i in range(10):
    d = d * a[i]
    s = s + a[i]
print('a = ', a)
print('Сума = ', s)
print('Добуток = ', d)
