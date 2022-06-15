# Program do obliczania pola lub obwodu kola o wskazanym promieniu
z1= float(input("Podaj promien kola: "))
obwod= 2*3.14*z1
pole= 3.14*(z1**2)
jeden= 1
dwa= 2

z2= float((input("Jesli chcesz policzyc obwod wybierz 1 jesli chcesz policzyc pole kola wcisnij 2 ")))
if z2==1:
    print(f"Obwod kola wynosi {obwod}")
elif z2==2:
    print(f"Pole kola wynosi {pole}")
else:
    print(f"Podales nieprawidlowa wartosc. Sprobuj jeszcze raz")
