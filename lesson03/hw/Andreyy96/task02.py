#2.1 ?
numbers = 4892

n1 = numbers % 10
numbers //= 10
n2 = numbers % 10
numbers //= 10
n3 = numbers % 10
numbers //= 10
n4 = numbers % 10

a = f'Добуток {n1} * {n2} * {n3} * {n4}: {n1 * n2 * n3 * n4}'
print(a)

#2.2
numbers = 4892
str_number = str(numbers)

revers = "".join(reversed(str_number))
print(revers)
print(type(revers))

revers = int(revers)
print(revers)
print(type(revers))



#2.3
numbers = 4892
str_number = "".join(sorted(str_number))
print(str_number)
print(type(str_number))

int_number = int(str_number)
print(int_number)
print(type(int_number))