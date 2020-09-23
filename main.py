
"""

Problem Statement : Make a vitual assisstant like Siri or Cortana that can perform various tasks like opening youtube,performing 
calculations, giving battery percentage, giving weather forecast.

Requirement Specifications: 

Software Requirements: Python
Hardware Requirement: Laptop/PC with a microphone

"""


import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import psutil
import operator
import requests
import sys
import tkinter as tk


print("Initializing Jarvis...")
Master = "Dhrumil"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

# Sends Email


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your@gmail.com', "password")
    server.sendmail("shahjewellery1@gmail.com", to, content)
    server.close()

# Speak function will pronounce the string passed to it


def speak(text):
    engine.say(text)
    engine.runAndWait()

# Will wish you


def wishMe():
    hour = datetime.datetime.now().hour
    # print(hour)
    if hour >= 0 and hour < 12:
        speak("Good morning" + Master)
    elif hour >= 12 and hour < 18:
        speak("Good afternoon" + Master)
    else:
        speak("Good evening" + Master)

    speak("How may I help you?")

# Takes the command from user


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')

    except sr.UnknownValueError:
        speak("Sorry sir! I didn't get that! Try typing the command!")
        query = str(input('Command: '))
    return query


# Returns the operator from the equation
def get_operator_fn(op):
    return {
        '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        'divided': operator.__truediv__,
        'Mod': operator.mod,
        'mod': operator.mod,
        '^': operator.xor,
    }[op]


# Solve the maths problems
def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)


# Main Function


if __name__ == '__main__':

    speak("Initializing Jarvis...")
    wishMe()

    # logic for executing tasks as per the query

    while True:

        query = takeCommand()
        query = query.lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'describe yourself' in query:
            print("Hi, I am JARVIS. (Just A Rather Very Intelligent System) . I was originally created by Tony Stark aka Iron man. I was redesigned and brought back to life by Dhrumil and Yash. Speed 1 Terahertz and memory 1 Zettabyte. ")
            speak("Hi, I am JARVIS. (Just A Rather Very Intelligent System) . I was originally created by Tony Stark aka Iron man. I was redesigned and brought back to life by Dhrumil and Yash. Speed 1 Terahertz and memory 1 Zettabyte. ")
        elif 'hello' in query or 'hi' in query:
            speak('Hi, Sir!')

        elif 'open youtube' in query:
            url = "youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open reddit' in query:
            url = "reddit.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"{Master} the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Shah\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'play music' in query:
            songs_dir = "C:\\Users\\Shah\\Downloads\\music"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'email' in query:
            try:
                speak("What should I send")
                content = takeCommand()
                to = "shahjewellery1@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully")

            except Exception as e:
                print(e)
        elif 'battery' in query.lower():
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = str(battery.percent)
            if plugged == False:
                plugged = "Not Plugged In"
            else:
                plugged = "Plugged In"
            print(percent+'% | '+plugged)
            speak(percent)
            speak(plugged)

        elif 'mathematics' in query.lower():
            speak("please tell the question")
            content = takeCommand()
            print(eval_binary_expr(*(content.split())))

        elif 'weather' in query.lower():
            api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=ef5f47970188ee0a020d5c029cf6ae86&q='
            print('Please tell city name')
            speak('Please tell city name')
            city = takeCommand()
            url = api_address + city
            json_data = requests.get(url).json()
            formatted_data = json_data['weather'][0]['description']
            Celcius = int(json_data['main']['temp']) - 273
            print("Description :", formatted_data)
            speak(formatted_data)
            print("Temperature in deg Celcius :", Celcius)
            speak(Celcius)
            speak("Degree Celcius")

        elif 'nothing' in query or 'bye' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        print('Sir! please give next command ')
        speak('Sir! please give next command ')
