def is_prime():
    x=int(input("Enter a number: "))
    if x<2:
        return False
    if x==2:
        return True
    for digit in range(2,x-1):
        if x%digit==0:
            return False
    return True
print(is_prime())