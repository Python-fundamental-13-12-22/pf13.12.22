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

m = generate_matrix(10, 10, 1, 20)
print('m =')
print_matrix(m)
def swap(m, col1, col2):
    rows = len(m)
    for i in range(rows):
        m[i][col1], m[i][col2] = m[i][col2], m[i][col1]
    return m
def selection_sort(m):
    nums = m[0]
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        m = swap(m, i, lowest_value_index)
    return m
m = selection_sort(m)
print("sorted by 1st row matrix:")
print_matrix(m)
