k = int(input("Input k\n"))
l = k % 7
match l:
    case 1:
        n = 'Понеділок'
        print(f'n = {n}')
    case 2:
        n = 'Вівторок'
        print(f'n = {n}')
    case 3:
        n = 'Середа'
        print(f'n = {n}')
    case 4:
        n = 'Четвер'
        print(f'n = {n}')
    case 5:
        n = "П'ятниця"
        print(f'n = {n}')
    case 6:
        n = 'Субота'
        print(f'n = {n}')
    case 0:
        n = 'Неділя'
        print(f'n = {n}')
