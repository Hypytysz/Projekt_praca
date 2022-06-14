# Pole lub obwod dowolnego prostokata
z1= float(input("Podaj pierwszy bok: "))
z2= float(input("Podaj drugi bok: "))
obwod= (2*z1)+(2*z2)
pole= z1*z2


z3= float((input("Jesli chcesz policzyc obwod wybierz 1 jesli chcesz policzyc pole wcisnij 2 ")))
if z3==1:
    print(f"Obwod prostokata wynosi {obwod} cm")
elif z3==2:
    print(f"Pole prostokata wynosi {pole} cm kwadratowych")
else:
    print(f"Podales nieprawidlowa wartosc. Sprobuj jeszcze raz")
