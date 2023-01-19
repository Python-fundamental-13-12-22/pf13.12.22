def generate_matrix(n=3, m=3, min_value=0, max_value=100):
    import random
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randint(min_value, max_value))
        matrix.append(row)
    return matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

n = 3 #рядків
m = 3 #стовпців
matrix = generate_matrix(n, m)
print_matrix(matrix)


list1 = []
list2 = []
list3 = []

for i in range(m):
    for j in range(m):
        b = (matrix[j][i])
        list1.append(b)

for i in range(0, len(list1), m):
    list2.append(list1[i:i+m])
    for k in list2:
        t = min(k)
    list3.append(t)

print(f"Максимальний елемент: {max(list3)}")
