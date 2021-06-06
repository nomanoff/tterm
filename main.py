import speech_recognition as sr
import webbrowser
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.AudioFile('./voice_commands/time.wav') as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
           
        except sr.UnknownValueError:
            print("Sorry, I don't get that")
        except sr.RequestError:
            print("Sorry, the service is down")
        return voice_data


def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is Friday')

    if 'what time is it' in voice_data:
        print(ctime())
    
    if 'what are you' in voice_data:
        print('I am AI bot')   
    
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print("Here is what I've found for " + search)
    

print('How can I help you?')
voice_data = record_audio()
respond(voice_data)


