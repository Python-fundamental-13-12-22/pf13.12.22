def is_prime():
    x=int(input("Enter a digit: "))
    if x<2:
        return False
    elif x==2:
        return True
    for a in range(2,x):
        if x%a==0:
            return False
        return True
result=is_prime()
print(f"The result: {result}")