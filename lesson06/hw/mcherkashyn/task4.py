def season(month):
    if 1 <= month <= 2 or month == 12:
        seasonName = "Зима"
    elif 3 <= month <= 5:
        seasonName = "Весна"
    elif 6 <= month <= 8:
        seasonName = "Літо"
    elif 9 <= month <= 11:
        seasonName = "Осінь"
    return seasonName

print(season(12))
