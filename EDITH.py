#IMPORTS FOR PROJECT
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import sys

#DEFINING VOICE ENGINE
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#TO TURN TEXT TO SPEACH
def Speak(audio):
    print("  ")
    engine.say(audio)
    print(f"EDITH:{audio}")
    engine.runAndWait()

#TO TURN VOICE TO TEXT
def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognising...")
            query = command.recognize_google(audio, language='en-in')
            print(f"User: {query}")

        except Exception as e:
            Speak("Please say it again")
            return "none"
        return query

#TO WISH THE USER
def wishme():   
    Speak("Initializing edith...")
    Speak("Starting all systems applications...")
    Speak("Installing and checking all drivers...")
    Speak("Caliberating and examining all the core processors...")
    Speak("All drivers are up and running...")
    Speak("All systems have been activated...")
    Speak("Now I am online")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        Speak("Good Morning sir,")
    elif hour>=12 and hour<=18:
        Speak("Good Afternoon sir,")
    else:
        Speak("Good Evening sir,")

if __name__ == '__main__':
    wishme()
    
#LOGIC OF AI 
while True:
    query = takecommand().lower()

#OPENING COMMON APPS
    if 'open word' in query:
        npath = ('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe')
        os.startfile(npath)
        Speak("Opening Word...")

    if 'open ward' in query:
        npath = ('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe')
        os.startfile(npath)
        Speak("Opening Word...")

    if 'open wood' in query:
        npath = ('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe')
        os.startfile(npath)
        Speak("Opening Word...")

    if 'open excel' in query:
        npath4 =  ("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
        os.startfile(npath4)
        Speak("Opening Excel..")

    elif 'open powerpoint' in query:
            npath5 = ("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
            os.startfile(npath5)
            Speak("Opening Powerpoint...")

    elif 'open publisher' in query:
            npath6 = ("C:\\Program Files\\Microsoft Office\\root\\Office16\\MSPUB.EXE")
            os.startfile(npath6)
            Speak("Opening Publisher...")

    elif 'open access' in query:
            npath7 = ("C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE")
            os.startfile(npath7)
            Speak("Opening Access...")
        
    elif 'open pycharm' in query:
            npath8 = ("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.3\\bin\\pycharm64.exe")
            os.startfile(npath8)
            Speak("Opening Pycharm...")

    elif 'open rider' in query:
            npath9 = ("C:\\Program Files\\JetBrains\\JetBrains Rider 2021.1.1\\bin\\rider64.exe")
            os.starfile(npath9) 
            Speak("Opening Rider...")

    elif 'open vs code ' in query:
            npath10 = ("C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            os.startfile(npath10)
            Speak("Opening VS Code...")

    elif 'open google' in query:
            npath11 = ("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            os.startfile(npath11)
            Speak("Opening Google...")


    elif 'open edge' in query:
            npath12 = ("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
            os.startfile(npath12)
            Speak("Opening edge...")

    elif 'open command prompt' in query:
            os.system("start cmd")
            Speak("Opening Cmd...")

    elif 'open powershell' in query:
            os.system("start powershell")
            Speak("Opening Powershell...")

    elif 'open calculator' in query:
            path13 = ('C:\\Windows\\System32\\calc.exe')
            os.startfile(path13)
            Speak("Opening Calculator...")


#LITRETAURE
    elif 'good morning' in query:
        Speak("What should we do today")    
    
    elif 'good afternoon' in query:
        Speak("What should we do today")    
    
    elif 'good evening' in query:
        Speak("What should we do today")

    elif 'good morning jarvis' in query:
        Speak("What should we do today")    
    
    elif 'good afternoon jarvis' in query:
        Speak("What should we do today")
    
    elif 'good evening jarvis' in query:
        Speak("What should we do today")

    elif 'hello' in query:
            Speak("what are we going to do today")

    elif 'hello edith' in query:
            Speak("what should we do today.")

    elif 'hi' in query:
            Speak("what do you want to do today.")

    elif 'edith' in query:
            Speak("Yes Sir, any help")

    elif 'have a rest' in query:
            Speak("Ok sir, Just call me when you need me")
            sys.exit()

    elif 'have a break' in query:
            Speak("Ok sir, i will be there when you need me")
            sys.exit()
    
    elif 'take a break' in query:
        Speak("Ok sir, i will be there when you need me")
        break

    elif 'chill' in query:
            Speak("Ok sir, just call my name for any help")
            sys.exit()

    elif 'cool down' in query:
            Speak("Ok sir, just call me if you need any help")
            sys.exit()

    elif 'bye' in query:
            Speak("Bye Sir,")
            sys.exit()

    elif 'bye edith' in query:
            Speak("Bye Sir,")
            sys.exit()

    elif 'bey bye' in query:
        Speak("likewise")
        sys.exit

    elif 'tell me who you are' in query:
            Speak("I am an artificial intelligence called Edith, Which means Even dead i am the hero , and i can do anythingg you can think of")

    elif 'tell me who are you' in query:
            Speak("I am an artificial intelligence called Edith, Which means Even dead i am the hero , and i can do anythingg you can think of")

    elif 'tell me who am i' in query:
            Speak( "You are a boy who studies in lps and has created an ai called Edith, Your name is T.Mani Balaa Raghava Reddy,")

#CAMERA
    elif 'open camera' in query:
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('CAMERA', img)
            k = cv2.waitKey(10)
            if k==10:
                break;

        cap.release()
        cv2.destroyAllWindows()

#IP address
    if 'tell my ip address' in query:
        ip = get('https://api.ipify.org').text
        Speak(f"Your IP address is {ip}")
    
    if 'get my ip address' in query:
        ip = get('https://api.ipify.org').text
        Speak(f"Your IP address is {ip}")
    
    if 'what is my ip address' in query:
        ip = get('https://api.ipify.org').text
        Speak(f"Your IP address is {ip}")
    
    if 'whats my ip address' in query:
        ip = get('https://api.ipify.org').text
        Speak(f"Your IP address is {ip}")
   
    if 'tell me my ip address' in query:
        ip = get('https://api.ipify.org').text
        Speak(f"Your IP address is {ip}")
    
    if 'tell me the current ip address' in query:
        ip = get('https://api.ipify.org').text
        Speak(f"Your IP address is {ip}")
    
    if 'ip address' in query:
        ip = get('https://api.ipify.org').text
        Speak(f"Your IP address is {ip}")
    
    if 'find my ip address' in query:
        ip = get('https://api.ipify.org').text
        Speak(f"Your IP address is {ip}")

#wikepedia
    elif 'wikipedia' in query.lower():
        Speak("Who or What would you like to know about ?")
        search_Term = takecommand().lower()
        Speak("Searching {} on wikipedia".format(search_Term))
        result = wikipedia.summary(search_Term, sentences=3)
        Speak('According to wikipedia')
        Speak(result)

#Youtube

    elif 'search on youtube' in query:
        Speak("What should i search for")
        cm  = takecommand()
        webbrowser.open(f'https://www.youtube.com/results?search_query={cm}')
    
    elif 'youtube search' in query:
        Speak("What should i search for")
        cm  = takecommand()
        webbrowser.open(f'https://www.youtube.com/results?search_query={cm}')
    elif 'youtube' in query:
        Speak("What should i search for")
        cm  = takecommand()
        webbrowser.open(f'https://www.youtube.com/results?search_query={cm}')

    elif 'a search on youtube' in query:
        Speak("What should i search for")
        cm  = takecommand()
        webbrowser.open(f'https://www.youtube.com/results?search_query={cm}')

    elif 'use youtube' in query:
        Speak("What should i search for")
        cm  = takecommand()
        webbrowser.open(f'https://www.youtube.com/results?search_query={cm}')

#TO OPEN COMMOM WEBSITES
    elif 'open instagram' in query:
            Speak("ok sir")
            webbrowser.open("https://www.instagram.com")
            Speak("Done")

    elif 'open twitter' in query:
            Speak("Ok Sir")
            webbrowser.open("https://twitter.com/home?lang=en")
            Speak("Done")

    elif 'open discord' in query:
            Speak("ok sir")
            webbrowser.open("https://discord.com/channels/@me/874924000583749674")
            Speak("Done")

    elif "open my youtube channel" in query:
            Speak("Ok Sir")
            webbrowser.open("https://studio.youtube.com/channel/UCVxaJQ2cTi_n0Zazqna4b0w")
            Speak("Done")

    elif "open youtube" in query:
            Speak("ok sir")
            webbrowser.open("https://youtube.com")
            Speak("done")
        
    elif 'open gmail' in query:
        Speak("ok sir")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        Speak("")

#TO LAUNCH A WEBSITE

    elif 'launch website' in query:
            Speak("Tell me the name of the website")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("found it!")

    elif 'search website' in query:
            Speak("Tell me the name of the website")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("found it!")

    elif 'open browser' in query:
            Speak("ok Sir")
            web = "C:\\Users\\USER\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
            webbrowser.open(web)
            Speak("done")

#GOOGLE


    elif 'google search' in query:
        Speak("What should i search for")
        cm  = takecommand().lower()
        webbrowser.open(f'http://www.google.com/search?q={cm}')
    
    elif 'search' in query:
        Speak("What should i search for")
        cm  = takecommand().lower()
        webbrowser.open(f'http://www.google.com/search?q={cm}')

    elif 'google' in query:
        Speak("What should i search for")
        cm  = takecommand().lower()
        webbrowser.open(f'http://www.google.com/search?q={cm}')

    elif 'search the web' in query:
        Speak("What should i search for")
        cm  = takecommand().lower()
        webbrowser.open(f'http://www.google.com/search?q={cm}')

    elif 'a search on google' in query:
        Speak("What should i search for")
        cm  = takecommand().lower()
        webbrowser.open(f'http://www.google.com/search?q={cm}')
    
    elif 'use google' in query:
        Speak("What should i search for")
        cm  = takecommand().lower()
        webbrowser.open(f'http://www.google.com/search?q={cm}')


