class Phone:

    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"


class MobilePhone(Phone):

    def __init__(self, name, brand, price, color, memory):
        super().__init__(name, brand, price)
        self.color = color
        self.memory = memory

    def __str__(self):
        return f'{self.name}, {self.brand}, {self.price}, {self.color}, {self.memory}'


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
            phone = None
            line = [element.strip() for element in line.split(",")]
            name = line[0]
            brand = line[1]
            price = int(line[2])
            if line[3].isnumeric():
                radius_of_action = int(line[3])
                answering_machine = True if line[4] == 'True' else False
                phone = RadioPhone(name=name,
                                   brand=brand,
                                   price=price,
                                   radius_of_action=radius_of_action,
                                   answering_machine=answering_machine)
            else:
                color = line[3]
                memory = int(line[4])
                phone = MobilePhone(name=name,
                                    brand=brand,
                                    price=price,
                                    color=color,
                                    memory=memory)
            phones.append(phone)
        file.close()
        return phones


def sort_list(list_phone):
    list_phone.sort(key=lambda phone: phone.price)


def write_1(phones, file_name):
    all_sum = 0
    with open(file_name, "w") as file:
        for phone in phones:
            all_sum += phone.price
            file.write(f'{phone}\n')
        file.write(f"sum of price = {all_sum}\n")


def write_2(phones, file_name):
    with open(file_name, "w") as file:
        for phone in phones:
            print(type(phone))
            if type(phone) is RadioPhone and phone.answering_machine:
                file.write(f'{phone}\n')
        file.close()


def add_new_phone(new_phone):
    list_phone.append(new_phone)


list_phone = read_from_file('Panasonic.txt')
list_phone += read_from_file('Apple.txt')

start = input('start: ')
while start == 'l':
    number = int(input(f'Введите номер класс 1 = MobilePhone, 2 = RadioPhone'))
    name = input()
    brand = input()
    price = int(input())
    if number <= 1:
        color = input()
        memory = int(input())
        new_phone = MobilePhone(name, brand, price, color, memory)
        print(new_phone)
    else:
        radius_of_action = int(input('Введиет радиус действия:'))
        answering_machine = bool(input('Введите есть на радио телефоне автоответчик True или False: '))
        new_phone = RadioPhone(name, brand, price, radius_of_action, answering_machine)
        print(new_phone)
    add_new_phone(new_phone)
    start = input('again start: ')

sort_list(list_phone)

write_1(list_phone, 'out1.txt')
write_2(list_phone, 'out2.txt')
