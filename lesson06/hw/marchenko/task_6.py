# TASK 6

def is_prime(number):
    if number == 1 or number == 2 or number == 3:
        return True
    elif number % 2 != 0 and number % 3 != 0 and number % 1 == 0 and number % number == 0:
        print (number, 'просте число ')
        return True
    else:
        print(number, 'складне число')
        return False

