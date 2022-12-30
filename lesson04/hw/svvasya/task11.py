i_d = 0
i_v = 0
i = 0
a =str(input("введіть декілька додатніх та від ємнихчисел через пробіл "))
a_sp = a.split()
for a_sp in a_sp:
    i = i + 1
    if int(a_sp) > 0:
        i_d = i_d + 1
    elif int(a_sp) < 0:
        i_v = i_v + 1
    elif int(a_sp) == 0:
        break
print (f'Відсоток додатніх {i_d/i*100}%')
print (f'Відсоток відємних {i_v/i*100}%')