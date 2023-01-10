""" Нехай `k`- ціле від `1` до `365`. Присвоїти цілій змінній n значення
(понеділок, вівторок, …, суботу чи неділю) залежно від того , на який
день тижня припадає `k`-й день не високосного року, в якому 1 січня -
понеділок"""

k = int(input(f" Enter number: "))

if k in range(1, 366, 7):
    n = "понеділок"
    print(n)
elif k in range(2, 365, 7):
    n = "вівторок"
    print(n)
elif k in range(3, 365, 7):
    n = "середа"
    print(n)
elif k in range(4, 365, 7):
    n = "четвер"
    print(n)
elif k in range(5, 365, 7):
    n = "п'ятниця"
    print(n)
elif k in range(6, 365, 7):
    n = "субота"
    print(n)
elif k in range(7, 365, 7):
    n = "неділя"
    print(n)
