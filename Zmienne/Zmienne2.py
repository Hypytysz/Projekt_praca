#Porgram liczący liczbę spacji w inpucie
znaki=(input(f"Podaj zdanie jakie chcesz zliczyc: "))
print("Liczba spacji to (II): "+str((len(znaki)) - len(znaki.replace(" ", ""))))
