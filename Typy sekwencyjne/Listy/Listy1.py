#Program sortujący duplikaty w liście
import random
lista = []
duplikaty = []
x = 10

while x > 0:
    x -= 1
    lista.append(int(random.randint(1, 10)))

for i in lista:
    if lista.count(i) > 1:
        duplikaty.append(i)


print(lista)
print(duplikaty)
