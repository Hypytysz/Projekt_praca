#Pole wybranej figury
z1= int(input("Wybierz 1 jesli chcesz policzyc pole trojkata, wcisnij 2 jesli chcesz policzyc pole prostokatu. "))


if z1==1:
    z4= int(input(f"Podaj dlugosc podstawy "))
    z5= int(input(f"Podaj wysokosc trojkata "))
    trojkat = (z4 * z5) / 2
    print(f"Pole wynosi: {trojkat}")
elif z1==2:
    z2= int(input(f"Podaj dlugosc boku a "))
    z3= int(input(f"Podaj dlugosc boku b "))
    prostokat = z2 * z3
    print(f"Pole wynosi: {prostokat}")
else:
    print(f"Podales nieprawidlowa wartosc. Sprobuj jeszcze raz.")
