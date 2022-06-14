#Ktora liczba jest wieksza uzytkownika czy komputera
import random
los1 = random.randint(1,10)
los2 = random.randint(1,10)
iloczyn1 = los1*los2
wynik_uzytkownika = input(f"Ile wynosi {los1}*{los2}?")
print(f"Twoja odpowiedz to = {wynik_uzytkownika}")
print(f"Prawidlowy wynik to = {iloczyn1}")
