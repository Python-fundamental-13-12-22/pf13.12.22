def bank(n, years):
    for money in range(0, years):
        n *= 1.1

    return n


n = int(input('Введите число депозита: '))
years = int(input('Введите число на сколько лет открывается депозита: '))
print(f'При вложении {n} денег на депозит строком на {years} у вас на счету будет: {bank(n, years)}')
