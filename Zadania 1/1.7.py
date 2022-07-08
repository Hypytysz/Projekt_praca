# Najwieksza liczba z trzech

def ktora_wieksza(x, y, z):
    if x >= y and x >= z:
        return x
    if y >= x and y >= z:
        return y
    if z >= x and z >= y:
        return z


x = input(f"Podaj 1 liczba: ")
y = input(f"Podaj 2 liczba: ")
z = input(f"Podaj 3 liczba: ")
zm = ktora_wieksza(x, y ,z)
print(zm)


