class Phone:
    def __init__(self, list1):
        self.name = list1[0]
        self. brand = list1[1]
        self.price = list1[2]


class MobilePhone(Phone):
    def __init__(self, list1):
        super().__init__(list1)
        self.color = list1[3]
        self.memory_space = list1[4]


class RadioPhone(Phone):
    def __init__(self, list1):
        super().__init__(list1)
        self.radius_of_action = list1[3]
        self.answering_machine = list1[4]


s = []
with open("file1.txt") as file:
    for line in file:
        line = list(line.replace(',', '').split())
        s.append(line)

with open("file2.txt") as file:
    for line in file:
        line = list(line.replace(',', '').split())
        s.append(line)


def write_phone(i):
    try:
        int(s[i][4])
    except ValueError:
        radiophone = RadioPhone(s[i])
        if s[i][4] == "Yes" or s[i][4] == "yes":
            with open("out2.txt", "a") as file:
                file.write(f"radiophone{i}: {radiophone.name=}, {radiophone.brand=}, {radiophone.price=}, {radiophone.radius_of_action=}, {radiophone.answering_machine=} \n")


def sort(s):
    for i in range(0, len(s)):
        minimum = i
        for j in range(i+1, len(s)):
            if int(s[j][2]) < int(s[minimum][2]):
                minimum = j
                s[minimum], s[i] = s[i], s[minimum]
    return s

def write_1(s):
    sum = 0
    for i in range(0, len(s)):
        sum = sum + int(s[i][2])
        with open("out1.txt", "a") as file:
            file.write(f'{s[i]}\n')
    with open("out1.txt", "a") as file:
        file.write(f"sum of price = {sum}")


sort(s)
for i in range(0, len(s)):
    write_phone(i)

write_1(s)