# Najwiueksza i najmniejsza wartosc z 5 podanych
l1 = int(input("Podaj liczbe: "))
l2 = int(input("Podaj liczbe: "))
l3 = int(input("Podaj liczbe: "))
l4 = int(input("Podaj liczbe: "))
l5 = int(input("Podaj liczbe: "))

najmniejsza = l1
najwieksza = l1

if(l2 > najwieksza):
    najwieksza = l2
if(l2 < najmniejsza):
    najmniejsza = l2

if(l3 > najwieksza):
    najwieksza = l3
if(l3 < najmniejsza):
    najmniejsza = l3

if(l4 > najwieksza):
    najwieksza = l4
if(l4 < najmniejsza):
    najmniejsza = l4

if(l5 > najwieksza):
    najwieksza = l5
if(l5 < najmniejsza):
    najmniejsza = l5

print(f"Max: {najwieksza} Min: {najmniejsza}")
