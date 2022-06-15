# Pętla dodająca tylko niepowtarzalne liczby
lista = []
lista2 = []

for i in range(10):
    lista.append(int(input(f"Podaj liczbe: ")))
    x = lista.count(lista[i])
    if x > 1 and lista[i] in lista2:
        lista2.remove(lista[i])
    if lista[i] not in lista2:
        lista2.append(lista[i])
    if x >= 2 and lista[i] in lista2:
        lista2.remove(lista[i])




print(lista2)
