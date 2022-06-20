# Przychodnia
class Przychodnia:

    def __init__(self, nazwa, miasto):
        self.nazwa = nazwa
        self.miasto = miasto
        self.listapacjentow = []
    def dodajPacjenta(self):
        self.listapacjentow.append(pacjent)
    def wypiszPacjentow(self):
        for x in self.listapacjentow:
            print(f"Imie: {x.imie}\nNazwisko: {x.nazwisko}\n")

class Pacjent:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.listachorob = []
    def dodajChorobe(self, choroba):
        self.listachorob.append(choroba)
    def wypiszChoroby(self):
        for x in self.listachorob:
            print(f"Choroba: {choroba}\n")
listaprzychodni = []
while(True):

    menu = int(input("1-Przychodnia, 2-Pacjent, 3-Koniec"))
    if menu == 1:
        menu2 = int(input("1-dodaj przychodnie, 2-usun przychodnie, 3-dodaj pacjenta do przychodni, 4-lista przychodni, 5-lista pacjentow przychodni: "))
        if menu2 == 1:
            nazwa = input(f"Podaj nazwe przychodni: ")
            miasto = input(f"Podaj miasto, w którym znajduje się przychodnia: ")
            przychodnia = Przychodnia(nazwa, miasto)
            listaprzychodni.append(przychodnia)
        elif menu2 == 2:
            nazwa = input(f"Podaj nazwe przychodni, ktora chcesz usunac: ")
            znaleziono = "NIE"
            for x in listaprzychodni:
                if nazwa in x.nazwa:
                    znaleziono = "TAK"
                    listaprzychodni.remove(x)
                    print("Pomyslnie usunieto przychodnie")
            if znaleziono == "NIE":
                print(f"Nie odnaleziono takiej przychodni")
        elif menu2 == 3:
            nazwa = input(f"Do jakiej przychodni chcesz przypisac pacjenta? ")
            znaleziono = "NIE"
            for x in listaprzychodni:
                if nazwa in x.nazwa:
                    znaleziono = "TAK"
                    imie = input(f"Podaj imie pacjenta: ")
                    nazwisko = input(f"Podaj nazwisko pacjenta ")
                    pacjent = Pacjent(imie, nazwisko)
                    x.dodajPacjenta()
                    print("Pomyslnie dodano pacjenta!")
            if znaleziono == "NIE":
                print(f"Nie odnaleziono {nazwa} w bazie danych!")
        elif menu2 == 4:
            for x in listaprzychodni:
                print(f"Nazwa: {x.nazwa}\nMiasto: {x.miasto}\n")
        elif menu2 == 5:
            nazwa = input(f"Podaj nazwe przychodni, ktorej pacjentow chcesz wyswietlic: ")
            znaleziono = "NIE"
            for i in listaprzychodni:
                if i.nazwa == nazwa:
                    znaleziono = "TAK"
                    i.wypiszPacjentow()
                    break
            if znaleziono == "NIE":
                print(f"Nie odnaleziono {nazwa} w bazie danych")

    elif menu == 2:
        menu3 = int(input("1-dodaj chorobe pacjentowi, 2-lista chorob pacjenta: "))
        if menu3 == 1:
            nazwa = input(f"Podaj przychodnie pacjenta: ")
            znaleziono = "NIE"
            for i in listaprzychodni:
                    if i.nazwa == nazwa:
                        znaleziono = "TAK"
                        for x in i.listapacjentow:
                            nazwisko = input(f"Podaj nazwisko pacjenta któremu chcesz dodac chorobe: ")
                            if nazwisko == x.nazwisko:
                                choroba = input(f"Podaj chorobe jaka chcesz dodac pacjentowi: ")
                                x.dodajChorobe(choroba)
                                print(f"Pomyslnie dodano {choroba} pacjentowi {nazwisko} z przychodni {nazwa} ")
                                break
            if znaleziono == "NIE":
                print(f"Nie odnaleziono {nazwa} w bazie danych")
        if menu3 == 2:
            nazwa = input(f"Podaj przychodnie pacjenta: ")
            znaleziono = "NIE"
            for i in listaprzychodni:
                    if i.nazwa == nazwa:
                        znaleziono = "TAK"
                        for x in i.listapacjentow:
                            nazwisko = input(f"Podaj nazwisko pacjenta którego choroby chcesz wyswietlic: ")
                            if nazwisko == x.nazwisko:
                                x.wypiszChoroby()
                                break
