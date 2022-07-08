# Anagramy


def is_anagram(napis1, napis2, liczba_znakow1, liczba_znakow2):
    lista1 = []
    lista2 = []
    if liczba_znakow2 == liczba_znakow1:
        for i in range(liczba_znakow1):
            lista1.append(napis1[i])
            lista2.append(napis2[i])
        for y in lista2:
            if y in lista1:
                lista1.remove(y)
                if lista1 == []:
                    print("Slowa sa anagramami")
        if lista1 != []:
            print("Slowa nie sa anagramami")
    else:
        print("Slowa nie sa anagramami")


napis1 = input("Podaj napis: ")
napis2 = input("Podaj napis: ")
liczba_znakow1 = len(napis1)
liczba_znakow2 = len(napis2)
is_anagram(napis1, napis2, liczba_znakow1, liczba_znakow2)
