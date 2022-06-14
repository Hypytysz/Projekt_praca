# Suma dwoch liczb podanych slownie
slownie = {1: "jeden", 2:"dwa", 3: "trzy", 4: "cztery", 5:"piec"}
cyfrowo = {"jeden":1,"dwa":2,"trzy":3,"cztery":4, "piec":5}

cyfra1 = (input(f"Wprowadz pierwsza liczbe:")) # trzy
cyfra2 = (input(f"Wprowadz druga liczbe:")) # dwa

suma = cyfrowo[cyfra1] + cyfrowo[cyfra2]
print(f"Suma tych dwoch liczb to {suma}")
