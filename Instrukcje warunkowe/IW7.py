#Losowanie dwoch zmiennych z zakresu od - do sprawdzenie wyniku
import random
zm1 = float(random.randint(1, 10))
zm2 = float(random.randint(1, 10))
print (f"Jaki będzie wynik mnożenia {zm1})x{zm2}?")

zm3 = float(input(f"Wpisz swój wynik: "))
if zm3 == zm1*zm2:
    print(f"Brawo udalo Ci sie podac poprawny wynik!")
else:
    print(f"Niestety twoj wynik nie jest prawidlowy.")
