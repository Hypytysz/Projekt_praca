# Program liczacy sume podanych liczb oraz srednia
liczby = []
liczby.append(float(input("Podaj pierwsza liczbe:")))
liczby.append(float(input("Podaj druga liczbe:")))
liczby.append(float(input("Podaj trzecia liczbe:")))
liczby.append(float(input("Podaj czwarta liczbe:")))
liczby.append(float(input("Podaj piata liczbe:")))

suma = liczby[0]+liczby[1]+liczby[2]+liczby[3]+liczby[4]
print(f"Suma wszystkich liczb to:{suma}")
srednia1 = suma/5
print(f"Srednia wszystkich liczb to:{srednia1}")
