n = int(input("input N\n"))
m = int(input("input M\n"))
for j in range(0, m):
    if j == 0 or j == m-1:
        print("*"*n)
    else:
        print("*", "|"*(n-2), "*", sep='')
