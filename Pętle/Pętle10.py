# Minimalna i maksymalna wartosc oraz srednia podanych liczb
liczba = 1
min = 0
max = 0
suma = 0
i=0

while liczba != 0:
    liczba = float(input(f"Podaj liczbe: "))
    if liczba == 0:
        break

    if(min==0 and max==0):
        min = liczba
        max = liczba
    else:

        if liczba <= min:
            min = liczba
        if liczba >= max:
            max = liczba

    suma += liczba
    i+=1

srednia = suma/i
print(f"Minimalna= {min}, Maksymalna= {max}, Srednia= {srednia}")
