#7. У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран.
import random
rand_list = []
count_once_list = []

for i in range(15):
    n = random.randint(1, 20)
    rand_list.append(n)
print(rand_list)

i = 0
for i in rand_list:
    if rand_list.count(i) == 1:
        count_once_list.append(i)
print(count_once_list)
