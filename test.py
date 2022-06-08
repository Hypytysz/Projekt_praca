#Kolko i krzyzyk

gra = [ ["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"] ]
ruchy = 9
zawodnik = "O"
zawodnik2 = "X"
zawodnik3 = "O"
while ruchy!= 0:
    ruchy -= 1
    for x in gra:
        for y in x:
            print(y, end=" ")

        print()
    wsp = input(f"Zawodnik '{zawodnik}' podaj wsplorzedne: ") # "12"
    wspY = int(wsp[0]) #"1"
    wspX = int(wsp[1]) #"2"
    if gra[wspY][wspX] == zawodnik2:
        print("Pole jest zajete! Tracisz ture :(")
        ruchy+=1
    if gra[wspY][wspX] == zawodnik3:
        print("Pole jest zajete! Tracisz ture :(")
        ruchy+=1
    elif gra[wspY][wspX] != zawodnik2 and gra[wspY][wspX] != zawodnik3:
        gra[wspY][wspX] = zawodnik

    # if(gra[0][0] == gra[1][1]) and (gra[1][1] == gra[2][2]) and (gra[0][0] != "*"):
    # if(gra[0][0] == "O" and gra[1][1] == "O" and gra[2][2] == "O") or (gra[0][0] == "X" and gra[1][1] == "X" and gra[2][2] == "X"):

    if(gra[0][0] == zawodnik and gra[1][1] == zawodnik and gra[2][2] == zawodnik):
        odp =input(f"Wygral zawodnik {zawodnik}! Chcesz zagrac jeszcze raz? T/N")
        if odp == "T":
            gra = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
            ruchy = 9
        elif odp == "N":
            break
        else:
            print(f"Ups cos poszlo nie tak :(")
    elif(gra[0][0] == zawodnik and gra[1][0] == zawodnik and gra[2][0] == zawodnik):
        odp =input(f"Wygral zawodnik {zawodnik}! Chcesz zagrac jeszcze raz? T/N")
        if odp == "T":
            gra = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
            ruchy = 9
        elif odp == "N":
            break
        else:
            print(f"Ups cos poszlo nie tak :(")
    elif(gra[0][0] == zawodnik and gra[0][1] == zawodnik and gra[0][2] == zawodnik):
        odp =input(f"Wygral zawodnik {zawodnik}! Chcesz zagrac jeszcze raz? T/N")
        if odp == "T":
            gra = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
            ruchy = 9
        elif odp == "N":
            break
        else:
            print(f"Ups cos poszlo nie tak :(")
    elif (gra[0][1] == zawodnik and gra[1][1] == zawodnik and gra[2][1] == zawodnik):
        odp =input(f"Wygral zawodnik {zawodnik}! Chcesz zagrac jeszcze raz? T/N")
        if odp == "T":
            gra = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
            ruchy = 9
        elif odp == "N":
            break
        else:
            print(f"Ups cos poszlo nie tak :(")
    elif (gra[0][2] == zawodnik and gra[1][2] == zawodnik and gra[2][2] == zawodnik):
        odp =input(f"Wygral zawodnik {zawodnik}! Chcesz zagrac jeszcze raz? T/N")
        if odp == "T":
            gra = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
            ruchy = 9
        elif odp == "N":
            break
        else:
            print(f"Ups cos poszlo nie tak :(")
    elif (gra[1][0] == zawodnik and gra[1][1] == zawodnik and gra[1][2] == zawodnik):
        odp =input(f"Wygral zawodnik {zawodnik}! Chcesz zagrac jeszcze raz? T/N")
        if odp == "T":
            gra = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
            ruchy = 9
        elif odp == "N":
            break
        else:
            print(f"Ups cos poszlo nie tak :(")
    elif (gra[2][0] == zawodnik and gra[2][1] == zawodnik and gra[2][2] == zawodnik):
        odp =input(f"Wygral zawodnik {zawodnik}! Chcesz zagrac jeszcze raz? T/N")
        if odp == "T":
            gra = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
            ruchy = 9
        elif odp == "N":
            break
        else:
            print(f"Ups cos poszlo nie tak :(")
    elif (gra[0][2] == zawodnik and gra[1][1] == zawodnik and gra[2][0] == zawodnik):
        odp =input(f"Wygral zawodnik {zawodnik}! Chcesz zagrac jeszcze raz? T/N")
        if odp == "T":
            gra = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
            ruchy = 9
        elif odp == "N":
            break
        else:
            print(f"Ups cos poszlo nie tak :(")
    if ruchy == 0:
        print("Mamy remis!")
        break

    #zamiana zawodnikow

    if(zawodnik == "O"):
        zawodnik = "X"
    else:
        zawodnik = "O"
