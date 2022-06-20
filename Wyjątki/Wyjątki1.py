# Try
while(True):

    while(True):
        try:
            liczba1 = int(input("Podaj liczbe 1: "))
        except ValueError:
            print("Wprowadzamy tylko liczby")
        except:
            print("Nieoczekiwany blad, prosi")
        else:
            break

    while (True):
        try:
            liczba2 = int(input("Podaj liczbe 2: "))
        except ValueError:
            print("Wprowadzamy tylko liczby")
        else:
            break

    try:
        wynik = liczba1 / liczba2
        print(wynik)
    except ZeroDivisionError:
        print("Nie dziel przez 0 !!!")
