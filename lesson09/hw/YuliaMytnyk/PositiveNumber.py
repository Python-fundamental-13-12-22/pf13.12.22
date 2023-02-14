class MyError(Exception):
    pass
def check_positive():
    try:
        number=int(input("enter a number: "))
        if number>0:
           return f" You input positive number: {number}"
        elif number<=0:
            raise MyError
    except MyError:
        return  f"You input negative number: {number}. Try again."
    except ValueError:
        return  "Error type: ValueError!"

print(check_positive())
