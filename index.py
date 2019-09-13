from gtts import gTTS
import os

myText="Text to speech conversion using python"

language='en'

ouput=gTTS(text=myText,lang=language,slow=False)

ouput.save("output.mp3")

#os.system('start output.mp3')