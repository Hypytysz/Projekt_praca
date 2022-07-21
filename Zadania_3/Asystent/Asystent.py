# Asystent informujący głosowo o harmonogramie pracy
from datetime import datetime
import playsound
from gtts import gTTS
import os


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

powiadomienie()
