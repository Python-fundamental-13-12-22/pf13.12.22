class Phone:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def __repr__(self):
        return f"{self.name}"


class Cellphone(Phone):
    def __init__(self, name, brand, price, color, memory):
        super().__init__(name, brand, price)
        self.color = color
        self.memory = memory

    def __repr__(self):
        return f"{self.name} {self.brand} {self.price} {self.color} {self.memory}"


class Radiophone(Phone):
    def __init__(self, name, brand, price, phone_reach, answering_machine):
        super().__init__(name, brand, price)
        self.phone_reach = phone_reach
        self.answering_machine = answering_machine

    def __repr__(self):
        return f"{self.name} {self.brand} {self.price} {self.phone_reach} {self.answering_machine}"


def read_from_file(file_name):
    phones_list = []
    with open(file_name) as file:
        for line in file:
            phone = None
            line = [element.strip() for element in line.split(",")]
            name = line[0]
            brand = line[1]
            price = int(line[2])
            if line[3].isnumeric():
                phone_reach = int(line[3])
                answering_machine = True if line[4] == "yes" else False
                phone = Radiophone(name=name, brand=brand, price=price, phone_reach=phone_reach,
                                answering_machine=answering_machine)
            else:
                color = line[3]
                memory = int(line[4])
                phone = Cellphone(name=name, brand=brand, price=price, color=color, memory=memory)
            phones_list.append(phone)
        return phones_list


phones1 = read_from_file('brand1_phones.txt')
phones2 = read_from_file('brand2_phones.txt')

all_phones = phones1 + phones2
print(all_phones)
all_phones.sort(key=lambda phone: phone.price)
print(all_phones)

with open('sorted_phoned.txt', 'w') as sf:
    for phone in all_phones:
        sf.writelines(f"{phone}\n")

with open('sorted_phoned.txt', 'a') as sf:
    sum_prices = 0
    for phone in all_phones:
        sum_prices += phone.price
    sf.write(f"Sum of price is {sum_prices}")

with open('radio_answering_phone.txt', 'w') as rad_ans_ph:
    for phone in all_phones:
        if type(phone) is Radiophone and phone.answering_machine is True:
            rad_ans_ph.write(f"{phone}\n")
