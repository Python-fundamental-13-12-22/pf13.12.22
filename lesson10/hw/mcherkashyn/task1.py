def Open_file(filename):
    with open(filename) as file:
        matrix = []
        for line in file:
            line = line.strip()
            list = line.split(', ')
            matrix.append(list)
        return matrix

file1 = Open_file("in1.txt")
file2 = Open_file("in2.txt")
matrix = file1 + file2
#print(matrix)

def Sort_out(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum = sum + int(matrix[i][3])
    sorted_m = list(sorted(matrix, key=lambda price: price[3] ))#, Total sum: {sum}
    sorted_m.append(str(f"Total price sum:{sum}$"))
    result = '\n'.join(map(str, sorted_m))
    return result

#print(Sort_out(matrix))

def Radio_out(matrix):
    radio_list = []
    for t in range(len(matrix)):
        if matrix[t][0] == "Radio_phone" and matrix[t][5] == "Yes":
            radio_list.append(matrix[t])
            result = '\n'.join(map(str, radio_list))
            return result

#print(Radio_out(matrix))

def Write_to_file(info, filename):
    with open(filename, 'a') as f:
            f.write(info)

Write_to_file(Sort_out(matrix), "out1.txt")
Write_to_file(Radio_out(matrix), "out2.txt")
#print(Sort_out(matrix))
#print(Radio_out(matrix))
