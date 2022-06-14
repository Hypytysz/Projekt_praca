# dowolna liczba 4 cufrowa na interpretacje slowna
slownie = {"1": "jeden", "2":"dwa", "3": "trzy","4": "cztery", "5":"piec", "6":"szesc", "7": "siedem", "8":"osiem", "9":"dziewiec"}
liczba1 = str(input(f"Podaj dowolna liczbe"))
cyfra1 = liczba1[0]
cyfra2 = liczba1[1]
cyfra3 = liczba1[2]
cyfra4 = liczba1[3]
print(slownie[cyfra1],slownie[cyfra2],slownie[cyfra3],slownie[cyfra4])
