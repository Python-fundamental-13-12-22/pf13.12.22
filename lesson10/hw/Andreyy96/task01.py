import json


class Phone:
    list_phone = []

    def __init__(self, name='', brand='', price=0):
        self.name = name
        self.brand = brand
        self.price = price

    def add_dif_phone(self):
        with open('Panasonic.txt', 'r') as file:
            for line in file:
                res = json.loads(line)
                self.list_phone.append(res)
                print(line, end="")
            file.close()

        with open("Apple.txt", 'r') as file:
            for line in file:
                res = json.loads(line)
                self.list_phone.append(res)
                print(line, end="")
            file.close()

    def sort_lst_phone(self):
        self.list_phone.sort(key=lambda i: i[2])

    def print_out1_txt_file(self):
        value = 0
        for i in range(len(self.list_phone)):
            if type(self.list_phone[i][2]) == int:
                value += self.list_phone[i][2]

        f = open('out1.txt', 'wt')
        for item in self.list_phone:
            s = (', '.join(map(str, item))) + '\n'
            s.split()
            f.write(s)
        f.write(f'Sum:{value}')
        f.close()


class MobilePhone(Phone):

    def __init__(self, name='', brand='', price=0, color='', memory=''):
        super().__init__(name, brand, price)
        self.color = color
        self.memory = memory

    def __str__(self):
        return f'MobilePhone: {self.name} {self.brand}, {self.price}, {self.color},  {self.memory}'


class RadioTelephone(Phone):

    def __init__(self, name='', brand='', price=0, radius=0, answering='No'):
        super().__init__(name, brand, price)
        self.radius_of_action = radius
        self.answering = answering

    def __str__(self):
        return f'MobilePhone: {self.name} {self.brand}, {self.price}, {self.radius_of_action},  {self.answering}'

    def print_out2_txt_file(self):
        f = open('out2.txt', 'wt')
        for i in range(len(self.list_phone)):
            for j in range(len(self.list_phone[i])):
                if self.list_phone[i][j] == 'True':
                    s = (', '.join(map(str, self.list_phone[i]))) + '\n'
                    f.write(s)
        f.close()


def add_dif_phone(list_phone):
    with open('Panasonic.txt', 'r') as file:
        for line in file:
            line = line.strip()
            list_row = line.split(', ')
            list_phone.append(list_row)
            print(line, end="\n")
        file.close()

    with open("Apple.txt", 'r') as file:
        for line in file:
            line = line.strip()
            list_row = line.split(', ')
            list_phone.append(list_row)
            print(line, end="\n")
        file.close()


def sort_lst_phone(list_phone):
    list_phone.sort(key=lambda i: i[2])


def get_sum_price(list_phone):
    sum_price = 0
    for i in range(len(list_phone)):
        p.price = int(list_phone[i][2])
        sum_price += p.price

    return sum_price


def print_out1_txt_file(list_phone, sum_price):

    list_tel = []
    for i in range(len(list_phone)):
        p.name = list_phone[i][0]
        p.brand = list_phone[i][1]
        p.price = int(list_phone[i][2])
        row = [p.name, p.brand, p.price]
        list_tel.append(row)


    f = open('out1.txt', 'wt')
    for item in list_tel:
        s = (', '.join(map(str, item))) + '\n'
        s.split()
        f.write(s)
    f.write(f'Sum:{sum_price}')
    f.close()


def print_out2_txt_file(list_phone):
    f = open('out2.txt', 'wt')
    for i in range(len(list_phone)):
        for j in range(len(list_phone[i])):
            if list_phone[i][j] == 'Yes':
                s = (', '.join(map(str, list_phone[i]))) + '\n'
                f.write(s)
    f.close()


p = Phone()
r = RadioTelephone()
m = MobilePhone()
list_phone = []

add_dif_phone(list_phone)
sort_lst_phone(list_phone)
sum_price = get_sum_price(list_phone)
print_out1_txt_file(list_phone, sum_price)
print_out2_txt_file(list_phone)
