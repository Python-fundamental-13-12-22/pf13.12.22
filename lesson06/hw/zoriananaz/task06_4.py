""" Написати функцію `season`, яка приймає 1 аргумент - номер місяця (від 1 до 12),
і повертає пору року, якій цей місяцьvналежить (зима, весна, літо або осінь)."""


def season(num_of_month):
    if 0 < num_of_month <= 2 or num_of_month == 12:
        result = "Winter"
    elif 3 <= num_of_month <= 5:
        result = "Spring"
    elif 6 <= num_of_month <= 8:
        result = "Summer"
    elif 9 <= num_of_month <= 11:
        result = "Autumn"
    else:
        result = "Error"
    return result


print(season(12))
print(season(4))
print(season(6))
print(season(9))
print(season(13))
print(season(-2))
