# Książka telefoniczna
from tkinter import *

kontakty= []
class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

def dodajKontakt():
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    telefon = entry_telefon.get()
    email = entry_email.get()

    kontakt = Kontakt(imie, nazwisko, telefon, email)
    kontakty.append(kontakt)

    entry_imie.delete(0,END)
    entry_nazwisko.delete(0,END)
    entry_telefon.delete(0,END)
    entry_email.delete(0,END)
    entry_imie.focus()
    listaKontaktow()

def listaKontaktow():
    listbox_listaKontaktow.delete(0, END)
    for indeks, value in enumerate(kontakty):
        listbox_listaKontaktow.insert(indeks, f"{value.imie} {value.nazwisko}")

def pokazSzczegoly():
    index = listbox_listaKontaktow.index(ACTIVE)
    label_imieDolnaValue.config(text=kontakty[index].imie)
    label_nazwiskoDolnaValue.config(text=kontakty[index].nazwisko)
    label_telefonDolnaValue.config(text=kontakty[index].telefon)
    label_emailDolnaValue.config(text=kontakty[index].email)


def usunKontakt():
    index = listbox_listaKontaktow.index(ACTIVE)
    kontakty.pop(index)
    listaKontaktow()

def edytujKontakt():
    index= listbox_listaKontaktow.index(ACTIVE)
    entry_imie.insert(0, kontakty[index].imie)
    entry_nazwisko.insert(0, kontakty[index].nazwisko)
    entry_telefon.insert(0, kontakty[index].telefon)
    entry_email.insert(0, kontakty[index].email)


    button_dodajKontakt.config(text="Zmien kontakt", command=lambda:zmienKontakt(index))

def zmienKontakt(index):
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    telefon = entry_telefon.get()
    email = entry_email.get()

    kontakty[index].imie= imie
    kontakty[index].nazwisko= nazwisko
    kontakty[index].telefon= telefon
    kontakty[index].email= email

    entry_imie.delete(0,END)
    entry_nazwisko.delete(0,END)
    entry_telefon.delete(0,END)
    entry_email.delete(0,END)
    entry_imie.focus()
    listaKontaktow()
    button_dodajKontakt.config(text="Dodaj kontakt", command=dodajKontakt)



root = Tk()

root.title("Ksiazka telefoniczna")
root.geometry("700x300")

ramkaLewa = Frame(root)
ramkaPrawa = Frame(root)
ramkaDolna = Frame(root)

ramkaLewa.grid(row=0, column=0, sticky=N, pady=20, padx=30)
ramkaPrawa.grid(row=0,column=1, sticky=N, pady=20, padx=20)
ramkaDolna.grid(row=1, column=0, columnspan=2, sticky=W, padx=25)


# RAMKA LEWA
label_listaKontaktow = Label(ramkaLewa, text="Lista kontaktow")
listbox_listaKontaktow = Listbox(ramkaLewa, width=30, height=7)
button_pokazSzczegolyKontaktu = Button(ramkaLewa, text="Pokaz szczegoly kontaktu", command=pokazSzczegoly)
button_usunKontakt = Button(ramkaLewa, text="Usun kontakt", command=usunKontakt)
button_edytujKontakt = Button(ramkaLewa, text="Edytuj tekst", command=edytujKontakt)


label_listaKontaktow.grid(row=0, column=0, columnspan=3)
listbox_listaKontaktow.grid(row=1, column=0, columnspan=3)
button_pokazSzczegolyKontaktu.grid(row=2, column=0)
button_usunKontakt.grid(row=2, column=1)
button_edytujKontakt.grid(row=2, column=2)

# RAMKA PRAWA
label_nowyKontakt = Label(ramkaPrawa, text="Nowy kontakt")
label_imie = Label(ramkaPrawa, text="Imie")
label_nazwisko = Label(ramkaPrawa, text="Nazwisko")
label_telefon = Label(ramkaPrawa, text="Telefon")
label_email = Label(ramkaPrawa, text="Email")
entry_imie = Entry(ramkaPrawa)
entry_nazwisko = Entry(ramkaPrawa, width=25)
entry_telefon = Entry(ramkaPrawa)
entry_email = Entry(ramkaPrawa)
# button_dodajKontakt = Button(ramkaPrawa, text="Dodaj kontrakt", command=test)
button_dodajKontakt = Button(ramkaPrawa, text="Dodaj kontrakt", command=dodajKontakt)

label_nowyKontakt.grid(row=0, column=0, columnspan=2)
label_imie.grid(row=1, column=0, sticky=W)
label_nazwisko.grid(row=2, column=0, sticky=W)
label_telefon.grid(row=3, column=0, sticky=W)
label_email.grid(row=4, column=0, sticky=W)
entry_imie.grid(row=1, column=1, sticky=W)
entry_nazwisko.grid(row=2, column=1, sticky=W)
entry_telefon.grid(row=3, column=1, sticky=W)
entry_email.grid(row=4, column=1, sticky=W)
button_dodajKontakt.grid(row=5, column=0, columnspan=2)

# RAMKA DOLNA

label_szczegolyKontaktu = Label(ramkaDolna, text="Szczegoly kontaktu")
label_imieDolna = Label(ramkaDolna, text="Imie: ")
label_imieDolnaValue = Label(ramkaDolna, text="...", width=10)
label_nazwiskoDolna = Label(ramkaDolna, text="Nazwisko: ")
label_nazwiskoDolnaValue = Label(ramkaDolna, text="...", width=10)
label_telefonDolna = Label(ramkaDolna, text="Telefon: ")
label_telefonDolnaValue = Label(ramkaDolna, text="...", width=10)
label_emailDolna = Label(ramkaDolna, text="Email:")
label_emailDolnaValue = Label(ramkaDolna, text="...", width=10)

label_szczegolyKontaktu.grid(row=0, column=0, columnspan=8, sticky=W)
label_imieDolna.grid(row=1, column=0)
label_imieDolnaValue.grid(row=1, column=1)
label_nazwiskoDolna.grid(row=1, column=2)
label_nazwiskoDolnaValue.grid(row=1, column=3)
label_telefonDolna.grid(row=1, column=4)
label_telefonDolnaValue.grid(row=1, column=5)
label_emailDolna.grid(row=1, column=6)
label_emailDolnaValue.grid(row=1, column=7)

root.mainloop()
