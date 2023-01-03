import random
k = random.randint(0, 100)
print(k)
for i in range (0, 11):
    k1 = int(input("input your number\n"))
    if k1 == k:
        print("Congratulations!")
        break
    elif k1 > k:
        print("Your number is more then my")
    elif k1 < k:
        print("Yor number is less then my")
if k1 != k:
    print(f"My number is {k}")
