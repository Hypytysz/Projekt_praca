# Program liczacy BMI
waga = int(input((f"Podaj wage w kg: ")))
wzrost = float(input((f"Podaj wzrost w metrach: ")))

wzor = waga/(wzrost**2)

if wzor < 18.5:
    print(f"Masz niedowage")
elif wzor > 24.9:
    print(f"Masz nadwage")
else:
    print(f"waga prawidlowa")
