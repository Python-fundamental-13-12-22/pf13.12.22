"""11. Матриця 5x4 заповнюється введенням з клавіатури (крім останніх елементів рядків).
Програма повинна обчислювати суму введених елементів кожного рядка і записувати її в останній рядок.
Наприкінці слід вивести отриману матрицю."""


m = []
for i in range(5):
    m.append([0] * 4)

for i in range(5):
    for j in range(4):
        m[i][j] = int(input("enter number:"))
        m[i][-1] = sum(m[i][:-1])


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end="\t")
        print()


print_matrix(m)
