# 4. Задано три довільних числа. Визначити, чи можна побудувати
# трикутник з такими довжинами сторін; Якщо так, то видрукувати його
# периметр та площу.

a = input("Введіть перше число а : \n ")
a = float(a)
b = input("Введіть друге число b : \n ")
b = float(b)
c = input("Введіть третє число  : \n ")
c = float(c)
p = a + b + c
s = (p*(p-a)*(p-b)*(p-b))**0.5
if (a+b)<c or a+c<b or b+c<a:
    print("Трикутник не можна побудувати")
else:
    print('Периметр = ', p, 'Площа = ', s)