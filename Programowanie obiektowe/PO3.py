# Zakupy z paragonem
class Koszyk:

    def __init__(self):
        self.zakupy = {}

    def dodajProdukt(self, produkt, ilosc):
        if produkt in self.zakupy:
            self.zakupy[produkt] += ilosc
        else:
            self.zakupy[produkt] = ilosc

    def usunProdukt(self, produkt, ilosc):
        if produkt in self.zakupy:
            if self.zakupy[produkt] < ilosc:
                print("W koszyku nie ma takiej ilosci produktu.")
            elif self.zakupy[produkt] == ilosc:
                self.zakupy.pop(produkt)
                print("Pomyslnie usunieto produkt z koszyka.")
            else:
                self.zakupy[produkt] -= ilosc
                print("Pomyslnie usunieto odpowiednia ilosc produktu w koszyku.")
        else:
            print("Produkt nie znajduje sie w Twoim koszyku.")
magazyn = {"chleb":2.50, "sok":1.80, "woda":3.0, "piwo":5.50}
listaKoszykow = []

while(True):

    klient = input("Czy chcesz rozpocząc zakupy T/N").upper()

    if(klient == "T"):

        koszyk = Koszyk()

        while(True):
            dec = input("Co robimy ? D - dodaj, U - usun, P - podglad, K - koniec ").upper()

            if(dec == "D"):
                produkt = input("Jaki produkt chcesz dodac?")
                ilosc = int(input(f"Ile {produkt} chcesz dodac?"))
                koszyk.dodajProdukt(produkt, ilosc)
            elif(dec == "P"):
                for i in koszyk.zakupy:
                    print(f"Produkt: {i} Ilosc: {koszyk.zakupy[i]}")

            elif(dec == "U"):
                produkt = input("Jaki produkt chcesz usunac?")
                ilosc = int(input(f"Ile {produkt} chcesz usunac?"))
                koszyk.usunProdukt(produkt, ilosc)

            elif(dec == "K"):
                listaKoszykow.append(koszyk)
                break

    elif(klient == "N"):
        nr = 1
        print(f"Koszyk nr: {nr}")
        for i in listaKoszykow:
            suma = 0
            for x in i.zakupy:
                wartosc = i.zakupy[x] * magazyn[x]
                suma = suma + wartosc
                print(f"Produkt: {x} Ilosc {i.zakupy[x]} Cena: {magazyn[x]}")
            print(f"Razem do zaplaty: {suma}")
            nr += 1
        break
