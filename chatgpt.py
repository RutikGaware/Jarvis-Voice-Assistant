import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio

# Dummy music library
musiclibrary = {
    "song1": "https://www.youtube.com/watch?v=abcd1234",
    "song2": "https://www.youtube.com/watch?v=xyz5678"
}

recognition = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, song not found.")

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening for Jarvis keyword...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis Active... Listening for command")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")
                    processCommand(command)

        except Exception as e:
            print("Error: {0}".format(e))
