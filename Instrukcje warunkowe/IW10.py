#Wprowadzenie 2och liczb i operatora matematycznego:
z1= int(input("Podaj pierwsza liczbe: "))
z2 =int((input(f"Podaj znak rownania:\n1 = x\n2 = /\n3 = +\n4 = -\n ")))
z3 =int(input("Podaj druga liczbe: "))
mno = z1*z3
dzi = z1/z3
dod = z1+z3
ode = z1-z3

if z2 == 1:
    print(f"Wynik mnozenia wynosi: {mno}")
elif z2 == 2:
    print(f"Wynik dzielenia wynosi: {dzi}")
elif z2 == 3:
    print(f"Wynik dodawania wynosi: {dod}")
elif z2 == 4:
    print(f"Wynik odejmowania wynosi: {ode}")
else:
    print(f"Niestety podales nieprawidlowe dane")
