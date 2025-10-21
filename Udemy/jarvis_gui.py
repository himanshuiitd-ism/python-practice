import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service unavailable.")
        return ""

if __name__ == "__main__":
    speak("Hello! Say something and I’ll repeat it.")
    while True:
        text = listen()
        if "stop" in text.lower():
            speak("Goodbye!")
            break
        elif text:
            speak(f"You said: {text}")
