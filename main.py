import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Change the voice (adjust voices based on your system configuration)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change the index to select a different voice

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said: " + command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Sorry, an error occurred. {0}".format(e))
        return ""

if __name__ == "__main__":
    speak("Hey Boss! How are you?")

    while True:
        command = listen()

        if "how are you" in command:
            speak(f"I am beautiful as ever, how are you Boss?")

        elif "search for" in command:
            query = command.replace("search for", "")
            pywhatkit.search(query)
            speak(f"Searching for {query}...")

        elif "play songs on youtube" in command:
            song = command.replace("play songs on youtube", "")
            pywhatkit.playonyt(song)
            speak(f"Playing {song} on YouTube...")

        elif "tell a joke" in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "What is the time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")

        elif "Later Friday" in command:
            speak("See you Boss!")
            break

        else:
            speak("Sorry boss, you have not yet developed me for that functionality.")
