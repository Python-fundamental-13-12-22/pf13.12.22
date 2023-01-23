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

    def is_table(self,cell):
        if cell == 'стіл':
            return True

class Chairs:
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
    def is_chair(self,cell):
        if cell == 'стілець':
            return True

class Nabir_mebliv(Chairs,Table):
    def __init__(self, name="", table="", chair="", count_chair = 0 ):
        self.name = name
        self.table = table
        self.chair = chair
        self.count_chair =  count_chair

    def __repr__(self):
        return f"({self.name},{self.table}, {self.chair}, {self.count_chair})"
    def create_nabir(self,size , count):
        self.size = size
        self.count_chair = count
        return [size, count]







inputFile = open("mebli_input.txt", "r")
s = []
for line in inputFile:
    s_i = line.encode('cp1251').decode('utf8').split(',')
    s.append(s_i)
inputFile.close()
print(s)

chair = Chairs()
table = Table()
nabir = Nabir_mebliv()

k = 0
select_nabir = nabir.create_nabir('2х1м',4)
for i in range(0,len(s)):
    if s[i][2] == select_nabir[0] and  table.is_table(s[i][0]):
        nabir.name = 'Набір ' + str(s[i][0]) + ' ' + select_nabir[0] + ' ----- '
        nabir.table = ' ' + str(s[i][0]) +  ' ' + str(s[i][1]) +  ' ' + select_nabir[0] + ' ----- '
    if chair.is_chair(s[i][0]):
        k = k + 1

if k >= select_nabir[1]:
    nabir.chair = "стільці шт.: "
    print(nabir)
    with open('mebli_output.txt', 'w') as file:
        file.write(str(nabir))
        print(f' file mebli_output.txt saved')
else:
    print(f'неможливо скласти набір ')


