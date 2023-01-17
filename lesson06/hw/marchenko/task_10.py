# TASK 10

def max_values(matrix):
    max_val = float("-inf")
    max_index = (0,0)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_index = (i, j)
    return (max_index[0], max_index[1], max_val)

