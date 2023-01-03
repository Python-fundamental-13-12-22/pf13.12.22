a = {}
lenght = int(input("Скільки чисел ви хочете ввести?\n"))
for i in range (0, lenght):
    a[i] = int(input("input number\n"))
p = int(input("input p\n"))
h = int(input('input h\n'))
sum = 0
dob = 1
k = 0
for i in range(0, lenght):
    if a[i] < p:
        sum = sum + a[i]
    if a[i] > h:
        dob = dob * a[i]
    if a[i] == p or a[i] == h:
        break
    if p < a[i] < h:
        k = k + 1
print(f"Чисел між p і h = {k}")
print(f'sum = {sum}')
print(f'dob = {dob}')
