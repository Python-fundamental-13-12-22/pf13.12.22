"""11. Напишіть функцію `greatest_common_denominator` яка приймає три натуральних числа і повертає
 їхній найбільший спільний дільник."""


def greatest_common_denominator(a, b, c):
    d = []
    for i in range(1, max(a, b, c)):
        if a > 0 and b > 0 and c > 0:
            if a % i == 0 and b % i == 0 and c % i == 0:
                d.append(i)
        else:
            d.append("Error")
    return max(d)


print(greatest_common_denominator(21, 3, 9))
