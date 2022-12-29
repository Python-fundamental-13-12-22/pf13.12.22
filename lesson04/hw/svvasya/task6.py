import random
a = random.randint(0, 100)
i = 1
while i<=10:
     b = int(input('Введіть число від 0 до 100  '))
     if b == a:
         print('Молодець! загадане число: ')
         break
     elif b != a and b>a:
         print('Забагато!!!')
         i = i + 1
     elif b != a and b<a:
         print('Замало!!!')
         i = i + 1
print(a)