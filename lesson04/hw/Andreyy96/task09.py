n = 9
m = 7

for i in range(n):
    if i == 0 or i == 8:
        for j in range(m + 1):
            print('!', end='')
        print('!', end='\t')
        print()
    else:
        print('!', end='')
        for j in range(m):
            print('*', end='')
        print('!', end='\t')
        print()
