# Pętla witająca się z 10 użytkownikami
lista = []
for i in range(10):
    lista.append(input(f"Dodaj imie do listy "))
for i in range(len(lista)):
    print(f"Cześć {lista[i]}!")
