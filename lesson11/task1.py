class Phone:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price
    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"

from json import JSONEncoder
class PhoneEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__




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



s = []
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
                answering_machine = True if line[4] == "Yes"  else False
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
PHONES = read_from_file("in.txt")
PHONES.sort(key=lambda phone: phone.price)



print(PHONES)


def write_1(phones, file_name):
    all_sum = 0
    with open(file_name, "a") as file:
        for phone in phones:
            all_sum += phone.price
            file.write(f'{phone}\n')
        file.write(f"sum of price = {all_sum}")
write_1(PHONES, "brand1_phones.json")

write_1([phone for phone in PHONES if type(phone) is RadioPhone and phone.answering_machine],
        "brand2_phones.json")
import json
j = json.dumps(PHONES, indent=4, cls=PhoneEncoder)
# j = json.dumps(PHONES[0], indent=4, cls=PhoneEncoder)
with open("phones.json", "w") as file:
    file.write(j)

with open("phones.json") as file:
    p = json.load(file)
m = MobilePhone(**p[0])
print(m)


# try:
#     file = open("file1.txt")
# except:
#     # ToDo
# finally:
#     file.close()
#
# with open("file1.txt") as file1, open("file2.txt") as file2:
#     pass
# a = 1
#
# class MyContext:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.open_file = None
#     def __enter__(self):
#         print(f"__enter__ {self.file_name}")
#         self.open_file = open(self.file_name)
#         return self.open_file
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.open_file:
#             print(f"__exit__ {self.file_name} {self.open_file}")
#             self.open_file.close()
#
# with MyContext("in.txt") as t:
#     print(t)
#
# def my_range(start, stop, step=1):
#     element = start
#     while stop > element:
#         print(f"yield {element}")
#         yield element
#         element += step
#         print(f"next - {element}")
#
# # g = my_range(0,2)
# # print(g)
# # print(next(g))
# # print("-"*10)
# # print(next(g))
# # print("-"*10)
# # print(next(g))
#
# g = my_range(0,2)
# for i in g:
#     print(f"i={i}")