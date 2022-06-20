# Losowo wybrana liczba przez komputer wieksza/mniejsza
import random

zm1 = int(random.randint(1, 100))
x = 6
while x!=0:
    x-=1
    if x == 0:
        print(f"Wylosowana liczba byla liczba: {zm1}")
        odp = input((f"Przegrales!  Chcesz zagrac jeszcze raz? T/N"))
        if odp == "T":
            x=6
            zm1=int(random.randint(1, 100))
        elif odp == "N":
            break
        else:
            print("cos poszlo nie tak")
    if x !=0:
        zm2 = int(input(f"Podaj liczbe: "))
        if zm2 == zm1:
            odp1 = input((f"Brawo udalo Ci sie odgadnac prawidlowa liczbe! Chcesz zagrac jeszcze raz? T/N"))
            if odp1 == "N":
                break
            if odp1 == "T":
                x=6
                zm1=int(random.randint(1, 100))
            else:
                print("Cos poszlo nie tak")
        elif zm2 > zm1:
            print(f"Podaj mniejsza liczbe")
        elif zm2 < zm1:
            print(f"Podaj wieksza liczbe")
