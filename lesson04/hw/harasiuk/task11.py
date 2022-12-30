k = 0
l = 0
while True:
    num = int(input("Введіть своє число\n"))
    if num == 0:
        break
    elif num > 0:
        k = k+1
    elif num < 0:
        l = l + 1
    print(f"Відсоток додатніx чисел = {(k/(k+l))*100}%, Відсоток від'ємних чисел = {(l/(k+l))*100}%")
