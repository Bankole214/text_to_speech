import speech_recognition as sr
import webbrowser
import time
import playsound   
import os       #operating sys create an audio file 
import random    #randomly gennerate audio name for the files
from gtts import gTTS
from time import ctime



r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            dimsey_speak(ask)
        
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  
            # dimsey_speak(voice_data)
        except sr.UnknownValueError:
            dimsey_speak('sorry would you like to repeat?  Please')
        except sr.RequestError:
            dimsey_speak('Sorry my speech  is down')
        return voice_data


def dimsey_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + 'mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def response(voice_data):
    if 'what is your name' in voice_data:   #  PROMPT NAME
        dimsey_speak(f'My name is DAN')


    if 'what time is it' in voice_data or 'what is the time' in voice_data:   # PROMPT TIME
        dimsey_speak(f' the time is {ctime()}')


    if 'search' in voice_data:     # PROMPT FOR SEARCH/FIND/KEYWORDS 
        search = record_audio('what do you want to search for?')
        url = 'http://google.com/search?q=' + search
        webbrowser.get().open(url)
        dimsey_speak ('Here is what i found for' + search)


    if 'find location' in voice_data:   # SEARCH FOR location
        location = record_audio('What is the location?')
        url = 'http://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        dimsey_speak ('Here is the location of' + location)

    if 'exit' in voice_data:    # Exit the voice data loop
        exit()

time.sleep(1)       #CONTINUE THE LOOP AFTER THE PROMPTING...WE IMPORT A MODULE CALLED TIME TO DELAY IT BY A SECOND
dimsey_speak('How can i help you?')
while 1:
    voice_data = record_audio()


    response(voice_data)




# pip installed objc 
# pip installed gTTS
# pip installed playsounnd but i had to install manually by going to the github and downloading the file then moved it to the project directory the activated my venv then ran this commND pip install --upgrade setuptools FOLLOWED BY python setup.py install 
