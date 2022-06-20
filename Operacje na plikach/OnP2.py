# Lista studentow z ocenami i srednia na pliku .txt
def dodaj(imie, nazwisko, grupa, ocena, srednia):
    plik = open("studenci.txt", "a", encoding="utf-8")
    plik.write(f"{imie};{nazwisko};{grupa};{ocena};{srednia}\n")
    plik.close()

def pokaz():
    plik = open("studenci.txt", "r", encoding="utf-8")
    for i in plik:
        x = i.split(";")
        print(f"Imie: {x[0]} Nazwisko: {x[1]} "
              f"Grupa: {x[2]} Oceny: {x[3]} Srednia: {x[4]}\n")
    plik.close()
def usun(imie, nazwisko):
    studenci = []
    plik = open("studenci.txt", "r", encoding="utf-8")
    for i in plik:
        x = i.split(";")
        if (x[0] != imie and x[1] != nazwisko):
            studenci.append(i)
        elif (x[0] == imie and x[1] != nazwisko):
            studenci.append(i)
            print("Nie znaleziono studenta o takim imieniu i nazwisku")
        elif (x[0] !=imie and x[1] == nazwisko):
            studenci.append(i)
            print(f"Nie znaleziono studenta o takim imieniu i nazwisku")
    plik.close()
    plik = open("studenci.txt", "w", encoding="utf-8")
    plik.writelines(studenci)
    plik.close()
def zmien(imie, nazwisko, noweImie, noweNazwisko, nowaGrupa):
    studenci = []
    plik = open("studenci.txt", "r", encoding="utf-8")
    for i in plik:
        x = i.split(";")
        if (x[0] != imie and x[1] != nazwisko):
            studenci.append(i)
        elif (x[0] == imie and x[1] != nazwisko):
            studenci.append(i)
        elif (x[0] !=imie and x[1] == nazwisko):
            studenci.append(i)
        elif (x[0] == imie and x[1] == nazwisko):
            studenci.append(f"{noweImie};{noweNazwisko};{nowaGrupa};{x[3]};{x[4]}")
    plik.close()
    plik = open("studenci.txt", "w", encoding="utf-8")
    plik.writelines(studenci)
    plik.close()
def dodajOcene(imie, nazwisko, oceny):
    studenci = []
    plik = open("studenci.txt", "r", encoding="utf-8")
    for i in plik:
        x = i.split(";")
        if (x[0] != imie and x[1] != nazwisko):
            studenci.append(i)
        if (x[0] == imie and x[1] != nazwisko):
            studenci.append(i)
        if (x[0] !=imie and x[1] == nazwisko):
            studenci.append(i)
        if x[0] == imie and x[1] == nazwisko:
            for indeks, y in enumerate(x[3]):
                if y == "0":
                    suma = oceny
                    srednia = suma / 1
                    studenci.append(f"{imie};{nazwisko};{x[2]};{oceny};{srednia}\n")
                    break
                if y != "0":
                    x = i.split(";")
                    b = x[3].split(",")
                    c = len(b) + 1
                    suma = oceny
                    for y in b:
                        suma += int(y)
                    srednia = suma / c
                    studenci.append(f"{imie};{nazwisko};{x[2]};{x[3]},{oceny};{srednia}\n")
                    break

    plik.close()
    plik = open("studenci.txt", "w", encoding="utf-8")
    plik.writelines(studenci)
    plik.close()

while(True):

    menu = input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-dodaj ocene, 6-koniec")

    if menu == "1":
        imie = input(f"Podaj imie: ")
        nazwisko = input(f"Podaj nazwisko: ")
        grupa = input(f"Podaj grupe: ")
        ocena = int()
        srednia = 0
        dodaj(imie, nazwisko, grupa, ocena, srednia)
    elif menu == "2":
        pokaz()
    elif menu == "3":
        imie = input(f"Podaj imie")
        nazwisko = input(f"Podaj nazwisko: ")
        usun(imie, nazwisko)
    elif menu == "4":
        imie = input(f"Podaj imie: ")
        nazwisko = input(f"Podaj nazwisko: ")
        noweImie = input(f"Podaj nowe imie: ")
        noweNazwisko = input(f"Podaj nowe nazwisko: ")
        nowaGrupa = input(f"Podaj nowa grupe: ")
        zmien(imie, nazwisko, noweImie, noweNazwisko, nowaGrupa)
    elif menu == "5":
        imie = input(f"Podaj imie: ")
        nazwisko = input(f"Podaj nazwisko: ")
        oceny = int(input(f"Podaj ocene: "))
        dodajOcene(imie, nazwisko, oceny)
    elif menu == "6":
        break
