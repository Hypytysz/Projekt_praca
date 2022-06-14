# Wypisz wartości zmiennych od najmniejszej do największej
liczba1 = float(input((f"Podaj pierwsza liczbe: ")))
liczba2 = float(input((f"Podaj druga liczbe: ")))
liczba3 = float(input((f"Podaj trzecia liczbe: ")))
if liczba1>liczba2 and liczba1>liczba3 and liczba2>liczba3:
    print(f"Liczba {liczba1} jest wieksza od {liczba2}, ktora natomiast jest wieksza od {liczba3}")
elif liczba1>liczba2 and liczba1>liczba3 and liczba3>liczba2:
    print(f"Liczba {liczba1} jest wieksza od {liczba3}, ktora natomiast jest wieksza od {liczba2}")
elif liczba2>liczba1 and liczba2>liczba3 and liczba1>liczba3 :
    print(f"liczba {liczba2} jest wieksza od {liczba1}, ktora natomiast jest wieksza od {liczba3}")
elif liczba2 > liczba1 and liczba2 > liczba3 and liczba3 > liczba1:
    print(f"liczba {liczba2} jest wieksza od {liczba3}, ktora natomiast jest wieksza od {liczba1}")
elif liczba3 > liczba1 and liczba3 > liczba2 and liczba1>liczba2:
    print(f"liczba {liczba3} jest wieksza od {liczba1}, ktora natomiast jest wieksza od {liczba2}")
else:
    print(f"liczba {liczba3} jest wieksza od {liczba2}, ktora natomiast jest wieksza od {liczba1}")
