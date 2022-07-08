# Czy napis jest palindromem


def is_palindrom(mapis):
    return napis == napis[::-1]


napis = input("Podaj slowo: ")
x = is_palindrom(napis)
print(x)