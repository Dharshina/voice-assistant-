import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import time
from time import ctime
import re
import webbrowser
import smtplib
import python_weather


def textToSpeech(text_in_english):
    print(text_in_english)
    tts = gTTS(text = text_in_english, lang = "ta")
    tts.save("textToSpeech.mp3")
    playsound.playsound("textToSpeech.mp3")
    os.remove("textToSpeech.mp3")



def listen():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hm..!! I am listening")
        audio = input.listen(source, phrase_time_limit = 5)
    data = ""
    try:
        data=input.recognize_google(audio,language='ta')
        print("You said "+data)
    except sr.UnknownValueError:
        print("You said "+data)
    except sr.RequestError as e:
        print("Request Failed")
    return data.lower()

def processVoiceReply(data):
    if "how are you" in data:
        listening = True
        textToSpeech("I'm good Thankyou")
    if "time" in data:
        listening = True
        current_time = time.strftime("%H:%M:%S")
        textToSpeech("the time is now " +current_time)
    if "temperature" in data:
        listening = True
        current_time = time.strftime("%H:%M:%S")
        print("The current time is", current_time)
        textToSpeech("the time is now " +current_time)
    if "stop" in data:
        listening = False
        textToSpeech("See you again")
    return listening

time.sleep(1)

#textToSpeech("வைரமுத்து ரிசிகர் சிந்து")
#textToSpeech("வணக்கம் வெங்கி")
#textToSpeech("சுஷி செல்சு")
#textToSpeech("செல்சு")
#textToSpeech("கார்த்தி")
#textToSpeech("நம்ஷா")
#textToSpeech("எல்லாரும் என்னா பண்றீங்க")
#textToSpeech("யென் சிரிக்ரீங்கா")
#textToSpeech("எல்லாரும் நல்லா தூங்குங்க")
#textToSpeech("Hey there!")
textToSpeech("என் பசப்புக்கள்ளி என் பசப்புக்கள்ளி அவ தந்துப்புட்டா இவன் மனச அள்ளி என் எருக்கஞ்சுள்ளி என் எருக்கஞ்சுள்ளி அவ பத்த வச்சா இவன் நெனப்ப கிள்ளி")
listening = True
while listening == True:
    data = listen()
    listening = processVoiceReply(data)
