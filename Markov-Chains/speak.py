import txt
from gtts import gTTS
import os

def speak():
    n = open("./output.txt", "r")
    myText = n.read().replace("\n", " ")

    # Language we want to use
    language = 'en'

    output = gTTS(text=myText, lang=language, slow=False)

    output.save("output.mp3")
    n.close()

    #mp3 file
    os.system("start output.mp3")
    print("Done playing.")
   
#would print out an mp3 file that is the spoken version of the txt file that was outputted from txt.py
speak()
