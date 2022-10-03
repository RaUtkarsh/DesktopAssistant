import os
import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
from time import sleep
from keyboard import press
from keyboard import write
from pyautogui import click

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        talk("Good Morning!")

    elif 12 <= hour < 18:
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")


def WhatsAppMsg(name, message):
    os.startfile("C:\\Users\\rajat\\Downloads\\WhatsAppSetup")
    sleep(20)
    click(x=490, y=243)
    sleep(2)
    write(name)
    sleep(1)
    click(x=532, y=342)
    sleep(1)
    click(x=1169, y=894)
    write(message)
    press('enter')


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = r.listen(source)
            command = r.recognize_google(voice)
            command = command.lower()
            if 'mikasa' in command:
                command = command.replace('mikasa', '')
                print(command)
    except:
        pass
    return command


def run_mikasa():
    wishMe()
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'wikipedia' in command:
        talk('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        talk("According to Wikipedia")
        print(results)
        talk(results)

    elif 'open google' in command:
        webbrowser.open("google.com")
        talk("Google is open now")

    elif 'open youtube' in command:
        webbrowser.open("youtube.com")
        talk("Youtube is open now")

    elif 'open gmail' in command:
        webbrowser.open_new_tab("mail.google.com")
        talk("Google Mail open now")

    elif 'make a note' in command:
        statement = command.replace("make a note", "")
        note(statement)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'news' in command:
        webbrowser.open_new_tab("https://timesofindia.indiatimes.com/")
        talk('Here are some headlines from the Times of India')

    elif 'open netflix' in command:
        webbrowser.open_new_tab("netflix.com/browse")
        talk("Netflix open now")

    elif 'open prime video' in command:
        webbrowser.open_new_tab("primevideo.com")
        talk("Amazon Prime Video open now")

    elif 'send message' in command:
        WhatsAppMsg("Harshit", "This is project presentation. Please IGNORE")
        talk("Message Sent")

    else:
        talk('Could not understand. Please rerun')


while True:
    run_mikasa()
    break
