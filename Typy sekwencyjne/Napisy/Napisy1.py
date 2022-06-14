#Program zliczający znaki oraz spacje w inpucie
znaki=(input(f"Podaj zdanie jakie chcesz zliczyc: "))
znaki_bezspacji = len(znaki.replace(" ", ""))
print(f"Liczba znaków to (I): {znaki_bezspacji} Liczba spacji to (II): "+str((len(znaki)) - len(znaki.replace(" ", ""))))
