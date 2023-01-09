def factorial(chyslo):
    fact = 1
    for i in range(1,chyslo+1):
        fact = fact*i
    print(fact)
chyslo = int(input('Введіть число  '))
factorial(chyslo)
