# Kursy wraz z uczestnikami oraz trenerami
class Kursant:

    def __init__(self, imie, nazwisko, email):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__email = email

    @property
    def imie(self):
        return self.__imie

    @imie.setter
    def imie(self, imie):
        self.__imie = imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @nazwisko.setter
    def nazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email


class Trener():
    def __init__(self,imiet, nazwiskot, specjalizacja):
        self.__imiet = imiet
        self.__nazwiskot = nazwiskot
        self.__specjalizacja = specjalizacja


    @property
    def imiet(self):
        return self.__imiet

    @imiet.setter
    def imiet(self, imiet):
        self.__imiet = imiet

    @property
    def nazwiskot(self):
        return self.__nazwiskot

    @nazwiskot.setter
    def nazwiskot(self, nazwiskot):
        self.__nazwiskot = nazwiskot

    @property
    def specjalizacja(self):
        return self.__specjalizacja

    @specjalizacja.setter
    def specjalizacja(self, specjalizacja):
        self.__specjalizacja = specjalizacja

class Kurs():

    def __init__(self, nazwa, miasto,termin):
        self.__nazwa = nazwa
        self.__miasto = miasto
        self.__termin = termin
        self.__trener = []
        self.listaKursantow = []
    def dodajTrenera(self):
        self.__trener.append(trener)


    @property
    def nazwa(self):
        return self.__nazwa

    @nazwa.setter
    def nazwa(self, nazwa):
        self.__nazwa = nazwa

    @property
    def miasto(self):
        return self.__miasto

    @miasto.setter
    def miasto(self, miasto):
        self.__miasto = miasto

    @property
    def trener(self):
        return self.__trener

    @trener.setter
    def trener(self, trener):
        self.__trener = trener

    @property
    def termin(self):
        return self.__termin

    @termin.setter
    def termin(self, termin):
        self.__termin = termin



listaKursow = []

while (True):

    menu = int(input("1-dodaj kurs, 2-wyswietl kursy, 3-dodaj kursanta do kursu, 4-wyswietl kursantow z danego kursu, "
                     "5-usun kursanta z kursu, 6-usun kurs, 7-koniec,\n8-Dodaj trenera do kursu, 9-Usun trenera z kursu "
                     "10-Modyfikuj dane uczestnika 11-Modyfikuj dane trenera"))



    if menu == 1:
        nazwa = input(f"Podaj nazwe kursu ")
        miasto = input(f"Podaj miasto, w ktorym odbywa sie kurs: ")
        termin = input(f"Podaj termin, w którym rozpoczyna sie kurs: ")
        kurs = Kurs(nazwa, miasto,termin)
        listaKursow.append(kurs)
        # pytania: nazwa, miasto
    elif menu == 8:
        kurs = input(f"Do jakiego kursu chcesz przypisac trenera? ")
        znaleziono = "NIE"
        for x in listaKursow:
            if x.nazwa == kurs:
                znaleziono = "TAK"
                imiet = input(f"Podaj imie trenera: ")
                nazwiskot = input(f"Podaj nazwisko trenera: ")
                specjalizacja = (input(f"Podaj specjalizacje trenera: "))
                trener = Trener(imiet, nazwiskot, specjalizacja)
                x.dodajTrenera()
                break
            if znaleziono == "NIE":
                print(f"Nie ma takiego kursu.")
    elif menu == 9:
        kurs = input(f"Z jakiego kursu chcesz usunac trenera? ")
        znaleziono = "NIE"
        znalezionoTrenera = "NIE"
        for x in listaKursow:
            if kurs == x.nazwa:
                znaleziono = "TAK"
                trener = input(f"Podaj nazwisko trenera, ktorego chcesz usunac z kursu: ")
                for y in x.trener:
                    if y.nazwiskot == trener:
                        znalezionoTrenera = "TAK"
                        x.trener.remove(y)
                        print("Pomyslnie usunieto trenera")
                if znalezionoTrenera == "NIE":
                    print(f"Nie znaleziono takiego trenera.")
        if znaleziono == "NIE":
            print(f"Nie odnaleziono takiego kursu")
    elif menu == 10:
        nazwa = input(f"Podaj nazwe kursu, z ktorego pochodzi uczestnik do modyfikacji: ")
        znaleziono = "NIE"
        for x in listaKursow:
            if nazwa == x.nazwa:
                znaleziono = "TAK"
                for i in x.listaKursantow:
                    nazwisko = input(f"Podaj nazwisko kursanta: ")
                    znalezionoKursanta = "NIE"
                    if nazwisko == i.nazwisko:
                        znalezionoKursanta = "TAK"
                        noweImie = input("Podaj nowe imie: ")
                        noweNazwisko = input("Podaj nowe nazwisko: ")
                        nowyEmail = input("Podaj nowy email: ")
                        i.imie = noweImie
                        i.nazwisko = noweNazwisko
                        i.email = nowyEmail
                        print("Pomyslnie zmieniono dane kursanta!")
                        break
                    elif znalezionoKursanta == "NIE":
                        print(f"Nie znaleziono takiego kursanta.")
            elif znaleziono == "NIE":
                print(f"Nie znaleziono takiego kursu.")
    elif menu == 11:
        nazwa = input(f"Podaj nazwe kursu, z ktorego pochodzi trener do modyfikacji: ")
        znaleziono = "NIE"
        for x in listaKursow:
            if nazwa == x.nazwa:
                znaleziono = "TAK"
                for i in x.trener:
                    nazwiskot = input(f"Podaj nazwisko trenera: ")
                    znalezionoTrenera = "NIE"
                    if nazwiskot == i.nazwiskot:
                        znalezionoTrenera = "TAK"
                        noweImiet = input("Podaj nowe imie: ")
                        noweNazwiskot = input("Podaj nowe nazwisko: ")
                        nowaSpecjalizacja = input("Podaj nowy email: ")
                        i.imiet = noweImiet
                        i.nazwiskot = noweNazwiskot
                        i.specjalizacja = nowaSpecjalizacja
                        print("Pomyslnie zmieniono dane trenera!")
                        break
                    elif znalezionoTrenera == "NIE":
                        print(f"Nie znaleziono takiego trenera.")
            elif znaleziono == "NIE":
                print(f"Nie znaleziono takiego kursu.")
    elif menu == 2:
        for x in listaKursow:
            print(f"Nazwa: {x.nazwa}\nMiasto: {x.miasto}\nTermin: {x.termin}\n")
            for i in x.trener:
                print(f"Trener: {i.imiet} {i.nazwiskot} Specjalizacja: {i.specjalizacja}")
            for y in x.listaKursantow:
                print(f"Uczestnik: {y.imie} {y.nazwisko} Email: {y.email}")
    elif menu == 3:
        kurs = input(f"Na jaki kurs chcesz sie zapisac?")
        znaleziono = "NIE"
        for x in listaKursow:
            if len(x.listaKursantow) == 5:
                znaleziono = "TAK"
                print("Niestety kurs posiada maksymalna liczbe uczestnikow.")
                break
            elif x.nazwa == kurs:
                znaleziono = "TAK"
                imie = input(f"Podaj imie kursanta: ")
                nazwisko = input(f"Podaj nazwisko kursanta: ")
                email = (input(f"Podaj email kursanta: "))
                kursant = Kursant(imie, nazwisko, email)
                x.listaKursantow.append(kursant)
                break
        if znaleziono == "NIE":
            print(f"Nie ma takiego kursu.")
    elif menu == 4:
        kurs = input(f"Liste kursantow jakiego kursu chcesz wyswietlic?")
        for x in listaKursow:
            if kurs == x.nazwa:
                for i in x.listaKursantow:
                    print(i.imie, i.nazwisko)
            break
        else:
            print(f"Nie ma takiego kursu.")
    elif menu == 5:
        kurs = input(f"Z jakiego kursu chcesz usunac kursanta?")
        znaleziono = "NIE"
        znalezionoKursanta = "NIE"
        for x in listaKursow:
            if kurs == x.nazwa:
                znaleziono = "TAK"
                kursant = input(f"Podaj nazwisko kursanta, ktorego chcesz usunac z kursu: ")
                for y in x.listaKursantow:
                    if y.nazwisko == kursant:
                        znalezionoKursanta = "TAK"
                        x.listaKursantow.remove(y)
                        print("Pomyslnie usunieto kursanta")
                if znalezionoKursanta == "NIE":
                    print(f"Nie znaleziono takiego kursanta")
        if znaleziono == "NIE":
                print(f"Nie odnaleziono takiego kursu")
    elif menu == 6:
        kurs = input("Podaj nazwe kursu, ktory chcesz usunac ")
        znaleziono = "NIE"
        for x in listaKursow:
            if x.nazwa == kurs:
                if len(x.listaKursantow) == 0:
                    znaleziono = "TAK"
                    listaKursow.remove(x)
                elif len(x.listaKursantow) > 0:
                    print(f"Niestety nie mozna usunac kursu jeśli są przypisani do niego kursanci.")
                break
        if znaleziono == "NIE":
            print("Nie ma takiego kursu")
    elif menu == 7:
        break
