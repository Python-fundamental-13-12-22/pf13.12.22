# 5. Нехай `k`- ціле від `1` до `365`. Присвоїти цілій змінній n значення
# (понеділок, вівторок, …, суботу чи неділю) залежно від того , на який
# день тижня припадає `k`-й день не високосного року, в якому 1 січня -
# понеділок.

k = int(input("Введіть день року від 1 до 365 : "))
n = k % 7
match n:
    case 1:
        print("Понеділок")
    case 2:
        print("Вівторок")
    case 3:
        print("Середа")
    case 4:
        print("Четвер")
    case 5:
        print("П'ятниця")
    case 6:
        print("Субота")
    case 7:
        print("Неділя")