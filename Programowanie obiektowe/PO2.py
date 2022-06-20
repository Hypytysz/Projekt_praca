# Pracownik - dodaj, usun, pokaz, zmien
class Pracownik:
    def __init__(self, imie, nazwisko, email, telefon):

        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.telefon = telefon


listaPracownikow = []

while (True):

    menu = int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-koniec"))

    if (menu == 1):
        imie = input(f"Dodaj imie: ")
        nazwisko = input(f"Dodaj nazwisko: ")
        email = input(f"Dodaj email: ")
        telefon = input(f"Dodaj telefon: ")

        pracownik = Pracownik(imie, nazwisko, email, telefon)
        listaPracownikow.append(pracownik)
        print("Pracownik pomyslnie dodany")
    elif (menu == 2):
        for x in listaPracownikow:
            print(f"Imie: {x.imie}\nNaziwsko: {x.nazwisko}\nEmail: {x.email}\nTelefon: {x.telefon}")
    elif (menu == 3):
        nazwisko = input("Podaj nazwisko, ktore chcesz skasowac: ")
        znaleziono = "NIE"
        for x in listaPracownikow:
            if x.nazwisko == nazwisko:
                znaleziono = "TAK"
                listaPracownikow.remove(x)
                break
        if znaleziono == "NIE":
            print("Nie ma takiej osoby")
    elif (menu == 4):
        nazwisko = input("Podaj nazwisko, ktore chcesz zmienic: ")
        znaleziono = "NIE"
        for x in listaPracownikow:
            if x.nazwisko == nazwisko:
                znaleziono = "TAK"
                noweImie = input(f"Podaj nowe imie: ")
                noweNazwisko = input(f"Podaj nowe nazwisko: ")
                nowyEmail = input(f"Podaj nowy email: ")
                nowyTelefon = input(f"Podaj nowyTelefon")
                x.nazwisko = noweNazwisko
                x.imie = noweImie
                x.email = nowyEmail
                x.telefon = nowyTelefon
                print(f"Zmieniono imie na: {x.imie}\nazwisko na: {x.nazwisko}\nemail na: {x.email}\ntelefon na: {x.telefon}")
                break
        if znaleziono == "NIE":
            print("Nie ma takiej osoby")
        pass
    elif (menu == 5):
        break
