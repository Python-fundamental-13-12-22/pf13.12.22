# ##5


k = int(input('Введіть число від 1 до 365 '))
n = k%7
#print(n)
if  (n == 1):
    print('Понеділок')
elif (n == 2):
    print('Вівторок')
elif (n == 3):
    print('Середа')
elif (n == 4):
    print('Четвер')
elif (n == 5):
    print('''П'ятниця''')
elif (n == 6):
    print('Субота')
elif (n == 0):
    print('Неділя')

