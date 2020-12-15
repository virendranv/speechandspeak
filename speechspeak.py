import pyttsx3
import pyaudio
speaker=pyttsx3.init()
speaker.say("  really i missed you ")
speaker.runAndWait()
import speech_recognition as sr
mic=sr.Microphone()
r=sr.Recognizer()
with mic as source:
 print("say:")
 audio=r.listen(source)
 text=r.recognize_google(audio)
 print(text)
 speaker.say(text)
 speaker.runAndWait()
