# Min, Max, parzyste, nieparzyste, srednia
import random
def cwiczenie(dane):
    ilosc = len(dane)
    srednia = 0
    min = dane[0]
    max = dane[0]
    parzyste = []
    nieparzyste = []
    suma = 0

    for i in dane:
        if i > max:
            max = i
        if i < min:
            min = i

        if i % 2 == 0:
            parzyste.append(i)
        else:
            nieparzyste.append(i)

        suma = suma + i

        srednia = suma/ilosc

    return len(parzyste), len(nieparzyste), srednia, min, max


lista = []
for i in range (10):
    los = random.randint(1,100)
    lista.append(los)
print(lista)

odp = cwiczenie(lista)
print(odp)
