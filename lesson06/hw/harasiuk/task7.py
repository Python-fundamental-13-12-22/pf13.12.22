d = int(input("Введіть день\n"))
m = int(input("Введіть місяць\n"))
r = int(input("Введіть рік\n"))


def date(d, m, r):
    correct = True
    if (((m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12)) and (d > 31)):
        correct = False
    if (((m == 4) or (m == 6) or (m == 9) or (m == 11)) and (d > 30)):
        correct = False
    if ((m == 2) and (l == 1) and (d > 29)):
        correct = False
    if ((m == 2) and (l == 0) and (d > 28)):
        correct = False
    if d < 0 or m < 0 or r < 0 or m > 12:
        correct = False
    return correct


print(date(d, m, r))
