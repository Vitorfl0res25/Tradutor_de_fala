import speech_recognition as sr
import pyttsx3
from googletrans import Translator

recognizer = sr.Recognizer()
translator = Translator()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio, language='pt')
            text = text.lower()
            print(f"Recognized: {text}")

            translated_text = translator.translate(text, dest='en')
            print(f"Translated: {translated_text.text}")

            engine.say(translated_text.text)
            engine.runAndWait()

    except sr.UnknownValueError:
        continue
