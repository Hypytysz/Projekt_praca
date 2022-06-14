# Sprawdzenie twierdzenia Pitagorasa
z1= float(input("Podaj jeden bok: "))
z2 = float(input("Podaj drugi bok: "))
z3 = float(input("Podaj trzeci bok: "))

if (z1**2)+(z2**2)==(z3**2):
    print(f"Ten trojkat moze byc prostokatny")
elif (z2**2)+(z1**2)==(z3**2):
    print(f"Ten trojkat moze byc prostokatny")
elif (z3**2)+(z1**2)==(z2**2):
    print(f"Ten trojkat moze byc prostokatny")
elif (z3**2) + (z2**2) == (z1**2):
    print(f"Ten trojkat moze byc prostokatny")
else:
    print(f"Ten trojkat nie moze byc prostokatny")
