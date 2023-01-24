class Table:
    def __init__(self, args):
        self.size = args[1]
        self.material = args[2]
        self.price = args[3]

    def __repr__(self):
        return f" table {self.size}, {self.material},{self.price}"


class Chairs:
    def __init__(self, args):
        self.material = args[1]
        self.price = args[2]

    def __repr__(self):
        return f"chair {self.material}, {self.price}"


class NabirMebliv:
    def __init__(self, name="", table="", chair="", count_chair = 0 ):
        self.name = name
        self.table = table
        self.chair = chair
        self.count_chair = count_chair

    def __repr__(self):
        return f"Набір меблів: {self.name}, {self.table}, {self.chair}, {self.count_chair}"


s = []
with open("input.txt") as file:
    for line in file:
        line = list(line.replace(',', '').split())
        s.append(line)


material = input("input material\n")
size = int(input("input size\n"))
count_ch = int(input("input count chairs\n"))


def create_nabir(s, material, size, count_ch):
    k = 0
    nabir = []
    total_price = 0
    for i in range(0, len(s)):
        if s[i][0] == "chair" and k<=count_ch and s[i][1] == material:
            chair = Chairs(s[i])
            nabir.append(chair)
            k += k
            total_price = int(chair.price) + total_price
        if s[i][0] == "table" and s[i][1] == material and size == int(s[i][2]):
            table = Table(s[i])
            nabir.append(table)
            total_price = int(table.price) + total_price
    return nabir, total_price


nabir, total_price = create_nabir(s, material, size, count_ch)
for i in range(0, len(nabir)):
    with open("outfile1.txt", "a") as file:
        file.write(f'{nabir[i]}\n')
with open("outfile1.txt", "a") as file:
    file.write(f'{total_price}\n')


def create_nabir2(s, material, size, count_ch):
    k = 0
    nabir = []
    total_price = 0
    for i in range(0, len(s)):
        if s[i][0] == "chair" and k<=count_ch and s[i][1] != material:
            chair = Chairs(s[i])
            nabir.append(chair)
            k += k
            total_price = int(chair.price) + total_price
        if s[i][0] == "table" and material != s[i][1] and size == int(s[i][2]):
            table = Table(s[i])
            nabir.append(table)
            total_price = int(table.price) + total_price
    return nabir, total_price


nabir, total_price = create_nabir2(s, material, size, count_ch)
for i in range(0, len(nabir)):
    with open("outfile2.txt", "a") as file:
        file.write(f'{nabir[i]}\n')
with open("outfile2.txt", "a") as file:
    file.write(f'{total_price}\n')