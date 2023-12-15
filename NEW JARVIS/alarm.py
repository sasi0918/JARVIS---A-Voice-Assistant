import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

with open("Alarmtext.txt", "r") as extracted_time_file:
    time = extracted_time_file.read()

def ring(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H %M %S")
        if current_time == alarm_time:
            speak("Alarm ringing, sir")
            os.startfile("D:\downloded music\Beast Mode.mp3")
            break

ring(time)

