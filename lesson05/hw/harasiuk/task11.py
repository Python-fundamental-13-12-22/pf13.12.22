def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()
m = []
for i in range(0, 4):
    row = []
    k = 0
    for j in range(0, 5):
        if j == 4:
            row.append(k)
        else:
            l = int(input(f"a[{i}][{j}]="))
            row.append(l)
            k = k + row[j]
    m.append(row)
print_matrix(m)
