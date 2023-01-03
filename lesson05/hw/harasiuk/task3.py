import random
list = []
minus = 0
plus = 0
noll = 0
for value in range(0, 20):
    list.append(random.randint(-5, 4))
for value in range(len(list)):
    if list[value] < 0:
        minus = minus +1
    elif list[value] > 0:
        plus = plus + 1
    elif list[value] == 0:
        noll = noll +1
print(list)
print(f"Більших нуля:{plus}")
print(f"Менших нуля:{minus}")
print(f"Дорівнює нулю:{noll}")
