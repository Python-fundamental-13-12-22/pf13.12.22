# ##10
P = 10
H = 100
s = 0
d = 1
i = 0
a =str(input("введіть декілька чисел через пробіл "))
a_sp = a.split()
for a_sp in a_sp:
    if int(a_sp) < P:
        s = s + int(a_sp)
    elif int(a_sp) > H:
        d = d * int(a_sp)
    elif P < int(a_sp) < H:
        i = i + 1
    elif int(a_sp) == P or int(a_sp) == H:
        break
print ('Сума = ', s)
print ('Добуток = ', d)
print ('Кількість = ', i)