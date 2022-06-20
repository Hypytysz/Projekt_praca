# Wykresy z danych txt
import matplotlib.pyplot as plt

miastaSrednia = {}
miasta = {"Warszawa":0,"Kraków":0,"Wrocław":0, "Gdańsk":0,"Poznań":0, "Szczecin":0, "Bydgoszcz":0,"Katowice":0}
calkowitasrednia = []
plik = open("dane4.txt", "r", encoding="utf-8")



while True:
    for i in plik:
        i = i.strip()
        x = i.split(";")
        for y in x:
            if x[2] in miastaSrednia:
                miasta[x[2]] += 1
                miasto = x[2]
                libcza1 = float(miastaSrednia[x[2]])
                libcza2 = float(x[1])
                wynik = libcza1 + libcza2
                miastaSrednia[miasto] = wynik
                break
            else:
                miasto = x[2]
                miastaSrednia[miasto] = x[1]
                break

    break
while True:
    for i in miastaSrednia:
        miasto = i
        srednia = miastaSrednia[i] / miasta[i]
        miastaSrednia[i] = srednia
        calkowitasrednia.append(srednia)
    break
etykieta = ["Warszawa","Kraków", "Wrocław", "Gdańsk", "Poznań", "Szczecin", "Bydgoszcz", "Katowice"]
plt.bar(etykieta, calkowitasrednia)
plt.show()
print(miastaSrednia)
plik.close()
