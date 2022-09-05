import speech_recognition as sr
import pyttsx3 as p
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(".\\chromedriver.exe")

name = 'jarvis'

listener = sr.Recognizer()
engine = p.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
active = 1
#
def listen():
    with sr.Microphone() as source:
        text = listener.listen(source)
        recognised_text = listener.recognize_google(text)
        recognised_text = recognised_text.lower()
    print(recognised_text)
    return recognised_text
def speak(text):
    engine.say(text)
    engine.runAndWait()
def type(text):
    words = text.split(' ')
    for i in range(len(words)):
        if words[i] == 'backspace':
            pyautogui.press('backspace')
            words.remove(words[i])
        elif words[i] == 'remove':
            for j in range(len(words[i+1])):
                pyautogui.press('backspace')
            words.remove(words[i])
            words.remove(words[i])
        if len(words) == 0:
            break
    if text != '':
        text = ' '.join(words)
        pyautogui.write(text,0.1)

def removewords(text, type, *args):
    words = text.split(' ')
    wc = []
    if type == 2:
        for word in words:
            if word not in args:
                wc.append(word)
        return ' '.join(wc)
    elif type == 1:
        for word in words:
            if word not in args:
                wc.append(word)
        return ' '.join(wc)
def openwebsite(text3):
    global text
    text = removewords(text3,2,'go', 'to')
    if text.endswith('.com') or text.endswith('.in'):
        print('web: ',text)
        text = 'https://'+text
        driver.get(text)

    elif '.' not in text:
        speak('should i search web for' + text)
        ans = listen()
        if ans in  ['yes','please','yeah']:
            text = 'https://www.google.com/search?source=hp&ei=-ZFgX7vEIO-Q4-EP54Cz4AM&q='+text+'&oq='+text+'&gs_lcp=CgZwc3ktYWIQAzIRCC4QsQMQiwMQqAMQmAMQkwIyBQgAELEDMgcIABCxAxAKMg4ILhCxAxCLAxCoAxCYAzIICC4QsQMQiwMyBQgAEIsDMgUILhCLAzIHCAAQChCLAzIFCAAQiwMyDgguELEDEIsDEKgDEKQDOg4IABDqAhC0AhCaARDlAjoICC4QsQMQkwI6AggAOgsILhCxAxDHARCjAjoCCC46BQguELEDOggILhCxAxCDAVCkG1ixIGDbP2gBcAB4AIABpAaIAe8RkgEHNC0xLjIuMZgBAKABAaoBB2d3cy13aXqwAQa4AQE&sclient=psy-ab&ved=0ahUKEwj7pJfb9OrrAhVvyDgGHWfADDwQ4dUDCAc&uact=5'
            driver.get(text)
def commands(text):
    global active
    text = text.lower()
    #say things
    if text.startswith('speak') or text.startswith('say') or text.startswith('pic') or text.startswith('bolo') or text.startswith('bol'):
        text = removewords(text,1,'speak','say','pic','bolo','bol')
        speak(text)
    elif text.startswith('go to'):
        openwebsite(text)
    # change voices between male and female
    elif text.startswith('print') or text.startswith('ring'):
        text = removewords(text,1,'print','ring')
        type(text)
    elif 'change' in text and 'voice' in text :
        changevoice(text)
    # stop listening
    elif 'top listening' in text:
        speak('fine')
        print('deactivated')
        active = 0
    # start listening
    elif 'start listening' in text or 'jarvis' in text:
        print('activated')
        speak('yeah')
        active = 1
    elif 'stop execution' == text:
        speak('terminating program')
        exit(0)
    if 'over' in text:
        speak('over')




def changevoice(text):
    if 'female' in text:
        engine.setProperty('voice', voices[1].id)
        speak('set to female voice sucessfully')
    elif 'mail' in text or 'male' in text:
        engine.setProperty('voice', voices[0].id)
        speak('set to male voice sucessfully')
    else:
        text = removewords(text,'change',"voice")
        speak('could not change voice to'+text)
while True:
    with sr.Microphone() as source:
        text = listener.listen(source)
        try:
            recognised_text = listener.recognize_google(text)
        except:
            recognised_text = '.'
        recognised_text = recognised_text.lower()
    print(recognised_text)
    # hello worldrecognise textd
    if active == 1 or 'start listening' in recognised_text or 'jarvis' in recognised_text:
        commands(recognised_text)

