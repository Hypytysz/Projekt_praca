# Lista pracowników i firm (operacje na pliku .dat)
import pickle

class Kontakt:

    def __init__(self, nazwa, miasto, pracownicy):
        self.nazwa = nazwa
        self.miasto = miasto
        self.pracownicy = pracownicy

class KontaktController():

    def __init__(self):
        super().__init__()
        self.listaKontaktow = []

    def zapis(self):
        plik = open("dane3.dat", "wb")
        pickle.dump(self.listaKontaktow, plik)
        plik.close()

    def dodajKontakt(self, nazwa, miasto, pracownicy):
        plik = Kontakt(nazwa, miasto, pracownicy)
        self.listaKontaktow.append(plik)
        self.zapis()

    def pokazKontakty(self):
        for x in self.listaKontaktow:
            print(f"Nazwa: {x.nazwa}\nMiasto: {x.miasto}\nPracownicy: {x.pracownicy}")

    def usunKontakt(self, nazwa):
        znaleziono = "NIE"
        for i in self.listaKontaktow:
            if nazwa == i.nazwa and len(i.pracownicy) == 0:
                znaleziono = "TAK"
                self.listaKontaktow.remove(i)
                print(f"Pomyslnie usunieto {nazwa} z listy firm.")
                self.zapis()
            if nazwa == i.nazwa and len(i.pracownicy) != 0:
                znaleziono = "TAK"
                print("Nie mozna usunac firmy jezeli posiada pracownikow.")
        if znaleziono == "NIE":
            print("Nie znaleziono takiej firmy.")


class Pracownik():

    def __init__(self, imie, nazwisko, firmy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.firmy = firmy

class PracownikController(KontaktController):

    def __init__(self):
        super().__init__()
        self.listaPracownikow = []

    def zapisPracownika(self):
        pracownik = open("dane3.dat", "wb")
        pickle.dump(self.listaPracownikow, pracownik)
        pracownik.close()

    def dodajPracownika(self, imie, nazwisko, firmy):
        pracownik = Pracownik(imie, nazwisko, firmy)
        self.listaPracownikow.append(pracownik)
        self.zapisPracownika()

    def pokazPracownikow(self):
        for x in self.listaPracownikow:
            print(f"Nazwa: {x.imie}\nNazwisko: {x.nazwisko}\n")

    def usunPracownika(self, nazwisko):
        znaleziono = "NIE"
        for i in self.listaPracownikow:
            if nazwisko == i.nazwisko and len(i.firmy) == 0:
                znaleziono = "TAK"
                self.listaPracownikow.remove(i)
                print(f"Pomyslnie usunieto {nazwisko} z listy pracownikow")
                self.zapisPracownika()
            elif nazwisko == i.nazwisko and len(i.firmy) != 0:
                znaleziono = "TAK"
                print("Nie mozna usunac zatrudnionego pracownika.")
        if znaleziono == "NIE":
            print("Nie znaleziono takiego pracownika lub pracownik posiada zatrudnienie")

    def dodajFirme(self, imie, nazwisko, firma):
        znaleziono = "NIE"
        for i in self.listaPracownikow:
            if imie == i.imie and nazwisko == i.nazwisko:
                znaleziono = "TAK"
                i.firmy.append(firma)
                print(f"Pomyslnie dodano {firma} do {nazwisko}.")
                self.dodajPracownikadoFirmy(nazwisko, firma)
                self.zapisPracownika()
        if znaleziono == "NIE":
            print("Nie znaleziono takiego kontaktu")

    def usunFirme(self, nazwisko, firma):
        znaleziono = "NIE"
        for i in self.listaPracownikow:
            if nazwisko == i.nazwisko:
                znaleziono = "TAK"
                i.firmy.remove(firma)
                self.usunPracownikazFirmy(nazwisko, firma)
                print(f"Pomyslnie usunieto {nazwisko} z listy firm")
                self.zapisPracownika()
            else:
                print(f"Pracownik nie jest tam zatrudniony.")
        if znaleziono == "NIE":
            print("Nie znaleziono takiego kontaktu")

    def dodajPracownikadoFirmy(self,nazwisko, firma):
        for y in self.listaKontaktow:
            if firma == y.nazwa:
                y.pracownicy.append(nazwisko)
                self.zapis()

    def usunPracownikazFirmy(self,nazwisko, firma):
        for y in self.listaKontaktow:
            if firma == y.nazwa:
                y.pracownicy.remove(nazwisko)
                self.zapis()

    def pokazFirmy(self):
        for x in self.listaPracownikow:
            print(f"Nazwa: {x.imie}\nNazwisko: {x.nazwisko}\nFirmy: {x.firmy}")

class App(PracownikController):

    def __init__(self):
        super().__init__()
        try:
            plik = open("dane3.dat", "rb")
            self.listaKontaktow = pickle.load(plik)
            self.listaPracownikow = pickle.load(plik)
            self.menu()

        except:
            plik = open("dane3.dat", "wb")
            pickle.dump(self.listaKontaktow, plik)
            pickle.dump(self.listaPracownikow, plik)
            plik.close()

    def menu(self):

        while(True):
            menu = input("1-firma, 2-pracownik 3-zatrudnienie")
            if menu == "1":
                menu = input("1-dodaj firme, 2-pokaz liste firm, 3-usun firme")
                if menu == "1":
                    nazwa = input("Podaj nazwe firmy: ")
                    miasto = input("Podaj miasto: ")
                    pracownicy = []
                    self.dodajKontakt(nazwa, miasto, pracownicy)
                elif menu == "2":
                    self.pokazKontakty()
                elif menu == "3":
                    nazwa = input("Podaj nazwe firmy, ktora chcesz usunac: ")
                    self.usunKontakt(nazwa)
            elif menu == "2":
                menu = input("1-dodaj pracownika, 2-pokaz pracownikow, 3-usun pracownika")
                if menu == "1":
                    imie = input("Podaj imie: ")
                    nazwisko = input("Podaj nazwisko: ")
                    firmy = []
                    self.dodajPracownika(imie, nazwisko, firmy)
                elif menu == "2":
                    self.pokazPracownikow()
                elif menu == "3":
                    nazwisko = input("Podaj nazwisko pracownika, ktorego chcesz usunac: ")
                    self.usunPracownika(nazwisko)
            elif menu == "3":
                menu = input("1-dodaj firme pracownikowi, 2-pokaz firmy pracownika, 3-usun firme pracownika")
                if menu == "1":
                    imie = input("Podaj imie pracownika")
                    nazwisko = input("Podaj nazwisko pracownika: ")
                    firma = input("Podaj nazwe firmy: ")
                    self.dodajFirme(imie, nazwisko, firma)
                elif menu == "2":
                    self.pokazFirmy()
                elif menu == "3":
                    nazwisko = input("Podaj nazwisko pracownika, ktoremu chcesz usunac firme: ")
                    firma = input("Podaj nazwe firmy, ktora chcesz usunac")
                    self.usunFirme(nazwisko, firma)
            elif menu == "8":
                break

app = App()
