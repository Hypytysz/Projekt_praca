# Funkcja zwracająca środkowy znak lub pusty napis jeżeli nie ma środka
def srodkowa_litera(napis, liczba_liter):
    if liczba_liter % 2 == 0:
        print("")
    elif liczba_liter % 2 != 0:
        liczba_liter //= 2
        print(napis[liczba_liter])


napis = input("Podaj napis: ")
liczba_liter = len(napis)
srodkowa_litera(napis, liczba_liter)
