This is a little project to handles appointments from user to a simple machine in python
We can wake the machine by keywords, create an appointment by speaking to it

The machine can retrieve appointments by email or text message if the user is not at home, 
and speak out the appointments when user come back.


sources from this project is : 

**for STT / Speech to text**
speech_recognition library, used to translate speech to text
snowboy, for custom hotword detection
pyAudio, used to allow the app to use microphone.

**for TTS / Text to speech**
gTTS, used to translate text from machine to speech
