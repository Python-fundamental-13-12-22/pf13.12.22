"""6. У програмі генерується випадкове ціле число від 0 до 100.
Користувач повинен його відгадати не більше ніж за 10 спроб.
Після кожної невдалої спроби повинно повідомлятися чи більше чи менше введене користувачем число, ніж те,
 що загадане. Якщо за 10 спроб число не відгадане, то вивести загадане число."""
import random

number = random.randint(0, 100)
choice = 0
while choice < 10:
    turn = int(input(f"Enter number: "))
    if turn == number:
        print(f"Congrats! You win. Number is {number}")
        break
    elif turn > number:
        print(f" Your turn is biggest than number")
    elif turn < number:
        print(f"Your turn is less than number")
    choice += 1
