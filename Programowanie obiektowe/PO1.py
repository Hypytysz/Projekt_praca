# Dodawanie i modyfikowanie studentow z ocenami oraz liczeniem sredniej
class Student:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []

    def dodajOcene(self, ocena):
        self.oceny.append(ocena)

    def wypiszOceny(self):
        for i in self.oceny:
            print(f"Twoje oceny to: {i}")


    def policzSrednia(self, srednia):
        suma = 0
        for x in self.oceny:
            suma += x
        srednia = suma/len(self.oceny)
        print(f"Srednia: {srednia}")

listaStudentow = []

while(True):

    menu = int(input("1-dodaj studenta, 2-pokaz studentow, 3-usun studenta, 4-dodaj ocenę studentowi, "
                     "5-wypisz oceny studenta, 6-pokaz srednią studenta, 7-koniec"))


    if menu == 1:
        imie = input(f"Podaj imie studenta: ")
        nazwisko = input(f"Podaj nazwisko studenta: ")
        student = Student(imie, nazwisko)
        listaStudentow.append(student)

    elif menu == 2:
        for x in listaStudentow:
            print(f"Imie: {x.imie}\nNaziwsko: {x.nazwisko}\n")
    elif menu == 3:
        nazwisko = input("Podaj nazwisko, ktore chcesz skasowac: ")
        znaleziono = "NIE"
        for x in listaStudentow:
            if x.nazwisko == nazwisko:
                znaleziono = "TAK"
                listaStudentow.remove(x)
                break
        if znaleziono == "NIE":
            print("Nie ma takiej osoby")
    elif menu == 4:
        nazwisko = input(f"Podaj nazwisko osoby, ktorej chcesz dodac ocene: ")
        znaleziono = "NIE"
        ilosc = int(input("Ile ocen chcesz dodac?"))
        for i in range(ilosc):
            for i in listaStudentow:
                if i.nazwisko == nazwisko:
                    znaleziono = "TAK"
                    oceny = int(input("Podaj ocene:"))
                    i.dodajOcene(oceny)
                    break
        if znaleziono == "NIE":
            print(f"Nie odnaleziono {nazwisko} w bazie danych")

    elif menu == 5:
        nazwisko = input(f"Podaj nazwisko osoby, ktorej oceny chcesz wyswietlic: ")
        znaleziono = "NIE"
        for i in listaStudentow:
            if i.nazwisko == nazwisko:
                znaleziono = "TAK"
                i.wypiszOceny()
                break
        if znaleziono == "NIE":
            print(f"Nie odnaleziono {nazwisko} w bazie danych")
    elif menu == 6:
        nazwisko = input(f"Podaj nazwisko osoby, ktorej srednia chcesz wyswietlic: ")
        znaleziono = "NIE"
        for i in listaStudentow:
            if i.nazwisko == nazwisko:
                znaleziono = "TAK"
                srednia = i.policzSrednia(nazwisko)
                break
        if znaleziono == "NIE":
            print(f"Nie odnaleziono {nazwisko} w bazie danych")
    elif menu == 7:
        break
