import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


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

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done,Boss")

import wikipedia

def searchWikipedia(query):
    try:
        # Attempt to get a summary from Wikipedia
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia..")
        print(results)
        speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        # If the query is ambiguous, provide options to the user
        options = e.options
        speak("I found multiple topics related to your query. Please choose one:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
            speak(f"{i}. {option}")
        
        # Wait for user input to choose a specific topic
        user_choice = int(input("Enter the number corresponding to your choice: "))
        if 1 <= user_choice <= len(options):
            chosen_topic = options[user_choice - 1]
            # Recur with the specific topic
            searchWikipedia(chosen_topic)
        else:
            speak("Invalid choice. Please try again.")
