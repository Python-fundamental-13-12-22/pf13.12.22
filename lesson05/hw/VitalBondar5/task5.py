# Заповнити список випадковими додатними і від’ємними цілими числами. Вивести його на екран. Видалити з списку
# всі від’ємні елементи і знову вивести.
import random
l = []
for i in range(10):
    x = random.randrange(-50, 50)
    l.append(x)
print(l)
dod = []
vid = []
for i in range(10):
    if l[i] >= 0:
        dod.append(l[i])
print(dod, 'додатні і нулі')


# # for i in range(0, 7):
# #     if a[i] >= 0:
# #         continue
# #     elif a[i] < 0:
# #         a.remove(a[i])
# # print(a)
#
# for i in range(0, 8):
#     if a[i] < 0:
#         a.remove(a[i])
# print(a)
