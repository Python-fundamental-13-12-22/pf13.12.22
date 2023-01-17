#task1
import random
list1=[]
list2=[]
list3=[]
for a in range(5):
  list1.append(random.randint(1,10))
for a in range(5):
  digit=int(input("Enter a digit: "))
  list2.append(digit)
for a in range(5):
  list3.append(list1[a]+list2[a])
print(f"First list: {list1}")
print(f"Second list: {list2}")
print(f"Third list: {list3}")
#task2
digits=[]
while True:
    digit=input("Enter a digit or 'stop to stop: ")
    if digit=='stop':
        break
    digits.append(float(digit))
print(f"The digits is: {digits}")
sum=0
product=1
for digit in digits:
    sum+=digit
    product*=digit
print(f"The sum of the digits is: {sum}")
print(f"The product of the digits is: {product}")
#task3
import random
random_digits=[]
for x in range(20):
    random_digits.append(random.randint(-5,4))
positive_digits=0
negative_digits=0
zero_digits=0
for digit in random_digits:
    if digit>0:
        positive_digits+=1
    elif digit<0:
        negative_digits+=1
    else:
        zero_digits+=1
print(f"Random digits: {random_digits}")
print(f"Positive digits: {positive_digits}")
print(f"Negative digits: {negative_digits}")
print(f"Zero digits: {zero_digits}")
#task4
import random
random_digits=[]
positive_digits=[]
negative_digits=[]
for x in range(10):
    digits=random.randint(-5,5)
    if digits==0:
        continue
    random_digits.append(digits)
    if digits>0:
        positive_digits.append(digits)
    else:
        negative_digits.append(digits)
print(f"Random digits: {random_digits}")
print(f"Positive digits: {positive_digits}")
print(f"Negative digits: {negative_digits}")
#task5
import random
digits=[random.randint(-100,100)for x in range(10)]
print(f"Random digits: {digits}")
digits=[n for n in digits if n>=0]
print(f"Positive digits: {digits}")
#task6
list1=[]
list2=[]
for x in range(10):
    digit=int(input("Enter a digit: "))
    list1.append(digit)
for x,digit in enumerate(list1):
    if digit%2==0:
        list2.append(x)
print(list2)
#task7
def find_unique_elements(lst):
  unique_elements = []
  for x in lst:
    if lst.count(x) == 1:
      unique_elements.append(x)
  return unique_elements


lst = [1, 2, 2, 4, 5, 6, 6, 8, 3, 7, 3, 6, 2, 6, 3, 2, 8, 9, 3, 2, 5]
unique_elements = find_unique_elements(lst)
print(unique_elements)
#task8
import random
def swap_min_max(digits):
    min_index=digits.index(min(digits))
    max_index=digits.index(max(digits))
    digits[min_index],digits[max_index]=digits[max_index],digits[min_index]
digits=[random.randint(0,100)for x in range(10)]
print(f"Origin digits: {digits}")
swap_min_max(digits)
print(f"Swapped digits: {digits}")
#task9
import random
matrix=[[random.randint(1,10)for a in range(5)]for n in range(5)]
print(f"Matrix digits: {matrix}")
row_sum=[0]*len(matrix)
col_sum=[0]*len(matrix[0])
for a in range(len(matrix)):
    for n in range(len(matrix[0])):
        row_sum[a]+=matrix[a][n]
        col_sum[n]+=matrix[a][n]
print(f"The sum of rows: {row_sum}")
print(f"The sum of cols: {col_sum}")
matrix.append(row_sum)
matrix.append(col_sum)
#task10
import random
matrix=[[random.randint(0,999)for a in range(5)]for n in range(5)]
for row in matrix:
    print(row)
count=0
for row in matrix:
    for digit in row:
        if digit>=10 and digit<100:
            count+=1
print(f"The number of double digits: {count}")
#task11
matrix=[]
for a in range(3):
    raw=[]
    for n in range(3):
        elements=int(input("Enter a digit: "))
        raw.append(elements)
    matrix.append(raw)
for raw in matrix:
    sum=0
    for n in range(3):
        sum+=raw[n]
    raw.append(sum)
    print(raw)
#task12
import random
def max_digit():
    matrix=[[random.randint(1,100)for a in range(4)]for n in range(4)]
    print(f"Matrix random generated digit: {matrix}")
    digit_max=max([max(digit)for digit in matrix])
    return digit_max
print(f"The largest digit calculated: {max_digit()}")
#task13
matrix1=[[1,3,5],[7,9,1],[3,5,7]]
matrix2=[[7,5,3],[1,9,7],[5,3,1]]
matrix_result=[]
for a in range(len(matrix1)):
    row_result=[]
    for n in range(len(matrix1[a])):
        row_result.append(max(matrix1[a][n],matrix2[a][n]))
    matrix_result.append(row_result)
print(f"The result: {matrix_result}")
#task14
matrix=[[0 for a in range(10)]for n in range(10)]
for a in range(10):
    for n in range(10):
        matrix[a][n]=a*10+n
for a in range(10):
    matrix[a][a],matrix[a][9-a]=matrix[a][9-a],matrix[a][a]
for row in matrix:
    print(f"The result: {row}")
#task15
import random
matrix=[[random.randint(0,100)for a in range(5)]for n in range(5)]
print(f"Matrix random generated digits: {matrix}")
def sort_row(matrix):
    first_row=matrix[0]
    first_row.sort()
    indices=[first_row.index(element)for element in first_row]
    sorted_matrix=[[row[index]for index in indices]for row in matrix]
    return sorted_matrix
sorted_matrix=sort_row(matrix)
print(f"Matrix sorted random generated digits: {sorted_matrix}")

