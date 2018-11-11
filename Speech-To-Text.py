import speech_recognition as sr

r = sr.Recognizer()

# get a list of all mics available on device
allMics = sr.Microphone.list_microphone_names()

# some initializers
blue_snowBall = 0
duration = 0.5
language = 'fr-FR'

# get index from micList
for i, item in enumerate(allMics):
    if "Snowball" in item:
        blue_snowBall = i
        break

# set mic just found

mic = sr.Microphone(blue_snowBall)

# this is an optional arument for the duration of the record task

# this is how audio is catched from a recorded wave file
'''
bl = sr.AudioFile('bodyLanguage.wav')
with bl as source:
    # if there is noise , calibrate and record
    r.adjust_for_ambient_noise(source, duration)
    audio = r.record(source)
'''

# we can do the same with mic, records stops automaticly when silent is detected
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

type(audio)

r.recognize_google(audio, language)

