"""Defining speechrecognition functionality"""

import os
import subprocess
from datetime import datetime
from logging.config import listen
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha
import requests

# Speech engine initialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female
activationWord = 'computer'  # Single word

def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 1
        input_speech = listener.listen(source)

    try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en_gb')
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that')
        print(exception)
        return 'None'

    return query


if __name__ == "__main__":
    speak('All systems nominal.')

    while True:
        # Parse as a list
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)
            response = requests.get("http://localhost:8000/api/document/")
            data = response.json()
            for item in data['items']:
                command = item['command']
                if command in query:
                    command_id = item['id']
                    url = f'http://localhost:8000/api/document/{command_id}/eval/'

                    response = requests.get(url)
