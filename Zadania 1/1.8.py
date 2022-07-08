# Suma wartosci listy, krotki, zbioru lub slownika

def suma_wartosci(x):
    suma = 0
    if type(x) is list:
        for i in x:
            suma += i
    if type(x) is tuple:
        for i in x:
            suma += i
    if type(x) is set:
        for i in x:
            suma += i
    if type(x) is dict:
        for i in x:
            suma += x[i]
    return suma

def wyswietl(x):
    if type(x) is list:
        y = suma_wartosci(lista)
        print(y)
    if type(x) is tuple:
        y = suma_wartosci(krotka)
        print(y)
    if type(x) is set:
        y = suma_wartosci(zbior)
        print(y)
    if type(x) is dict:
        y = suma_wartosci(slownik)
        print(y)

lista = [1, 2, 3, 4, 5]
krotka = (1, 2, 5, 10)
zbior = {10, 20, 30, 4}
slownik = {"jeden": 1, "trzy": 3, "szesc": 6, "dziewiec": 9}
suma_wartosci(lista)
wyswietl(lista)
suma_wartosci(krotka)
wyswietl(krotka)
suma_wartosci(zbior)
wyswietl(zbior)
suma_wartosci(slownik)
wyswietl(slownik)
