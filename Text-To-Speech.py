from gtts import gTTS
tts = gTTS('hello')  # optional second parameter is language
tts.save('example.mp3')
