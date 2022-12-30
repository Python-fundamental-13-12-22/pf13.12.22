# ##9

n = int(input('введіть n '))
m = int(input('введіть m '))
for j in range (1,m):
    if j == 1 or j == m-1:
        print("+".center(2)*n)
    else:
        print("+", "-".center(2)*(n-2), "+")