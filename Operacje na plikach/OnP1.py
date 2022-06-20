# Wykresy z danych txt
import matplotlib.pyplot as plt
studenciWarszawa = []
studenciSzczecin = []
studenciBydgoszcz = []
iloscstudentow = []
plik = open("dane4.txt", "r", encoding="utf-8")
for i in plik:
    x = i.split(";")
    if x[2] == "Warszawa\n":
        studenciWarszawa.append(i)
    if x[2] == "Szczecin\n":
        studenciSzczecin.append(i)
    if x[2] == "Bydgoszcz\n":
        studenciBydgoszcz.append(i)
    else:
        continue
iloscW = (len(studenciWarszawa))
iloscstudentow.append(iloscW)

iloscS = (len(studenciSzczecin))
iloscstudentow.append(iloscS)

iloscB = (len(studenciBydgoszcz))
iloscstudentow.append(iloscB)


etykieta = ["Warszawa", "Szczecin", "Bydgoszcz"]
plt.bar(etykieta, iloscstudentow)
plt.show()
plik.close()
