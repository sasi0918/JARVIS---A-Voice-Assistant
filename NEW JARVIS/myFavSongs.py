import random
import pyttsx3
import webbrowser
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def links():
    songs = [
    "https://www.youtube.com/watch?v=ySPKnRY56Cc",
    "https://www.youtube.com/watch?v=xRb8hxwN5zc&list=RDxRb8hxwN5zc&start_radio=1",
    "https://www.youtube.com/watch?v=JTpDCoxZdv8",
    "https://www.youtube.com/watch?v=D_SRMiIWyL4",
    "https://www.youtube.com/watch?v=hYFzyK9ExuM",
    "https://www.youtube.com/watch?v=KcbmbnRX-nU&list=RDKcbmbnRX-nU&start_radio=1",
    "https://www.youtube.com/watch?v=KH_8iNPeDOo&list=RDKH_8iNPeDOo&start_radio=1",
    "https://www.youtube.com/watch?v=dYPpr4ZLa1I",
    "https://www.youtube.com/watch?v=2ySr4lR0XFg&list=RDxRb8hxwN5zc&index=21",
    "https://www.youtube.com/watch?v=olmU0FVe-nc&list=RDolmU0FVe-nc&start_radio=1",
    "https://www.youtube.com/watch?v=rjA_q9Ma_9U&list=RDolmU0FVe-nc&index=7",
    "https://www.youtube.com/watch?v=2ySr4lR0XFg",
    "https://www.youtube.com/watch?v=KAca7KQ9p-A&list=RDKAca7KQ9p-A&start_radio=1",
    "https://www.youtube.com/watch?v=D_SRMiIWyL4&list=RDxRb8hxwN5zc&index=18",
    "https://www.youtube.com/watch?v=QlFwVjhllzQ&list=RDxRb8hxwN5zc&index=17",
    "https://www.youtube.com/watch?v=Xc4veW5wF48&list=RDxRb8hxwN5zc&index=22",
    "https://www.youtube.com/watch?v=eOZ0PR6Kr8w&list=RDeOZ0PR6Kr8w&start_radio=1",
    "https://www.youtube.com/watch?v=vczpI9OPZB8",
    "https://www.youtube.com/watch?v=2BT70EPS9mE",
    "https://www.youtube.com/watch?v=K-Ts-NFR62o",
]
    
    chosen_song = random.choice(songs)
    webbrowser.open(chosen_song)

def youtubelinks():
    print("Enter the YouTube links to add. Type 'done' when finished:")
    speak("Enter the link Here  ")
    new_links = []

    # Collect new links from user input
    while True:
        user_input = input()
        if user_input.lower() == "done":
            break
        else:
            new_links.append(user_input)

    # Read the existing songs list from the file
    with open("myFavSongs.py", "r") as file:
        lines = file.readlines()

    # Find the line with 'songs =' and create a new list to store the combined songs
    combined_songs = []
    for line in lines:
        if line.strip().startswith("songs = ["):
            combined_songs.append(line)  # Keep the opening bracket
        elif line.strip() == "]":
            # Add new links before closing bracket
            for link in new_links:
                combined_songs.append(f'    "{link}",\n')
            # Add the closing bracket
            combined_songs.append(line)
        else:
            combined_songs.append(line)  # Keep existing lines

    # Write the combined list back to the file
    with open("myFavSongs.py", "w") as file:
        file.writelines(combined_songs)

    print("Links Added Successfully.")
    speak("DONE BOSS")
    speak("ADDED successfully")
