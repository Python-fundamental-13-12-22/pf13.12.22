s = int(input("input number\n"))


def season(s):
    pora_roku = ""
    if s == 1 or s == 2 or s == 12:
        pora_roku = "Зима"
    elif 2 < s < 6:
        pora_roku = "Весна"
    elif 5 < s < 9:
        pora_roku = "Літо"
    elif 8 < s < 12:
        pora_roku = "Осінь"
    else:
        pora_roku = "error"
    return pora_roku


print(season(s))
