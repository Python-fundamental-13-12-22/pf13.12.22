list = []
for value in range(0, 10):
    list.append(int(input(f"input list[{value}]\n")))
suma = sum(list)
dobutok = 1
for value in range(len(list)):
    dobutok = list[value]*dobutok
print(list)
print(f"Sum is: {suma}")
print(f"Product is: {dobutok}")
