# Asystent informujący głosowo o harmonogramie pracy
from datetime import datetime
import playsound
from gtts import gTTS
import os

def valid():
    plik = open("asystent.txt", "r", encoding="utf-8")
    lista_x0 = []
    lista_x1 = []
    for i in plik:
        x = i.split(";")
        lista_x0.append(x[0])
        lista_x1.append(x[1])
    plik.close()
    lista_x0.pop(0)
    lista_x1.pop(-1)
    if lista_x0 == lista_x1:
        print("Your schedule is ok!")
    else:
        print("Times in your schedule must be upgrade! It's not match together!")

def powiadomienie():
    run = True
    while run == True:
        plik = open("asystent.txt", "r", encoding="utf-8")
        for i in plik:
            x = i.split(";")
            time = datetime.now().time().strftime("%H:%M:%S")
            if time == x[0]:
                napis = x[2]
                tts = gTTS(f'{napis}')
                tts.save('voice.mp3')
                playsound.playsound("voice.mp3")
                os.remove("voice.mp3")
                continue
            elif time == "21:01:00":
                tts = gTTS("the end")
                tts.save('end.mp3')
                playsound.playsound("end.mp3")
                run = False
                break
        plik.close()

valid()
powiadomienie()
