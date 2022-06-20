# Kalkulator
from tkinter import *
wyrazenie = ""
def press(num):
    global wyrazenie
    wyrazenie += str(num)
    rownanie.set(wyrazenie)
def wynik():
    global wyrazenie
    wynik = str(eval(wyrazenie))
    wynikdzialania.set(wynik)

def wyczysc():
    global wyrazenie
    wyrazenie = ""
    rownanie.set("")
root = Tk()

root.title("Kalkulator")
root.geometry("265x390")
rownanie = StringVar()
wynikdzialania = StringVar()
ramkaGorna = Frame(root)
ramkaSrodkowa = Frame(root)
ramkaDolna = Frame(root, pady=10)



ramkaSrodkowa.grid(row=1,column=0, sticky=W)
ramkaDolna.grid(row=2, column=0, pady=10)
#Ramka Gorna
wyrazenie_pole = Entry(textvariable=rownanie,font=('arial', 18, 'bold'), width=20, bg="grey", bd=0, justify=RIGHT)
wyrazenie_pole.grid(row=-0, column=0)
#Ramka Srodkowa
wynik_pole = Entry(textvariable=wynikdzialania, font=('arial', 18, 'bold'), width=20, justify=RIGHT)

wynik_pole.grid(row=1, column=0)
#Ramka Dolna
button_7 = Button(ramkaDolna, text="7", height=3, width=5, command=lambda: press(7))
button_8 = Button(ramkaDolna, text="8", height=3, width=5, command=lambda: press(8))
button_9 = Button(ramkaDolna, text="9", height=3, width=5, command=lambda: press(9))
button_razy = Button(ramkaDolna, text="*", height=3, width=5, command=lambda: press("*"))
button_4 = Button(ramkaDolna, text="4", height=3, width=5, command=lambda: press(4))
button_5 = Button(ramkaDolna, text="5", height=3, width=5, command=lambda: press(5))
button_6 = Button(ramkaDolna, text="6", height=3, width=5, command=lambda: press(6))
button_minus = Button(ramkaDolna, text="-", height=3, width=5, command=lambda: press("-"))
button_1 = Button(ramkaDolna, text="1", height=3, width=5, command=lambda: press(1))
button_2 = Button(ramkaDolna, text="2", height=3, width=5, command=lambda: press(2))
button_3 = Button(ramkaDolna, text="3", height=3, width=5, command=lambda: press(3))
button_dodac = Button(ramkaDolna, text="+", height=3, width=5, command=lambda: press("+"))
button_0 = Button(ramkaDolna, text="0", height=3, width=5, command=lambda: press(0))
button_rowne = Button(ramkaDolna, text="=", height=3, width=12, command=wynik)
button_r = Button(ramkaDolna, text="R", height=3, width=5, command=wyczysc)

button_7.grid(row=2, pady=7, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_razy.grid(row=2, column=3)
button_4.grid(row=3, pady=7, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_minus.grid(row=3, column=3)
button_1.grid(row=4, pady=7,  column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_dodac.grid(row=4, column=3)
button_0.grid(row=5, pady=7, column=0)
button_rowne.grid(row=5, column=1, columnspan=2)
button_r.grid(row=5, column=3)



root.mainloop()
