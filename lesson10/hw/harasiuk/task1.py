class Phone:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"


class MobilePhone(Phone):
    def __init__(self, name, brand, price, color, memory_space):
        super().__init__(name, brand, price)
        self.color = color
        self.memory_space = memory_space

    def __str__(self):
        return f"{self.name}, {self.brand}, {self.price}, {self.color}, {self.memory_space}"


class RadioPhone(Phone):
    def __init__(self, name, brand, price, radius_of_action, answering_machine):
        super().__init__(name, brand, price)
        self.radius_of_action = radius_of_action
        self.answering_machine = answering_machine

    def __str__(self):
        return f"{self.name}, {self.brand}, {self.price}, {self.radius_of_action}, {self.answering_machine}"


def read_from_file(file_name):
    phones = []
    with open(file_name) as file:
        for line in file:
            line = [element.strip() for element in line.split(",")]
            phone = None
            name = line[0]
            brand = line[1]
            price = int(line[2])
            if line[3].isnumeric():
                radius_of_action = int(line[3])
                answering_machine = True if line[4] == "Yes" else False
                phone = RadioPhone(name=name,
                                   brand=brand,
                                   price=price,
                                   radius_of_action=radius_of_action,
                                   answering_machine=answering_machine)
            else:
                color = line[3]
                memory_space = int(line[4])
                phone = MobilePhone(name=name,
                                    brand=brand,
                                    price=price,
                                    color=color,
                                    memory_space=memory_space)
            phones.append(phone)
    return phones


PHONES = read_from_file("file2.txt")
PHONES += read_from_file("file1.txt")
PHONES.sort(key=lambda phone: phone.price)


def write_1(phones, file_name):
    all_sum = 0
    with open(file_name, "w") as file:
        for phone in phones:
            all_sum += phone.price
            file.write(f'{phone}\n')
        file.write(f"sum of price = {all_sum}\n")


write_1(PHONES, "out1.txt")
write_1([phone for phone in PHONES if type(phone) is RadioPhone and phone.answering_machine], "out2.txt")