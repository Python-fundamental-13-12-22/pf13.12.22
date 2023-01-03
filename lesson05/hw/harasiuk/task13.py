n = input('n=\n')
m = input("m=\n")
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()
m1 = []
m2 = []
m3 = []
for i in range(0, n):
    row = []
    for j in range(0, m):
        row.append(int(input(f"m1[{i}][{j}]=")))
    m1.append(row)
for i in range(0, n):
    row = []
    for j in range(0, m):
        row.append(int(input(f"m2[{i}][{j}]=")))
    m2.append(row)
print("m1 matrix:")
print_matrix(m1)
print("m2 matrix:")
print_matrix(m2)
for i in range(0, n):
    row = []
    for j in range(0,m):
        row.append(max(m1[i][j], m2[i][j]))
    m3.append(row)
print("m3 matrix:")
print_matrix(m3)
