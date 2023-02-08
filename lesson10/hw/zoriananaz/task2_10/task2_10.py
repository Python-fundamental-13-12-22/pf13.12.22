class Table:
    def __init__(self, name, size, material, price):
        self.name = name
        self.size = size
        self.material = material
        self.price = int(price)

    def __repr__(self):
        return f"{self.name} {self.size} {self.material} {self.price}"


class Chair:
    def __init__(self, name, material, price):
        self.name = name
        self.material = material
        self.price = int(price)

    def __repr__(self):
        return f"{self.name} {self.material} {self.price}"


class SetOfFurniture:
    def __init__(self, name, table, chair, sum_price):
        self.name = name
        self.table = table
        self.chair = chair
        self.sum_price = sum_price

    def __repr__(self):
        return f"{self.name} {self.table} {self.chair} {self.sum_price}"


def read_from_file(file_name):
    with open(file_name) as file:
        list = []
        for line in file:
            line = [element.strip() for element in line.split(",")]
            name = str(line[0])
            if name == "chair":
                material = str(line[1])
                price = int(line[2])
                item = Chair(name="Chair", material=material, price=price)
            elif name == "table":
                size = int(line[1])
                material = str(line[2])
                price = int(line[3])
                item = Table(name="Table", size=size, material=material, price=price)
            list.append(item)
        return list


def write_user_choice(list):
    chairs_choose = []
    set_furniture = []
    table_choose = []
    final_sum = 0
    other = []
    for item in list:
        if item.material == user_material:
            if type(item) is Table:
                other.append(item)
                if item.size == user_table_size:
                    table_choose.append(item)
                    final_sum += item.price
                    if len(other) > len(table_choose):
                        other.remove(item)
            elif type(item) is Chair and len(chairs_choose) < user_num_chair:
                chairs_choose.append(item)
                final_sum += item.price
    set_furniture = table_choose + chairs_choose
    set_furniture = SetOfFurniture(name=f"Furniture is", table=str(table_choose), chair=str(chairs_choose),
                                   sum_price=f"{final_sum} $" )
    return set_furniture


def write_user_choice2(list):
    chairs_choose = []
    set_furniture1 = []
    table_choose = []
    final_sum = 0
    other_mat_chairs = []
    remained_chairs = []
    remained_tables = []
    other_mat_tables = []
    for item in list:
        if item.material == user_material:
            if type(item) is Table:
                remained_tables.append(item)
                if item.size == user_table_size:
                    table_choose.append(item)
                    final_sum += item.price
                    if len(remained_tables) > len(table_choose):
                        table_choose.remove(item)
                    remained_tables.remove(item)
            elif type(item) is Chair and len(chairs_choose) < user_num_chair:
                chairs_choose.append(item)
                final_sum += item.price
            else:
                remained_chairs.append(item)
        elif item.material != user_material:
            if type(item) is Chair:
                other_mat_chairs.append(item)
            else:
                other_mat_tables.append(item)
    set_furniture1 = remained_chairs + remained_tables + other_mat_chairs + other_mat_tables
    set_furniture1 = SetOfFurniture(name="Other",  table=set_furniture1, chair="", sum_price="")
    return f"Other {remained_chairs + remained_tables} or {other_mat_chairs + other_mat_tables} "


user_material = str(input(f"Enter material(wood or glass): "))
user_table_size = int(input(f"Enter size(110 or 120): "))
user_num_chair = int(input(f"Enter number of chairs(1-3): "))


def report_to_file(file_name, a):
    with open(file_name, 'w') as fn:
        fn.write(str(a))


list_all = read_from_file('values.txt')
rep = write_user_choice(list_all)
rep2 = write_user_choice2(list_all)
report_to_file('user_choice.txt', rep)
report_to_file('another_furniture.txt', rep2)
