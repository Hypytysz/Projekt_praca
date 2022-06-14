# Gra do nauki tabliczki mnozenia
import random
zm1 = int(random.randint(1, 9))
zm2 = int(random.randint(1, 9))
znak = random.randint(1,3)
wynik1 = int(zm1*zm2)
wynik2 = int(zm1-zm2)
wynik3 = int(zm1+zm2)

if znak == 1:
   wyniku = int(input(f"Jaki jest wynik dzialania: {zm1} x {zm2}?"))
   if wyniku == wynik1:
       print(f"BRAWO! Odpowiedz jest prawidlowa!")
   else:
       print(f"NIESTETY! Odpowiedz to {wynik1}")
if znak == 2:
   wyniku = int(input(f"Jaki jest wynik dzialania: {zm1} - {zm2}?"))
   if wyniku == wynik2:
       print(f"BRAWO! Odpowiedz jest prawidlowa!")
   else:
       print(f"NIESTETY! Odpowiedz to {wynik2}")
if znak == 3:
    wyniku = int(input(f"Jaki jest wynik dzialania: {zm1} + {zm2}?"))
    if wyniku == wynik3:
        print(f"BRAWO! Odpowiedz jest prawidlowa!")
    else:
        print(f"NIESTETY! Odpowiedz to {wynik3}")
