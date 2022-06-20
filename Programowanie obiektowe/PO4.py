# Lista pracowników na polach prywatnych
class Pracownik:
    def __init__(self, imie, nazwisko, kontrakt, pensja):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__kontrakt = kontrakt
        self.__pensja = pensja

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
    def nazwisko(self,nazwisko):
        self.__nazwisko = nazwisko

    @property
    def kontrakt(self):
        return self.__kontrakt
    @kontrakt.setter
    def kontrakt(self, kontrakt):
        self.__kontrakt = kontrakt

    @property
    def pensja(self):
        return self.__pensja
    @pensja.setter
    def pensja(self, pensja):
        self.__pensja = pensja


    def __str__(self):
        return f"Imie: {self.__imie} Nazwisko: {self.__nazwisko} Kontrakt: {self.__kontrakt} Pensja: {self.__pensja}"

class PracownikController:

    def __init__(self):
        self.listaPracownikow = []

    def dodajPracownika(self,imie, nazwisko, kontrakt="staz", pensja=1000 ):
        pracownik =Pracownik(imie, nazwisko,kontrakt,pensja)
        self.listaPracownikow.append(pracownik)
        print("Pracownik zostal pomyslnie dodany")
    def pokazPracownikow(self):
        for i in self.listaPracownikow:
            print(i)
    def usunPracownika(self, nazwisko):
        znaleziono = 0
        for i in self.listaPracownikow:
            if nazwisko == i.nazwisko:
                znaleziono = 1
                self.listaPracownikow.remove(i)
                print(f"Pomyslnie usunieto pracownika o nazwisku: {nazwisko}")
        if znaleziono == 0:
            print(f"Nie ma pracownika o nazwisku {nazwisko}")
    def zmienKontrakt(self, nazwisko, pensja):
        znaleziono = 0
        for x in self.listaPracownikow:
            if nazwisko == x.nazwisko:
                znaleziono = 1
                if x.kontrakt == "staz":
                    x.pensja = pensja
                    x.kontrakt = "etat"
                elif x.kontrakt == "etat":
                    x.pensja = pensja
                    break
        if znaleziono == 0:
            print(f"Nie znaleziono takiego pracownika")

class Firma(PracownikController):

    def __init__(self, nazwaFirmy):
        super().__init__()
        self.nazwaFirmy = nazwaFirmy
        self.menu()

    def menu(self):

        while(True):
            print(f"Witaj w firmie {self.nazwaFirmy}")
            menu = int(input("1-dodaj pracownika, 2-pokaz pracownikow, 3-usun pracownika, 4-zmien kontrakt pracownikowi, 5-koniec"))

            if menu == 1:
                imie = input(f"Podaj imie: ")
                nazwisko = input(f"Podaj nazwisko: ")
                kontrakt = input(f"Podaj kontrakt: staz/etat:")
                if kontrakt == "staz":
                    self.dodajPracownika(imie, nazwisko)
                elif kontrakt == "etat":
                    pensja =int(input("Podaj pensje: "))
                    self.dodajPracownika(imie, nazwisko, kontrakt, pensja)
            elif menu == 2:
                self.pokazPracownikow()
            elif menu == 3:
                nazwisko = input(f"Podaj nazwisko, ktore chcesz usunac: ")
                self.usunPracownika(nazwisko)
            elif menu == 4:
                nazwisko = input("Podaj nazwisko pracownika, ktoremu chcesz zmienic kontrakt: ")
                pensja = input("Podaj nowa pensje: ")
                self.zmienKontrakt(nazwisko, pensja)

            elif menu == 5:
                            break


firma = Firma("XYZ Company")
