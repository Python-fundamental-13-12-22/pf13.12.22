def season():
    month=int(input("Enter a month: "))
    if month==12 or month==1 or month==2:
        print("winter")
    elif month==3 or month==4 or month==5:
        print("spring")
    elif month==6 or month==7 or month==8:
        print("summer")
    elif month==9 or month==10 or month==11:
        print("autumn")
    else:
        print("Invalid month!")
months=season()
print(months)
