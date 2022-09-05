import pyttsx3 as p
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import smtplib
import psutil
import pyjokes
import pyautogui
from loc import weather
import geocoder
import pyautogui
import psutil
import pyjokes
from sys import platform
import os
import getpass
g = geocoder.ip('me')


listener = sr.Recognizer()
engine = p.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
active = 1
#
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning SIR")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon SIR")

    else:
        speak('Good Evening SIR')

    weather()
    speak('I am JARVIS. Please tell me how can I help you SIR?')
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)
def screenshot():
    img = pyautogui.screenshot()
    img.save('path of folder you want to save/screenshot.png')
def writecoordinates():
    s = str(g.latlng[0])+','+str(g.latlng[1])
    pyautogui.typewrite(s)
writecoordinates()