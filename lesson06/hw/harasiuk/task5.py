n = int(input("введіть суму\n"))
years = int(input("Введіть кількість років\n"))


def bank(n, years):
    for i in range(0, years):
        n = n * 1.1
    return n


print(f"якщо ви вкладете {n} грн на {years} рокыв то отримаєте {bank(n, years)}")
