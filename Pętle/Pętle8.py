# 10 losowych działań z wynikami
import random

poprawne = 0
niepoprawne = 0
x=10
while x > 0:
    zm1 = int(random.randint(1, 10))
    zm2 = int(random.randint(1, 10))
    zm3 = (random.randint(1, 3))
    if zm3 == 1:
        x-=1
        y = int(input((f"Jaki jest wynik dodawania {zm1} + {zm2}? ")))
        wynik = zm1 + zm2
        if wynik == y:
            poprawne += 1
            print(f"Tak wynik to {y}!")
        if wynik != y:
            niepoprawne += 1
            print(f"Niestety wynik to {wynik}")
    if zm3 == 2:
        x-=1
        y = int(input((f"Jaki jest wynik odejmowania {zm1} - {zm2}? ")))
        wynik = zm1 - zm2
        if wynik == y:
            poprawne += 1
            print(f"Tak wynik to {y}!")
        if wynik != y:
            niepoprawne += 1
            print(f"Niestety wynik to {wynik}")
    if zm3 == 3:
        x-=1
        y = int(input((f"Jaki jest wynik mnozenia {zm1} * {zm2}? ")))
        wynik = zm1 * zm2
        if wynik == y:
            poprawne += 1
            print(f"Tak wynik to {y}!")
        if wynik != y:
            niepoprawne += 1
            print(f"Niestety wynik to {wynik}")
    if x == 0:
        print(f"Suma poprawnych odpowiedzi:{poprawne} \nSuma niepoprawnych odpowiedzi: {niepoprawne}")
