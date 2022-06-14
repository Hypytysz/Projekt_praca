#wybor najwiekszej liczby sposrod 3 zmiennych
liczba1 = float(input((f"Podaj pierwsza liczbe: ")))
liczba2 = float(input((f"Podaj druga liczbe: ")))
liczba3 = float(input((f"Podaj trzecia liczbe: ")))
if liczba1>liczba2 and liczba1>liczba3:
    print(f"Liczba {liczba1} jest wieksza od {liczba2} oraz od {liczba3}")
elif liczba2>liczba1 and liczba2>liczba3:
    print(f"liczba {liczba2} jest wieksza od {liczba1} oraz od {liczba3}")
else:
    print(f"liczba {liczba3} jest wieksza od {liczba1} oraz od {liczba2}")
