import speech_recognition as sr
import pyttsx3

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # print("🎙️ Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        # print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        # print("❗Could not understand audio")
        return "❗Could not understand audio"
    except sr.RequestError as e:
        # print(f"❗Speech service error: {e}")
        return " ❗Speech service error"
    
def speak_response(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()
    
# speak_response(listen_to_user())