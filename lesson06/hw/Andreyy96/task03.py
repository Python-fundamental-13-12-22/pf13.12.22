def square(number):
    p = number * 4
    s = number * number
    d = ((number ** 2) / 2) ** 0.5
    tuple_answer = (p, s, d)

    return tuple_answer

number =  int(input('Введите число: '))
tuple_answer = square(number)
print(tuple_answer)
