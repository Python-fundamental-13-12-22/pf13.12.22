k = int(input("Введите число от 1 до 365: "))
n = 7

if (k - 1) % 7 < n:
    k = k % 10
    if k == 1:
        print('Понедельник')
    elif k == 2:
        print('Вторник')
    elif k == 3:
        print('Среда')
    elif k == 4:
        print('Четверг')
    elif k == 5:
        print('Пятница')
    elif k == 6:
        print('Субота')
    elif k == 7:
        print('Воскресение')
