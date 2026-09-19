import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser

# ----------------------------------------------------
# 1. Voice Engine Setup (JARVIS - Tone & Pitch)
# ----------------------------------------------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# टोनी स्टार्क के Jarvis की तरह Male/British वॉइस सेट करना
for voice in voices:
    if "male" in voice.name.lower() or "david" in voice.name.lower() or "george" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# बोलने की गति (Jarvis शांत और प्रोफेशनल लहजे में बोलता है)
engine.setProperty('rate', 160)

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

# ----------------------------------------------------
# 2. Voice Command Input (आपकी आवाज़ सुनना)
# ----------------------------------------------------
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio, language="hi-IN")
            print(f"You said: {command}")
            return command.lower()
        except:
            return ""

# ----------------------------------------------------
# 3. Main Features & Workflows (Jarvis Personality)
# ----------------------------------------------------
def jarvis_assistant():
    speak("Yes Sir! I am online and fully operational.")
    
    # वेलकम और टाइम चेक
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"Sir, the current time is {current_time}. How was your day today, Sir?")

    is_active = True

    while is_active:
        command = listen_command()

        if not command:
            continue

        # वेक वर्ड और रिस्पांस (Hey Jarvis)
        if "हे जार्विस" in command or "hey jarvis" in command or "जार्विस" in command or "jarvis" in command:
            speak("Yes Sir, at your service.")

        # 1. ऐप खोलने का कमांड
        elif "खोलो" in command or "open" in command:
            if "यूट्यूब" in command or "youtube" in command:
                speak("Sir, opening YouTube for you right now.")
                webbrowser.open("https://youtube.com")
            elif "गूगल" in command or "google" in command:
                speak("Sir, launching Google search.")
                webbrowser.open("https://google.com")
            elif "व्हाट्सएप" in command or "whatsapp" in command:
                speak("Sir, opening WhatsApp.")
                webbrowser.open("https://web.whatsapp.com")
            else:
                speak("Sir, opening the requested application.")

        # 2. मैसेज और टाइपिंग
        elif "मैसेज करो" in command or "टाइप करो" in command:
            speak("Sir, sending the message as instructed.")

        # 3. कॉलर आईडी / कॉल अनाउंसमेंट
        elif "कॉल आया" in command or "किसका कॉल है" in command:
            if "अननोन" in command or "अज्ञात" in command:
                speak("Sir, you have an incoming call from an unknown number.")
            else:
                speak("Sir, you have an incoming call from Rahul.")

        # 4. कोडिंग असिस्टेंस
        elif "कोड करो" in command or "कोडिंग" in command:
            speak("Sir, initiating code execution immediately.")

        # 5. शट डाउन / ऑफ कमांड
        elif "शट डाउन" in command or "बंद हो जाओ" in command or "off" in command:
            speak("Shutting down systems. Have a good time, Sir.")
            is_active = False

if __name__ == "__main__":
    jarvis_assistant()
