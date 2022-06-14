#Program sortujący duplikaty z dwóch list 2
import random
lista = []
lista2 = []
obie = []
x = 10
y = 10
while x > 0:
    x -= 1
    lista.append(int(random.randint(1, 50)))
while y > 0:
    y -= 1
    lista2.append(int(random.randint(1, 50)))

for i in lista:
    for j in lista2:
        if i==j:
            obie.append(i)
            break



print(lista)
print(lista2)
print(obie)
