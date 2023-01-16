#2. Заповнити список дійсними числами введенням з клавіатури.
#Порахувати суму і добуток елементів списку.
#Вивести на екран сам список, отримані суму і добуток його елементів.

user_list = []
sum_el = 0
product_numbers = 1
for i in range(6):
    n = float(input(f"Enter numbers :"))
    user_list.append(n)
    sum_el += n
    product_numbers += n
print(f"{user_list}\n"
      f"The sum of elements is {sum_el}\n"
      f"The product of numbers is {product_numbers}" )
