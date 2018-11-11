import speech_recognition as sr  # Speech to text recognition
from gtts import gTTS   # Text to speech
from time import ctime
import time
import os

r = sr.Recognizer()

# get a list of all mics available on device
allMics = sr.Microphone.list_microphone_names()

# some initializers
blue_snowBall = 0
duration = 0.5  # this is an optional argument for the duration of the record task

# get index from micList
for i, item in enumerate(allMics):
    if "Snowball" in item:
        blue_snowBall = i
        break

# set mic just found

mic = sr.Microphone(blue_snowBall)

# this is how audio is catched from a recorded wave file
'''
bl = sr.AudioFile('bodyLanguage.wav')
with bl as source:
    # if there is noise , calibrate and record
    r.adjust_for_ambient_noise(source, duration)
    audio = r.record(source)
'''

# we can do the same with mic, records stops automaticly when silent is detected


def record_audio():
    # Record Audio
    with mic as source:
        print('i listen')
        r.adjust_for_ambient_noise(source, .5)
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio, language='fr-FR')
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def speak(audiostring):
    print(audiostring)
    tts = gTTS(audiostring, 'fr')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")


def jarvis(data):
    if "comment ça va" in data:
        speak("ça va bien.")

    if "quelle heure est-il" in data:
        speak('il est ' + time.strftime('%-H') + ' heure ' + time.strftime('%M'))

    if "what microphone are you using" in data:
        if "Snowball" in allMics[blue_snowBall]:
            speak("I am using the Blue Snowball microphone.")
        else:
            speak("i don't know what microphone i use.")

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")


# process
time.sleep(2)
speak("Salut, qu'est-ce que je peux faire pour toi ?")
while 1:
    data = record_audio()
    jarvis(data)

