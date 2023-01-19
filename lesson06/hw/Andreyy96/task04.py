def season(month):
    winter = ( 1, 2, 12)
    spring = (3, 4, 5)
    summer = (6, 7, 8)
    autumn = (9, 10, 11)
    season_month = ''

    if month in winter:
        print(f'Этот месяц принадлежит к зиме')
        season_month = 'Зима'
    elif month in spring:
        print(f'Этот месяц принадлежит к весне')
        season_month = 'Весна'
    elif month in summer:
        print(f'Этот месяц принадлежит к лету')
        season_month = 'Лето'
    elif month in autumn:
        print(f'Этот месяц принадлежит к осени')
        season_month = 'Осень'
    else:
        print(f'Число {month} не принадлежит ни к одному сезону')

    return season_month

month = int(input('Введите номер месяца: '))
print(season(month))
