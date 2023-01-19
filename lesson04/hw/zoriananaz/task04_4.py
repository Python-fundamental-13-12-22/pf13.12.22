"""4. Задано три довільних числа. Визначити, чи можна побудувати
трикутник з такими довжинами сторін; Якщо так, то видрукувати його
периметр та площу."""
a = int(input())
b = int(input())
c = int(input())
p = a + b + c
p_half = p / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
if a > 0 and b > 0 and c > 0:
    if (a + b) > c or (a + c) > b or (b + c) > a:
        print(f"Perimeter: {p} Square: {s:.2f}")
else:
    print(f"the triangle can't be created")
