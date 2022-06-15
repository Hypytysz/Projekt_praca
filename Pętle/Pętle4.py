# Lista w liscie edycja danych
kontakty = []

while (True):

    menu = int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-koniec"))

    if (menu == 1):
        imie =input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        telefon = int(input("Podaj telefon: "))
        kontakt = [imie, nazwisko, telefon]
        kontakty.append(kontakt)
        print("Pomyslnie dodano.")
        pass
    elif (menu == 2):
        for x in kontakty:
            print(f"Imie: {x[0]}, Nazwisko: {x[1]}, Telefon: {x[2]}")
        pass
    elif (menu == 3):
        usun = input("Podaj nazwisko: ")
        znaleziono = False
        for x in kontakty:
            if x[1] == usun:
                znaleziono = True
                kontakty.remove(x)
                print(f"Usunieto pomyslnie {usun}")
                break
        if znaleziono == False:
                print(f"Podanego nazwiska nie ma w bazie danych.")
        pass
    elif (menu == 4):
        nazwisko = input("Podaj nazwisko: ")
        znaleziono = False
        for x in kontakty:
            if (x[1] == nazwisko):
                noweImie = input("Podaj nowe imie: ")
                noweNazwisko = input("Podaj nowe nazwisko: ")
                nowyTelefon = input("Podaj nowy telefon: ")

                znaleziono = True
                x[0] = noweImie
                x[1] = noweNazwisko
                x[2] = nowyTelefon
                print("Dane zostaly pomyslnie zmienione")
                break

        if (znaleziono == False):
            print("nie znaleziono")
        pass
    elif (menu == 5):
        break
