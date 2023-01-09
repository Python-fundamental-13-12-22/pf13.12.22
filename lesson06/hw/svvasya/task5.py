def bank(n,years):
    sum = n
    for i in range (1,years+1):
        sum += sum * 0.1
    return sum
n = int(input('Введіть суму внеску '))
years = int(input('Введіть к-ть років '))
print(bank(n,years))

