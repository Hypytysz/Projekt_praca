# Książka telefoniczna na pliku .dat
import pickle

class Kontakt:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefony = []
        self.emaile = []

class KontaktController:

    def __init__(self):
        self.listaKontaktow = []

    def sprawdzNazwisko(self, nazwisko):
        for x in self.listaKontaktow:
            if nazwisko == x.nazwisko:
                return True

        print("Nie znaleziono kontaktu o wskazanym nazwisku")
        return False

    def zapis(self):
        plik = open("dane.dat", "wb")
        pickle.dump(self.listaKontaktow, plik)
        plik.close()

    def dodajKontakt(self, imie, nazwisko):
        kontakt = Kontakt(imie, nazwisko)
        self.listaKontaktow.append(kontakt)
        self.zapis()


    def pokazKontakty(self):
        for x in self.listaKontaktow:
            print(f"Nazwa: {x.imie}\nNazwisko: {x.nazwisko}\nTelefony: {x.telefony}\nEmaile: {x.emaile}")



    def usunKontakt(self, nazwisko):
        znaleziono = "NIE"
        for i in self.listaKontaktow:
            if nazwisko == i.nazwisko:
                znaleziono = "TAK"
                self.listaKontaktow.remove(i)
                print(f"Pomyslnie usunieto {nazwisko} z kontaktow")
                self.zapis()
        if znaleziono == "NIE":
            print("Nie znaleziono takiego kontaktu")

    def dodajTelefon(self, nazwisko, telefon):
        znaleziono = "NIE"
        for x in self.listaKontaktow:
            if nazwisko == x.nazwisko:
                znaleziono = "TAK"
                x.telefony.append(telefon)
                print("Pomyslnie dodano numer telefonu!")
                self.zapis()
        if znaleziono == "NIE":
            print("Nie znaleziono takiego kontaktu")

    def usunTelefon(self, nazwisko, telefon):
        znaleziono = "NIE"
        for x in self.listaKontaktow:
            if nazwisko == x.nazwisko:
                znaleziono = "TAK"
                x.telefony.remove(telefon)
                print("Pomyslnie usunieto numer telefonu!")
                self.zapis()
        if znaleziono == "NIE":
            print("Nie znaleziono takiego kontaktu")

    def dodajEmail(self, nazwisko, email):
        znaleziono = "NIE"
        for x in self.listaKontaktow:
            if nazwisko == x.nazwisko:
                znaleziono = "TAK"
                x.emaile.append(email)
                print("Pomyslnie dodano email!")
                self.zapis()
        if znaleziono == "NIE":
            print("Nie znaleziono takiego kontaktu")

    def usunEmail(self, nazwisko, email):
        znaleziono = "NIE"
        for x in self.listaKontaktow:
            if nazwisko == x.nazwisko:
                znaleziono = "TAK"
                x.emaile.remove(email)
                print("Pomyslnie usunieto numer email!")
                self.zapis()
        if znaleziono == "NIE":
            print("Nie znaleziono takiego kontaktu")


class App(KontaktController):

    def __init__(self):
        super().__init__()
        try:
            plik = open("dane.dat", "rb")
            self.listaKontaktow = pickle.load(plik)
            self.menu()
        except:
            plik = open("dane.dat", "wb")
            pickle.dump(self.listaKontaktow, plik)
            plik.close()


    def menu(self):

        while(True):
            menu = input("1-dodaj kontakt, 2-pokaz kontakty, 3-usun kpontakt, 4-dodaj telefon, 5-usun telefon,"
                         "6-dodaj enail, 7-usun email, 8-koniec")
            if menu == "1":
                imie = input("Podaj imie: ")
                nazwisko = input("Podaj nazwisko: ")
                self.dodajKontakt(imie, nazwisko)
            elif menu == "2":
                self.pokazKontakty()
            elif menu == "3":
                nazwisko = input("Podaj nazwisko kontaktu, ktory chcesz usunac: ")
                self.usunKontakt(nazwisko)
            elif menu == "4":
                nazwisko = input("Podaj nazwisko kontaktu, ktoremu chcesz dodac telefon: ")
                if(self.sprawdzNazwisko(nazwisko) == True):
                    telefon = int(input("Podaj numer, ktory chcesz dodac: "))
                    self.dodajTelefon(nazwisko, telefon)
            elif menu == "5":
                nazwisko = input("Podaj nazwisko kontaktu, ktorego telefon chcesz usunac: ")
                if(self.sprawdzNazwisko(nazwisko) == True):
                    telefon = int(input("Podaj telefon, ktory chcesz dodac: "))
                    self.usunTelefon(nazwisko, telefon)
            elif menu == "6":
                nazwisko = input("Podaj nazwisko kontaktu, do ktorego chcesz dodac email: ")
                if(self.sprawdzNazwisko(nazwisko) == True):
                    email = int(input("Podaj email, ktory chcesz dodac: "))
                    self.dodajEmail(nazwisko, email)
            elif menu == "7":
                nazwisko = input("Podaj nazwisko kontaktu, do ktorego chcesz dodac email: ")
                if(self.sprawdzNazwisko(nazwisko) == True):
                    email = int(input("Podaj email, ktory chcesz dodac: "))
                    self.usunEmail(nazwisko, email)
            elif menu == "8":
                break

app = App()
