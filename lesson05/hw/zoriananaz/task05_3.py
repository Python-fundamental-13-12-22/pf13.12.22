#3. Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список.
#Порахувати кількість додатних, від’ємних і нульових елементів.
#Вивести на екран елементи списку і пораховані кількості.
import random
rand_list = []
positive_numbers = 0
negative_numbers = 0
null_numbers = 0
for i in range(1, 21):
    n = random.randint(-5, 4)
    rand_list.append(n)
    if n > 0:
        positive_numbers += 1
    if n < 0:
        negative_numbers += 1
    if n == 0:
        null_numbers += 1
print(f"{rand_list}\n"
      f"The positive numbers are {positive_numbers}\n"
      f"The negative numbers are {negative_numbers}\n" 
      f"The null numbers are {null_numbers}")
