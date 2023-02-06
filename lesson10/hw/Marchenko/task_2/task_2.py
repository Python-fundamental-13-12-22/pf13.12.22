class Table:
    def __init__(self, size, material, price):
        self.size = size
        self.material = material
        self.price = price

    def __repr__(self):
        return f"Table {self.size}, {self.material}, {self.price}"

class Chair:
    def __init__(self, material, price, ch_count = 0, size=None):
        self.material = material
        self.price = price
        self.ch_count = ch_count
        self.size = size

    def __repr__(self):
        return f"Chair {self.material}, {self.price}, {self.ch_count}"

class Set_of_furniture:
    def __init__(self, name, table, chair, ch_count, total_price):
        self.name = name
        self.table = table
        self.chair = chair
        self.ch_count = ch_count
        self.total_price = total_price

    def __repr__(self):
        return f"Set {self.name}, {self.table}, {self.chair}, {self.ch_count}, {self.total_price}"


input_name_of_set = str(input("Name of set:")) #name
input_material = str(input("Material:")) #wood
input_count_chair = str(input("Number of chairs:")) #2
input_table_size = str(input("Table size:")) #60*40


def read_from_file(file_name):
    furniture = []
    with open(file_name) as file:
        for line in file:
            line = [element.strip() for element in line.split(",")]
            if line[1].isnumeric():
                material = line[0]
                price = line[1]
                items = Chair(material=material,
                              price=price)
            else:
                size = str(line[0])
                material = line[1]
                price = line[2]
                items = Table(size=size,
                              material=material,
                              price=price)
            furniture.append(items)
    return furniture


all_furniture = read_from_file("furniture.txt")


def sort_furniture_set(list):
    global other
    other = []
    chairs = []
    tables = []
    count = 0
    price = 0
    price2 = 0
    for item in list:
        if type(item) is Chair and item.material == input_material and count <= int(input_count_chair) - 1:
            count = count + 1
            price = price + int(item.price)
            chairs.append(item)
        if item.material == input_material and item.size == input_table_size:
            tables.append(item)
            price2 = price2 + int(item.price)
        else:
            other.append(item)
    total_price = f"Total price: {price+price2}$"
    chairs_number = f"Number of chairs: {count}"
    set = Set_of_furniture(name=input_name_of_set,
                           table=tables,
                           chair=chairs,
                           ch_count=chairs_number,
                           total_price=total_price)
    return set


sorted_set = str(sort_furniture_set(all_furniture))


def write1(info, filename):
    with open(filename, "a") as file:
            file.write(info)


write1(sorted_set, "file1.txt")


def write2(info, filename):
    info.sort(key=lambda element: element.material)
    with open(filename, "a") as file:
        file.write(f"{info}")


write2(other, "file2.txt")