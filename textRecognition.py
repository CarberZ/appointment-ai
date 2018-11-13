import speech_recognition as sr  # Speech to text recognition
from gtts import gTTS   # Text to speech
from time import ctime
import time
import os
'''
imports for snowboy
'''
import snowboydecoder
import sys
import signal


r = sr.Recognizer()

# get a list of all mics available on device
allMics = sr.Microphone.list_microphone_names()

# some initializers
blue_snowBall = 0
duration = 0.5  # this is used to calibrate mic if room is noisy

# get index from micList
for i, item in enumerate(allMics):
    if "Snowball" in item:
        blue_snowBall = i
        break

# set mic just found
mic = sr.Microphone(blue_snowBall)

# records stops automaticly when silent is detected

def record_audio():
    # Record Audio
    with mic as source:
        print('Cloé listen')
        # r.adjust_for_ambient_noise(source, .5) // if needed for noisy room
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
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


def cloe(audioSource):
    if "comment ça va" in audioSource:
        speak("ça va bien.")

    if "quelle heure est-il" in audioSource:
        speak('il est ' + time.strftime('%-H') + ' heure ' + time.strftime('%M'))

    if "quel micro utilises-tu" in audioSource:
        if "Snowball" in allMics[blue_snowBall]:
            speak("J'utilise le Blue Snowball microphone.")
        else:
            speak("Je ne sais pas quel microphone j'utilise.")


'''
SNOWBOY ENGINE
'''
interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

model = 'Cloé.pmdl'

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=snowboydecoder.play_audio_file,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
