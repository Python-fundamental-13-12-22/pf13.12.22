def EvenOddNumber(number):
    try:
        if number // 2 == 0:
            result = 'Entered number is even'
        else:
            result = 'Entered number is odd'
    except:
        result = 'You entered not a number'
    return result

print(EvenOddNumber(4))
print(EvenOddNumber(9))
print(EvenOddNumber('Five'))