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

# Main loop
if __name__ == "__main__":
    speak('All systems nominal.')

    while True:
        # Parse as a list
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            # list command
            """
            if 'hello' in query:
                speak('Greetings, all')
            else:
                query.pop(0) # remove say
                speech = ' '.join(query)
                speak(speech)
            """
            if 'firefox' in query:
                os.system("open firefox")
            if 'maxima' in query:
                subprocess.run(
                    [
                        "C:/Program Files/Git/git-bash",
                        "-c",
                        "C:/maxima-5.45.1/bin/wxmaxima.exe",
                    ],
                    capture_output=True,
                    shell=False,
                    check=True,
                )
def eval_document_controller(id: int):
    """GET method subprocess (getting object by id)
    code example:
    "emacsclient -e '(with-current-buffer (window-buffer) (latex-insert-block \"center\"))'"
    "C:/Program Files/Git/git-bash -c open C:/Program Files/Image-Line/FL Studio 20/FL64.exe"
    """

    document = Document.objects.get(id=id)
    text = document.request_path

    part1 = re.findall(r"^\s*(.*?)\s-", text)[0]
    part2 = re.findall(r'( -\w+)', text)[0]
    part3 = re.findall(r" -\w+ (.*)", text)[0]

    my_command = [part1, part2, part3]

    czesci1 = re.findall(r"^\s*(.*?)\s-", text)
    czesci2 = re.findall(r'( -\w+)', text)
    czesci3 = re.findall(r"-\w+ (.*)", text)

    command_eval = f'open "{document.request_path}"'

    #czesci1 = re.findall(r"^\s*(.*?)\s-", tekst)
    #czesci2 = re.findall(r'(-[^"]*?)\'', tekst)
    #czesci3 = re.findall(r"-\w+ (.*)", tekst)

    tekst = "emacsclient -e '(with-current-buffer (window-buffer) (latex-insert-block \"center\"))'"
    tekst = "C:/Program Files/Git/git-bash -c open C:/Program Files/Image-Line/FL Studio 20/FL64.exe"

    part1 = re.findall(r"^\s*(.*?)\s-", tekst)[0]
    part2 = re.findall(r'( -\w+)', tekst)[0]
    part3 = re.findall(r" -\w+ (.*)", tekst)[0]

    my_command = [part1, part2, part3]

    print(my_command)
    #czesci3 = re.findall(r"'(.*?)'", tekst)
    # czesci = re.findall(r"(-.*?)(?=\'.*)", tekst)
    # czesci = re.findall(r" -\s*(.*?)\s'", tekst)
    # czesci = re.findall(r"^\s*(.*?)\s-", tekst)
    # czesci = re.split(r"\s ", tekst)
    # czesci = re.findall(r"\w+ | '(.*?)'", tekst)
    # czesci = re.findall(r"'(.*?)'", tekst)
    # print(czesci)
    """
    my_command = ["C:/Program Files/Git/git-bash", "-c", command_eval]
    my_command2 = [
        "emacsclient",
        "-e",
        '(with-current-buffer (window-buffer) (latex-insert-block "center"))'
        ]

    subprocess.run(
        czesci,
        capture_output=True,
        shell=False,
        check=True,
    )

    """
    # os.system('open "C:/Program Files/Image-Line/FL Studio 20/FL64.exe"')

    return my_command
    #return czesci
