import speech_recognition as sr
import pyttsx3
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens to the user's voice command."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was a problem with the speech recognition service.")
            speak("Sorry, there was a problem with the speech recognition service.")
            return None

def respond(command):
    """Responds to the user's command."""
    if command is None:
        return

    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        query = command.replace("search", "").strip()
        search_web(query)
    else:
        speak("I'm sorry, I didn't understand that command.")

def search_web(query):
    """Searches the web for the given query and reads out the top results."""
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for g in soup.find_all(class_='BNeawe vvjwJb AP7Wnd'):
        results.append(g.get_text())

    if results:
        speak("Here are some search results:")
        for result in results[:5]:
            print(result)
            speak(result)
    else:
        speak("Sorry, I couldn't find any results.")

# Main loop
if __name__ == "__main__":
    speak("Voice assistant activated. How can I help you today?")
    while True:
        command = listen()
        respond(command)
