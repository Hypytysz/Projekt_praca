# Modyfikacja bazy danych pracowników
import pymysql

try:
    conn = pymysql.connect(host='localhost', user='root', password='admin', database='baza93', charset='utf8')
    c = conn.cursor()
    print('połączenie ustanowione!')
except:
    print("błąd połączenia")


def dodaj(imie, nazwisko, pensja):
    sql=f"insert into pracownicy(imie, nazwisko, pensja) values('{imie}','{nazwisko}', {pensja})"
    c.execute(sql)

    dec = input("Czy dodac dane do bazy? T/N").upper()
    if(dec =="T"):
        conn.commit()
        print("Dane zostaly dodane.")
    else:
        conn.rollback()
        print("Operacja została anulowana.")
    pass


def pokaz():
    sql = "SELECT * from pracownicy"
    c.execute(sql)
    dane = c.fetchall()
    for i in dane:
        print(f"Imie: {i[1]}, Nazwisko: {i[2]}, Pensja: {i[3]}")

def usun(nazwisko):
    sql =f"Select * from pracownicy where nazwisko ='{nazwisko}'"
    c.execute(sql)
    dane = c.fetchall()
    if len(dane) > 0:
        odp = input("Chcesz wykonac te operacje? T/N ")
        dec = f"Delete from pracownicy where id ='{dane[0][0]}'"
        c.execute(dec)
        if odp == "T":
            conn.commit()
            print("Usunieto pracownika")
        elif odp == "N":
            conn.rollback()
            print("Operacja zostala anulowana.")
        else:
            conn.rollback()
            print("Podano nieprawidlowa odpowiedz. Operacja zostala anulowana.")
    else:
        print("Nie znaleziono takiego pracownika!")

def zmien(nazwisko):
    sql =f"Select * from pracownicy where nazwisko ='{nazwisko}'"
    c.execute(sql)
    dane = c.fetchall()
    if len(dane) > 0:
        noweImie = input("Podaj nowe imie: ")
        noweNazwisko = input("Podaj nowe nazwisko:: ")
        nowaPensja = int(input("Podaj nowa pensje: "))
        dec = f"update pracownicy set imie='{noweImie}', nazwisko= '{noweNazwisko}', pensja = {nowaPensja} where {dane[0][0]}"
        odp = input("Chcesz wykonac te operacje? T/N ")
        c.execute(dec)
        if odp == "T":
            conn.commit()
            print("Zmieniono dane pracownika")
        elif odp == "N":
            conn.rollback()
            print("Operacja zostala anulowana.")
        else:
            conn.rollback()
            print("Podano nieprawidlowa odpowiedz. Operacja zostala anulowana.")
    else:
        print("Nie znaleziono takiego pracownika.")

def szukaj(dana):
    sql =f"Select * from pracownicy where imie like '%{dana}%' or nazwisko like '%{dana}%' or pensja like '%{dana}%'"
    c.execute(sql)
    dane = c.fetchall()
    if len(dane) > 0:
        for i in dane:
            print(f"Imie: {i[1]}, Nazwisko: {i[2]}, Pensja: {i[3]}")
    else:
        print("Nie znaleziono takiego pracownika")

while (True):

    menu = input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-szukaj, 6-koniec")

    if (menu == "1"):
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        pensja = int(input("Podaj pensje: "))
        dodaj(imie, nazwisko, pensja)
    elif (menu == "2"):
        pokaz()
    elif (menu == "3"):
        nazwisko = input("Podaj nazwisko pracownika, ktorego chcesz usunac: ")
        usun(nazwisko)
    elif (menu == "4"):
        nazwisko = input("Podaj nazwisko pracownika, ktorego dane chcesz zmienic: ")
        zmien(nazwisko)
        pass
    elif (menu == "5"):
        dana = input("Podaj fraze po jakiej chcesz wyszukac pracownika: ")
        szukaj(dana)
    elif (menu == "6"):
        print("koniec")
        conn.close()
        break
    else:
        print("Nierozpoznana opcja menu")
