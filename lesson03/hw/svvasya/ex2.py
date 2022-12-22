a = 1456
a1= a%10
#print(a1)
a2= a%100//10
#print(a2)
a3= a%1000//100
#print(a3)
a4= a//1000
#print(a4)
print('Добуток', a1*a2*a3*a4)
print('Реверс', int(str(a1) + str(a2) + str(a3) + str(a4)))
print('Сортування', sorted([a1,a2,a3,a4]))
