"""9. Напишіть функцію `factorial` для обчислення факторіалу числа (цілого невід’ємного числа).
Функція приймає число як аргумент."""


def factorial(n):
    fact = n
    for n in range(1, n):
        fact *= n
    return fact


print(factorial(8))
