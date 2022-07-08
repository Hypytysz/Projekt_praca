# Liczby doskonałe


def dzielniki(x):
    suma = 0
    for i in range(1, int(x / 2) + 1):
        if x % i == 0:
            dziel.append(i)
    for y in dziel:
        suma += y
    if suma == x:
        print("To liczba doskonała.")
    else:
        print("To nie jest liczba doskonała.")


dziel = []
a = int(input("Podaj liczbę: "))
dzielniki(a)
