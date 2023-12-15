import pyttsx3
import speech_recognition 
import requests

from  bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import openai
import webbrowser
from pygame import mixer
import speedtest
from game import game_play
import ctypes
from pynput.keyboard import Key, Controller
keyboard = Controller()

for i in range(3):
    a = input("Enter Password to open Jarvis: ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read().strip() 
    pw_file.close()
    if a == pw:
        print("WELCOME SIR")
        break
    elif i == 2 and a != pw:
        exit()
    else:
        print("Try Again")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",100)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
    
if __name__ == "__main__":
    alarm_mode = False
    while True:
        query = takeCommand().lower()
        if "jarvis" in query:
            from GreetMe import greetMe
            greetMe()
        
            while True:
                query = takeCommand().lower()
                if "hold on" in query:
                    speak("Ok Boss ,You can call me anytime")
                    break 
                
                elif "change password" in query:
                    speak("What's the new password?")
                    new_pw = input("Enter the new password: ")
                    new_password_file = open("password.txt", "w")
                    new_password_file.write(new_pw.strip()) 
                    new_password_file.close()
                    speak("Done BOSS ! ,.")
                    speak(f"Your new password is {new_pw}") 
                            
                
                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()
                    

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)
                
                    
                elif "open" in query:  
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")  
                    
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576        
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi Upload speed is {upload_net}") 
                    speak(f"Wifi download speed is {download_net}")
                
                elif "set an alarm" in query:
                    alarm_mode = True  
                    speak("Please set the time for the alarm.")
                    alarm_time = input("Please tell the time in the format HH MM SS: ").strip()
                    with open("Alarmtext.txt", "w") as alarm_file:
                       alarm_file.write(alarm_time)
                    
                                   
                elif "game" in query:
                    from game import game_play
                    game_play()

                elif "screenshot" in query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                           
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                elif "how are you" in query:
                    speak("Perfect,Boss")                    

                elif "who are you" in query:
                    speak("MY NAME IS JARVIS , IAM A PROGRAMMING VOICE ASSISTANT ")  
                elif "created you" in query:
                    speak("Mr SASIDHAR")    
                elif "hello" in query:
                    speak("Hello Boss, how are you ?")
                elif "thanks" in query:
                    speak("DO YOU WANT TO KNOW ANYTHING MORE!!")
                elif "wait" in query:
                    speak("OK BOSS")   
                elif "i am fine" in query:
                    speak("that's great,Boss")

                    
                elif "thank" in query:
                    speak("you are welcome,Boss")
                    
                elif "play songs" in query:
                    from myFavSongs import links
                    speak("Playing your favorite songs, Boss")
                    links()  
                    
                elif "change" in query: 
                    from myFavSongs import youtubelinks 
                    youtubelinks()              
                                
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                     pyautogui.press("k")
                     speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                    
                elif "increase volume" in query:
                    from keyboard import volumeup
                    speak("Turning volume up")
                    volumeup()
                    
                elif "decrease volume" in query:
                   from keyboard import volumedown
                   speak("Turning volume down")
                   volumedown()
                   
                elif "increase brightness" in query:
                    from keyboard import increase_brightness
                    speak("Increasing brightness")
                    increase_brightness()
                
                elif "decrease brightness" in query:
                    from keyboard import decrease_brightness
                    speak("Decrease brightness")
                    decrease_brightness()
                   
                elif "home" in query:
                    keyboard.press(Key.cmd)
                    keyboard.press('d') 
                    keyboard.release('d') 
                    keyboard.release(Key.cmd) 
                    speak("Showing desktop")

                elif "to work" in query:
                    keyboard.press(Key.cmd) 
                    keyboard.press('d')  
                    keyboard.release('d') 
                    keyboard.release(Key.cmd) 
                    speak("SURE ,BOSS")
    
                elif "open" in query:
                  from Dictapp import openappweb
                  openappweb(query)
                  
                elif "close" in query:
                  from Dictapp import closeappweb
                  closeappweb(query)
                     
                elif " google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                    
                elif "in youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                    
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()    
                
                    
                elif "calculate" in query:
                    from Calculatenumbers import Calc
                    query = query.replace("calculate", "")
                    query = query.replace("jarvis", "")
                    Calc(query)

                elif "whatsapp" in query:
                     from Whatsapp import sendMessage
                     sendMessage()
 
                elif "alarm" in query:
                        print("input time example:- 10 and 10 and 10")
                        speak("Set the time")
                        a = input("Please tell the time :- ")
                        alarm(a)
                        speak("Done,BOSS")
                        
                 elif "what is " in query:
                    from OpenAIFile import get_openai_info
                    get_openai_info()
                        
                elif " time" in query:
                    strTime = datetime.datetime.now().strftime("%I:%M %p")    
                    speak(f" BOSS , the time is {strTime}")
                    
                    
                elif " system" in query:
                    speak("Are you sure you want to shutdown?")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown.lower() == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown.lower() == "no":
                        speak("Shutdown operation aborted.")
      
                elif "shutdown" in query:
                      speak("OK BOSS, SHUTTING DOWN ! ")
                      exit()
                  
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "").strip()
                    rememberMessage = rememberMessage.replace("jarvis", "").strip()
                    speak("You told me to remember that " + rememberMessage)
                    with open("Remember.txt", "a") as remember:
                        remember.write(rememberMessage + "\n")

                elif "what do you remember" in query:
                    with open("Remember.txt", "r") as remember:
                        memories = remember.read()
                    if memories:
                        speak("You told me that: " + memories)
                    else:
                        speak("I don't have any specific memories to recall.")

                elif "temperature" in query:
                    from weather import get_weather
                    API_KEY = 'ba202f459e9f42a4b5830894f8a98e82'  
                    speak("LET ME KNOW WHAT's  THE LOCATION is ")
                    city = takeCommand().lower()
                    weather_info = get_weather(API_KEY, city)
                    speak(weather_info)
                    
                elif "weather" in query:
                    from weather import get_weather
                    API_KEY = 'ba202f459e9f42a4b5830894f8a98e82' 
                    speak("ENTER THE NAME OF THE CITY")
                    print("Please enter the city name ")
                    city = takeCommand().lower()
                    weather_info = get_weather(API_KEY, city)
                    speak(weather_info)
                    
                elif"music" in query:
                    from music import play_music
                    speak("playing music")
                    play_music()    


