import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import os

assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
assistant.setProperty('voices', voices[0].id)


def Speak(audio):
    assistant.say(audio)
    print(f"EDITH:{audio}")
    assistant.runAndWait()


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognising...")
            query = command.recognize_google(audio, language='en-in')
            print(f"User Said:{query}")

        except Exception as Error:
            return "None"

        return query.lower()


def wishme():
    Speak("Hello sir")

def taskexe():
    while True:
        query = takecommand()

#LITRETAURE
        if 'hello' in query:
            Speak("hello sir, what are we going to do")
        
        elif 'hello edith' in query:
            Speak("Hello sir, what should we do today.")

        elif 'hi' in query:
            Speak("Hi Sir, what do you want to do today.")

        elif 'edith' in query:
            Speak("Yes Sir, any help")

        elif 'have a rest' in query:
            Speak("Ok sir, Just call me when you need me")
            break

        elif 'have a break' in query:
            Speak("Ok sir, i will be there when you need me")
            break

        elif 'have a rest' in query:
            Speak("Ok sir, just call my name for any help")
            break

        elif 'cool down' in query:
            Speak("Ok sir, just call me if you need any help")
            break

        elif 'bye' in query:
            Speak("Bye Sir,")
            break

        elif 'bye edith' in query:
            Speak("Bye Sir,")
            break

        elif 'tell me who you are' in query:
            Speak("I am an artificial intelligence called Edith, Which means Even dead i am the hero , and i can do anythingg you can think of")

        elif 'tell me who are you' in query:
            Speak("I am an artificial intelligence called Edith, Which means Even dead i am the hero , and i can do anythingg you can think of")

        elif 'tell me who am i' in query:
            Speak( "You are a boy who studies in lps and has created an ai called Edith, Your name is T.Mani Balaa Raghava Reddy,")

#Youtube
        if 'youtube search' in query:
            Speak("Searching...")
            query = query.replace("edith", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            print("        ")
            Speak("Done sir")

#google
        elif 'google search' in query:
            Speak("Searching...")
            query = query.replace("edith", "")
            query = query.replace("google search", "")
            web = 'https://www.google.com/search?q=' + query
            webbrowser.open(web)
            print("         ")
            Speak("Completed")

#website

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
        
        elif 'open opera' in query:
            Speak("ok Sir")
            web = "C:\\Users\\USER\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
            webbrowser.open(web)
            Speak("done")

#websites commonly used
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

#wikepedia
        elif 'wikipedia' in query.lower():
            Speak("What would you like to know ?")
            search_Term = takecommand().lower()
            Speak("Searching {} on wikipedia".format(search_Term))
            result = wikipedia.summary(search_Term, sentences=3)
            Speak('According to wikipedia')
            Speak(result)

#APPS OPENING
        elif 'open word' in query:
            npath = ('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe')
            os.startfile(npath)
            Speak("Opening word")

        elif 'open CMD' in query:
            os.system('open cmd')
            Speak("Opening CMD")

        elif 'open premiere pro' in query:
            npath1 = ('C:\\Program Files\\Adobe\\Adobe Premiere Pro 2021\\Adobe Premiere Pro.exe')
            os.startfile(npath1)
            Speak("Opening Premiere Pro")

        elif 'open photoshop' in query:
            npath2 = ("C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe")
            os.startfile(npath2)
            Speak("Opening photoshop")

        elif 'open audition' in query:
            npath3 = ("C:\\Program Files\\Adobe\\Adobe Audition 2021\\Adobe Audition.exe")
            os.startfile(npath3)
            Speak("Opening Audition")

        elif 'open powershell'in query:
            os.system('open powershell')
            Speak("Opening powershell")

wishme()
takecommand()
taskexe()
    
    