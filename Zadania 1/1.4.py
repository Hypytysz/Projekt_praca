try:
    def double_letters(napis):
        liczba_cyfr = len(napis)
        for i in range(liczba_cyfr):
            if napis[i] == napis[i+1]:
                print(f"W napisie sasiaduja ze soba litery: {napis[i]}")


    napis = input("Podaj napis: ")
    double_letters(napis)
except IndexError:
        pass