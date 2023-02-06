class Table:
    def __init__(self, size="", material="", price=0):
        self._size = size
        self._material = material
        self._price = price
    def __repr__(self):
        return f"({self._size}, {self._material},{self._price})"
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size
    @property
    def material(self):
        return self._material
    @material.setter
    def material(self, material):
        self._material = material
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        self._price = price
class Chair:
    def __init__(self, material="", price=0):
        self._material = material
        self._price = price
    def __repr__(self):
        return f"({self._material},{self._price})"

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, material):
        self._material = material

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
class Nabir_mebliv(Chair,Table):
    def __init__(self, name="", tabl="", chair="", count_chair = 0 ):
        self.name = name
        self.tabl = tabl
        self.chair = chair
        self.count_chair =  count_chair

    def __repr__(self):
        return f"({self.name},{self.tabl}, {self.chair}, {self.count_chair})"
    def create_nabir(self,size , count, material):
        self.size = size
        self.count_chair = count
        self.material = material
        return [size, count, material]

inputFile = open("mebli_input.txt", "r")
s = []
for line in inputFile:
    s_i = line.encode('cp1251').decode('utf8').split(',')
    s.append(s_i)
inputFile.close()
chairs_ar = []
tables_ar = []
for i in range(0,len(s)):
    type_m = s[i][0]
    material = s[i][1]
    if type_m == 'стілець':
        price= s[i][2]
        chairs = Chair(material=material,
                        price=price,
                           )
        chairs_ar.append(chairs)
    elif type_m == 'стіл':
        price= s[i][3]
        size = s[i][2]
        tables = Table(size=size,
                      material=material,
                      price=price)
        tables_ar.append(tables)
nabir = Nabir_mebliv()
k = 0
price_t = 0
flag = False
# вхідні дані
select_nabir = nabir.create_nabir('2х1м',4,'дуб')
for table in tables_ar:
    if type(table) is Table and select_nabir[0] == table.size and select_nabir[2] == table.material:
        nabir.name = 'Набір стіл і стільці '
        nabir.tabl = 'Стіл' + ' ' + table.material + ' ' + table.size + ' ----- '
        price_t += int(str(table.price).split(' ')[0])
        flag = True
price_ch = 0
for chairs in chairs_ar:
    if type(chairs) is Chair and select_nabir[2] == chairs.material:
        k = k + 1
        price_ch += int(str(chairs.price).split(' ')[0])


if k >= select_nabir[1] and flag == True:
    price_n = price_t + price_ch
    nabir.chair = "стільці "+ select_nabir[2] +", шт.: "
    #print(nabir)
    with open('mebli_output.txt', 'w') as file:
        file.write(str(nabir) + ', ціна набору  ' + str(price_n) + 'грн.' )
        print(f' file mebli_output.txt saved')
else:
    with open('mebli_output.txt', 'w') as file:
        file.write('неможливо скласти набір')
    print(f'неможливо скласти набір ')




