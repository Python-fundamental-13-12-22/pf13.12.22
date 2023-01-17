def bank():
    n=int(input("Enter the sum of deposit(UA): "))
    years=int(input("Enter a period: "))
    for a in range(years):
     sum=n+n*0.1
    return sum
print(f"Received amount of money(UA): {bank()} ")
