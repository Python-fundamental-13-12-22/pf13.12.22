"""10. Дано число P  і число H. Користувач вводить послідовність чисел.
 Визначити: суму тих чисел, які менше P; добуток чисел, які більші за H; кількість чисел,
 що знаходяться  в діапазоні значень від P до H. При введенні числа рівного P або H,
 припинити обчислення та вивести результат. (не використовувати білдін функції)"""

p = int(input("Enter P:"))
h = int(input("Enter H:"))
result_sum = 0
product_of_numbers = 1
count_value = 1
counter = 0

while True:
    user_value = int(input("Enter your number: "))
    if user_value != p or user_value != h:
        if p > user_value:
            result_sum += user_value
        elif user_value > h:
            product_of_numbers *= user_value
        elif p < user_value < h:
            counter += count_value
    if user_value == h or user_value == p:
        if product_of_numbers == 1:
            print(f"The sum of numbers less than P  is {result_sum}\n"
                  f"There are no numbers greater than H\n"
                  f"In the range between P and H {counter} numbers")
        else:
            print(f"The sum of numbers less than P  is {result_sum}\n"
                  f""f"The product of numbers greater than H is {product_of_numbers}\n"
                  f"In the range between P and H {counter} number(s)")
        break
