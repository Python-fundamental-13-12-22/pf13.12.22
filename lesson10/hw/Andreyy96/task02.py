class Table:

    def __init__(self, name='', size='', material='', price=0):
        self.name = name
        self.size = size
        self.material = material
        self.price = price

    def __repr__(self):
        return f'{self.name}, {self.size}, {self.material}, {self.price}'


class Chair:

    def __init__(self, name='', material='', price=0):
        self.name = name
        self.material = material
        self.price = price

    def __repr__(self):
        return f'{self.name}, {self.material}, {self.price}'


class FurnitureSet:

    def __init__(self, name='', table=None, chair=None, count_chairs=0, sum_price=0):
        self.name = name
        self.table = table
        self.chair = chair
        self.count_chairs = count_chairs
        self.sum_price = sum_price

    def __str__(self):
        return f'SetFurniture: {self.name} {self.table}, {self.chair}, {self.count_chairs}, {self.sum_price}'
    def get_price(self):
        pass

def read_from_file(file_name):
    list_furniture = []
    with open(file_name) as file:
        for line in file:
            line = [element.strip() for element in line.split(",")]
            furniture = None
            name = str(line[0])
            if name == "Table":
                size = str(line[1])
                material = str(line[2])
                price = int(line[3])
                furniture = Table(name=name,
                                  material=material,
                                  price=price,
                                  size=size, )
            elif name == "Chair":
                material = str(line[1])
                price = int(line[2])
                furniture = Chair(name=name,
                                  material=material,
                                  price=price)
            list_furniture.append(furniture)
        return list_furniture


def creat_set_furniture(list_furniture, size, count_ch):
    k = 1
    sum_price = 0
    furnit_table = []
    chairs = []
    set_furniture = None
    for elements in list_furniture:
        if type(elements) is Table and str(elements.size) == size:
            if elements.material == material and str(elements.size) == size:
                sum_price += int(elements.price)
                table = Table(name=elements.name,
                              size=elements.size,
                              material=elements.material,
                              price=elements.price)
                furnit_table.append(table)
        if type(elements) is Chair:
            if elements.material == material and k <= int(count_ch):
                k += 1
                print(count_ch)
                sum_price += int(elements.price)
                chair = Chair(name=elements.name,
                              material=elements.material,
                              price=elements.price)
                chairs.append(chair)
    set_furniture = FurnitureSet(name='Result =',
                                 table=furnit_table,
                                 count_chairs=count_ch,
                                 chair=chairs,
                                 sum_price=sum_price)

    return set_furniture


def creat_second_set_furniture(list_furniture, material, first_set_furniture, size):
    k = 1
    sum_price = 0
    furniture_table = []
    chairs = []
    set_furniture2 = None
    for line in list_furniture:
        if type(line) is Table and line.material != material and size == str(line.size):
            print(line.material, material)
            sum_price = int(line.price)
            table = Table(name=line.name,
                          size=line.size,
                          material=line.material,
                          price=line.price)
            furniture_table.append(table)
            print(furniture_table)
        elif type(line) is Chair:
            if line.material != material and k <= int(count_ch):
                k += 1
                print(count_ch)
                sum_price += int(line.price)
                chair = Chair(name=line.name,
                              material=line.material,
                              price=line.price)
                chairs.append(chair)
    set_furniture2 = FurnitureSet(name='Result =',
                                  table=furniture_table,
                                  count_chairs=count_ch,
                                  chair=chairs,
                                  sum_price=sum_price)

    return set_furniture2

#
# list_furniture = read_from_file('TablesAndChairs.txt')
#
# material = input("Введите материал wood или steel: ")
# size = input("Введите размер стола: 120*80 или 150*90: ")
# count_ch = int(input("input count chairs 1 - 6"))
#
# first_set_furniture = creat_set_furniture(list_furniture, size, count_ch)
# with open("first_set.txt", "w") as file:
#     file.write(f'{first_set_furniture}\n')
#
# second_set_furniture = creat_second_set_furniture(list_furniture, material, first_set_furniture, size)
# with open("full_set.txt", "w") as file:
#     file.write(f'{second_set_furniture}\n')


class FurnitureSet:

    def __init__(self, name='', table=None, chair=None):
        self.name = name
        self.table = table
        self.chair = chair if chair else []

    def __str__(self):
        return f'SetFurniture: {self.name} <{self.table}>, <{len(self.chair)} {self.chair}> {self.get_price()}'
    def __repr__(self):
        return f'<{self.name}, {self.table.material}, {len(self.chair)}>'
    def get_price(self):
        return self.table.price + sum(chair.price for chair in self.chair)

list_furniture = read_from_file('TablesAndChairs.txt')


material = "wood" #input("Введите материал wood или steel: ")
size = "120*80" #input("Введите размер стола: 120*80 или 150*90: ")
count_ch = 5 #int(input("input count chairs 1 - 6: "))

furnitureSet = FurnitureSet(name="task1")
for index, element in enumerate(list_furniture):
    if type(element) is Table:
        if element.size == size and element.material == material:
            furnitureSet.table = element
            del list_furniture[index]
            break
for index, element in enumerate(list_furniture):
    if type(element) is Chair:
        if element.material == material and len(furnitureSet.chair) < count_ch:
            furnitureSet.chair.append(element)
            del list_furniture[index]
print(furnitureSet)
print(list_furniture)
print()
print(list_furniture)
tables = [element for element in list_furniture if type(element) is Table]
print(tables)
chairs = [element for element in list_furniture if type(element) is Chair]
print(chairs)
furniture_sets = []
for i, table in enumerate(tables):
    fs = FurnitureSet(name=f"fs_{i+1}", table=table)
    for chair in chairs:
        if chair.material == table.material and len(fs.chair) < 4:
            fs.chair.append(chair)
    for chair in fs.chair:
        chairs.remove(chair)

    furniture_sets.append(fs)

print(tables)
print(chairs)
print(furniture_sets)