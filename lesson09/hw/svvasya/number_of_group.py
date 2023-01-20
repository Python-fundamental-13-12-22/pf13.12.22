#from loging_config import logging
class MyError(ArithmeticError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #logging.info("create MyError")
    pass
def check_number_group(number):
    if int(number) < 10:
        raise MyError("We obtain error: Number of your group can't be less than 10")
    else:
        print(f'Number of your group {number} is valid')

try:
    check_number_group(4)      #output:    "We obtain error: Number of your group can't be less than 10 "
    #check_number_group(59)   #output:     "Number of your group 59 is valid"
    #check_number_group("25")              #output:    "Number of your group 25 is valid"
    check_number_group("abc")            #output:     "You entered incorrect data. Please try again."
except MyError as err:
    print(err)
except:
    print("You entered incorrect data. Please try again")
