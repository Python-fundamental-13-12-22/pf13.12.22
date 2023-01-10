#8. Вивести на екран таблицю множення (від 1 до 9).

for n in range(1, 10):
    for m in range(1, 10):
        result = n * m
        print(f"{n} * {m} = {result}")
    print()
