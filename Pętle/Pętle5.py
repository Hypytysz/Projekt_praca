# Potęga bez użycia operatora **
podstawa = int(input(f"Podaj podstawe "))
potega = int(input(f"Podaj potege "))
suma = 1
for i in range(potega):
    suma = suma * podstawa
print(f"{podstawa} do potegi {potega} = {suma}")
