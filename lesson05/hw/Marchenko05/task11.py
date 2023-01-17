def generate_matrix(n=4, m=5):
    matrix = []
    for i in range(n):
        row = []
        sum_numbers = 0
        for j in range(m - 1):
            number = int(input(f'Введіть число: '))
            sum_numbers += number
            row.append(number)
        row.append(sum_numbers)
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

m = generate_matrix()
print_matrix(m)
