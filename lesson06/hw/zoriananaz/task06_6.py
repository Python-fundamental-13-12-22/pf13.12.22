"""6. Написати функцію `is_prime`, яка приймає 1 аргумент - число від 0 до 1000, і повертає True,
 якщо воно просте,і `False` - в іншому випадку."""


def is_prime(num):
    if num < 2:
        return False
    elif num >= 2:
        for i in range(2, num - 1):
            if num % i == 0:
                return False
        return True


print(is_prime(113))
