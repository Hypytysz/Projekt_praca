# Czy zdanie jest pangramem?
# -*- coding: utf-8 -*-


def is_pangram(x, i2):
    for y in i2:
        y = y.lower()
        if y in x:
            x.pop(x.index(y))
    if len(x) == 0:
        print("Zdanie jest pangramem.")
    else:
        print("Zdanie nie jest pangramem.")


i = (input("Podaj wyrazenie: "))
i2 = ("".join(i.split()))
x = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o",
        "ó", "p", "r", "s", "ś", "t", "u", "w", "y", "z", "ź", "ż"]
is_pangram(x, i2)
