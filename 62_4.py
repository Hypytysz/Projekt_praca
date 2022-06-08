x=2
lista= []
while x != 0:
    x = (int(input(f"Podaj liczbe calkowita: ")))
    if x != 0 and x not in lista:
        lista.append(x)
        print(lista)
        for indeks, wartosc in enumerate(lista):
            a = (indeks-1)
            if x < lista[a]:
                lista.remove(x)
                lista.insert(a, x)
                print(lista)
                break
    elif x == 0:
        print(lista)
        break
    else:
        print(f"Ta liczba juz jest na liscie!")