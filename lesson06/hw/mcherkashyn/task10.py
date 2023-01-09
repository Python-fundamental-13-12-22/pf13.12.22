def max_values(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            value = max(matrix[i])
            if matrix[i][j] == value:
                c = (i, j, value)
                print(c)

max_values([[0, 2, 3], [4, 13, 6], [7, 8, 9]])
