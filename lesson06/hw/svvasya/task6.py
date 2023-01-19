def is_prime(a):
    for i in range(2, (a//2)+1):
        if a % i == 0:
            return False
    return True
a = int(input('Введіть число '))
print(is_prime(a))
