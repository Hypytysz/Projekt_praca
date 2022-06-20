# Po wpisaniu 15 liczb program oblicza sumę tylko liczb parzystych
suma = 0
for i in range(15):
    liczba = int(input(f"Podaj liczbe "))
    if(liczba%2==0):
        suma = suma + liczba
print(suma)
