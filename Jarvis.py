import datetime
import os
import pyttsx3
import speech_recognition as sr
import urllib.parse
import webbrowser

# Voice Engine Setup
engine = pyttsx3.init()
engine.setProperty("rate", 170)


def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()


def greet_and_status():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    # Weather setup requires an API key like OpenWeatherMap
    speak(
        f"Yes sir! Current time is {current_time}. Today weather is expected to be clear, sir."
    )


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language="hi-IN")
        print(f"User said: {query}")
        return query.lower()
    except Exception:
        return ""


def run_jarvis():
    speak("Hello Boss! How can I help you today?")
    while True:
        command = listen_command()

        if "hey jarvis" in command or "जार्विस" in command:
            greet_and_status()

        elif "समय" in command or "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, current time is {current_time}")

        elif "youtube पर ढूंढो" in command or "search on youtube" in command:
            search_query = command.replace("youtube पर ढूंढो", "").strip()
            url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(search_query)}"
            webbrowser.open(url)
            speak(f"Sir, searching {search_query} on YouTube.")

        elif "गूगल पर ढूंढो" in command or "search on google" in command:
            search_query = (
                command.replace("गूगल पर ढूंढो", "")
                .replace("search on google", "")
                .strip()
            )
            url = (
                f"https://www.google.com/search?q={urllib.parse.quote(search_query)}"
            )
            webbrowser.open(url)
            speak(f"Sir, here are the search results for {search_query}.")

        elif "खोलो" in command or "open" in command:
            # Android / Windows app launcher logic
            app_name = command.replace("खोलो", "").replace("open", "").strip()
            speak(f"Opening {app_name}, sir.")
            # Example for Android package launch using os.system
            # os.system(f"am start -n {app_package_name}")

        elif "stop" in command or "बाय" in command:
            speak("Goodbye sir, have a great day!")
            break


if __name__ == "__main__":
    run_jarvis()
