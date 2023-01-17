def season():
    season=int(input("enter a month: "))
    if season==12 or season==1 or season==2:
        print("winter")
    elif season==3 or season==4 or season==5:
        print("spring")
    elif season==6 or season==7 or season==8:
        print("summer")
    elif season==9 or season==10 or season==11:
        print("autumn")
    else:
        print("incorrect month")
month=season()
print(month)
