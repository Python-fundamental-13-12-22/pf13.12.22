class Table:
    def __init__(self, classification, size, material, price):
        self.classification = classification
        self.size = size
        self.material = material
        self.price = price

    def __repr__(self):
        return f" table {self.size}, {self.material},{self.price}"


class Chairs:
    def __init__(self, classification, material, price):
        self.classification = classification
        self.material = material
        self.price = price

    def __repr__(self):
        return f"chair {self.material}, {self.price}"


class Collections:
    def __init__(self, name=None, table=None, chair=None, count_chair=0, total_price =0):
        self.name = name
        self.table = table
        self.chair = chair
        self.count_chair = count_chair
        self.total_price = total_price

    def __repr__(self):
        return f"Collection: {self.name}, {self.table}, {self.chair}, {self.count_chair} {self.total_price=}"


def read_from_file(file_name):
    collections_chairs = []
    collections_tables = []
    with open(file_name) as file:
        for line in file:
            line = [element.strip() for element in line.split(",")]
            element = None
            classification = line[0]
            if classification == "chair":
                material = line[1]
                price = int(line[2])
                element = Chairs(material=material,
                                 price=price,
                                 classification="chair")
                collections_chairs.append(element)
            elif classification == "table":
                material = line[1]
                size = line[2]
                price = line[3]
                element = Table(material=material,
                                price=price,
                                size=size,
                                classification="table")
                collections_tables.append(element)
    return collections_tables, collections_chairs


tables_collection, chairs_collection = read_from_file("input.txt")


material = input("input material\n")
size = int(input("input size\n"))
count_ch = int(input("input count chairs\n"))


def creat_collections(chairs, tables, material, size, count_ch):
    k = 0
    total_price = 0
    collection = None
    for elements in tables:
        if elements.material == material and elements.size == size:
            total_price += int(elements.price)
    collection_chairs = []
    for elements in chairs:
        chair = None
        if elements.material == material and k <= int(count_ch):
            k = k + 1
            total_price += int(elements.price)
            chair = Chairs(classification=elements.classification,
                           material=elements.material,
                           price=elements.price)
            collection_chairs.append(chair)
    collection = Collections(name=material,
                             table=size,
                             count_chair=count_ch,
                             chair=collection_chairs,
                             total_price=total_price)

    return collection


collection = creat_collections(chairs_collection, tables_collection, material, size, count_ch)
with open("outfile1.txt", "w") as file:
    file.write(f'{collection}\n')


def creat_collections2(chairs, tables, collection):
    k = 0
    total_price = 0
    for table in tables:
        if table.material != collection.name:
            total_price += int(table.price)
            material = table.material
    collection_chairs = []
    for elements in chairs:
        chair = None
        if elements.material == material and k <= int(collection.count_chair):
            k = k + 1
            total_price += int(elements.price)
            chair = Chairs(classification=elements.classification,
                           material=elements.material,
                           price=elements.price)
            collection_chairs.append(chair)
    collection1 = Collections(name=material,
                             table=collection.table,
                             count_chair=k,
                             chair=collection_chairs,
                             total_price=total_price)
    return collection1


c2 = (creat_collections2(chairs_collection, tables_collection, collection))
with open("outfile2.txt", "w") as file:
    file.write(f'{c2}\n')