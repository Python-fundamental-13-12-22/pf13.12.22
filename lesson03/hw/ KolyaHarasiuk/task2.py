num = (input("give a number:\n"))
print("dobutok = ", (int(num[1]) * int(num[2]) * int(num[3]) * int(num[0])))
num_reverse = sorted(num, reverse=True)
print('reverse number :', ''.join(num_reverse))
print('sorted =', ''.join(sorted(num)))