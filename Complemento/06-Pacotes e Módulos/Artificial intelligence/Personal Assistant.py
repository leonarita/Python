import speech_recognition as sr
import pyttsx3
import wikipedia


def speak(string):
    engine = pyttsx3.init()
    engine.say(string)
    engine.runAndWait()


def userInput():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
        query = r.recognize_google(audio)
    return query


def out():
    query = userInput().lower()
    print(f"User said: {query}")
    results = wikipedia.summary(query, sentences=3)
    print(results)
    speak("Wikipedia said:")
    speak(results)


speak("Hello Sir, how can I help you?")
speak("What do you want to search on Wikipedia?")
out()