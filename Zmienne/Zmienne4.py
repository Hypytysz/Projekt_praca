#Paragon podsumowujacy wybrane zakupy
chleb = float(6.50)
sok = float(4.00)
paczek = float (5.50)
ilosc_chleba = float(input(f"Ile bochenkow chleba chcesz zamowic?"))
ilosc_soku = float(input(f"Ile kartonow soku chcesz zamowic?"))
ilosc_paczek = float(input(f"Ile paczkow chcesz zamowic?"))
cena_chleba = float(chleb*ilosc_chleba)
cena_soku = float(sok*ilosc_soku)
cena_paczka = float(paczek*ilosc_paczek)
print(f"Zamowienie {ilosc_chleba} bochenkow chleba {cena_chleba} zl\n{ilosc_soku} kartonow soku {cena_soku}zl \noraz {ilosc_paczek} paczkow {cena_paczka} zl")

suma = float(cena_chleba+cena_soku+cena_paczka)
print(f"Calkowita kwota do zaplaty {suma} zl")
