num=7592
print('number = ', num)
numstr = str(num)
a=int(numstr[0])
b=int(numstr[1])
c=int(numstr[2])
d=int(numstr[3])
print('dobutok = ', a*b*c*d)
print('revers = ', numstr[::-1])
print('sorted =', ''.join(sorted(numstr)))

# rev = '{3:>15d},{2:>10d},{1:<5d},{0:$^5d}'.format(a,b,c,d)
# print('revers = ', rev)

# revers=(numstr[3],numstr[2],numstr[1],numstr[0])
# print ('revers = ', ''.join(revers))

# print('revers = ', numstr[3],numstr[2],numstr[1],numstr[0], sep='')
