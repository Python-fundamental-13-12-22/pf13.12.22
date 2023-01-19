# 8. Вивести на екран таблицю множення (від 1 до 9).
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(i * j, end="\t")
        j += 1
    print()
    i += 1