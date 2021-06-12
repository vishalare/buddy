
import pyttsx3
from PyPDF2.pdf import PageObject
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import sys
import pyautogui
import pdfplumber
from gtts import gTTS
import PyPDF2
from googletrans import Translator
import psutil
import datetime
from instabot import Bot
from playsound import playsound
import keyboard
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',180)



def Speak(Audio):
    
    print(f"Buddy : {Audio}")
    engine.say(Audio)
    engine.runAndWait()

def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    return query.lower()


def TaskExe():

    Speak('BUDDY IS ARRIVED')

    def screenshot():
        img=pyautogui.screenshot()
        img.save('E:\\New folder (3)\\u.png')
        Speak('screenshot taken.....')
    def READER2():
        Speak('the demon book started')
        pdf = pdfplumber.open('The-Demon-Girl.pdf')
        page = pdf.pages[6]
        text = page.extract_text()
        transl = Translator()
        textHin = transl.translate(text,'hi')
        textm = textHin.text
        Speak(textm)
                 

    def bookReader():
            Speak("Tell Me The Name Of The Book!")

            v = takecommand()

            if 'random'in v:

                os.startfile('E:\\New folder (3)\\180220131101_AS4.pdf')
                book = open('E:\\New folder (3)\\180220131101_AS4.pdf','rb')
                pdfreader = PyPDF2.PdfFileReader(book)
                pages = pdfreader.getNumPages()
                Speak(f"Number Of Pages In This Books Are {pages}")
                Speak("From Which Page I Have To Start Reading ?")
                numPage = int(input("Enter The Page Number :"))
                page= pdfreader.getPage(numPage) 
                text = page.extractText()
                print(text)
                Speak("In Which Language , I Have To Read ?")
                Speak(text)

    def Music():
        Speak("Tell Me The NamE oF The Song!")
        musicName = takecommand()
        Speak('ENJOY YOUR MUSIC') 
        pywhatkit.playonyt(musicName)


    def OpenApps():
        Speak("HEY BUDDY,WAIT A SECOND!")
        
        if 'discord' in query:
            os.startfile("C:\\Users\\deepak rajput\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk")

        elif 'telegram' in query:
            os.startfile("C:\\Users\\deepak rajput\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Telegram Desktop\\Telegram.lnk")

        elif 'chrome' in query:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk")

        elif 'spotify' in query:
            os.startfile('C:\\Users\\deepak rajput\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk')
        
        elif 'teams' in query:
            os.startfile('C:\\Users\\deepak rajput\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams.lnk')
        
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@23.0199968,72.2995501,10z')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        Speak("working on your command")

    def CloseAPPS():
        Speak("Ok Sir , Wait A second!")

        if 'youtube' in query:
            os.close("TASKKILL /F /im chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'telegram' in query:
            os.system("TASKKILL /F /im telegram.exe")

        elif 'discord' in query:
            os.close("TASKKILL /F /im discord.exe")
        
        elif 'teams' in query:
            os.close("TASKKILL /F /im teams.exe")

        elif 'spotify' in query:
            os.system("TASKKILL /F /im spotify.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        Speak("Your Command Has Been Succesfully Completed!")

    def automaticyoutube():
        Speak("Whats Your Command ?")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'next' in comm:
            keyboard.press_and_release('shift + n')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        Speak("Done Sir")

        
    def ChromeAuto():
        Speak("Chrome Automation started!")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')

    def instamsg():
            bot=Bot()
            Speak('enter your message buddy')
            text=input('enter msg;')
            Speak('enter receiver username')
            to=input(' enter receiver username;')
            Speak('enter your username buddy')
            username=input('enter username;')
            Speak('enter your password buddy')
            password=input('enter password;')
            
            bot.login(username=username, password=password)
            bot.send_message(text,[to])

    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("hey i am buddy .")
            Speak('how are you ')

        elif 'how are you' in query:

            Speak("I Am Fine Sir!")
            Speak("Whats About YOU?")
        
        elif 'screenshot' in query:
            screenshot()

        elif 'good' and ' fine' and 'what about'in query:
            Speak('good too here that you are fine')
            Speak('and i am always fine  unless you write wrong code')

        elif 'age' and 'old ' in query:
            Speak('i am younger then you lol by the way i am nineteen')

        elif 'who made you' and 'who create you' in query:
            Speak('rv create me for his college project')
    
        elif 'ok bye buddy' in query:
            Speak("Ok Sir ")
            Speak("Just remember buddy is always ther efor you ")
            break
        
        elif 'youtube search' in query:

            Speak("going to youtube for your search")
            query = query.replace("buddy","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("task done sir ")

        #elif 'open camera' in query:
            
            #camera()
        
        elif 'read the book' in query:
            bookReader()

        elif 'website' in query:
            Speak("Ok Sir , Launching.....")
            query = query.replace("buddy","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'launch' in query:
            Speak("Tell Me The Name Of The Website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("buddy","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif 'open facebook' in query:
            OpenApps()
            Speak('opening facebook.....')

        elif 'open instagram' in query:
            OpenApps()
            Speak('opening instagram.....')

        elif 'open maps' in query:
            OpenApps()
            Speak('opening maps.....')

        elif 'open discord' in query:
            OpenApps()
            Speak('discord lunching.....')

        elif 'open team' in query:
             OpenApps()
             Speak('opening team.....')
        
        elif 'open spotify' in query:
            OpenApps()
            Speak('now spotify is open for you.....')

        elif 'open youtube' in query:
            OpenApps()
            Speak('mission youtube over.....')
            
        elif 'open telegram' in query:
            OpenApps()
            Speak('mission telegram over.....')  

        elif 'open chrome' in query:
          OpenApps()
          Speak('opening chrome.....')

        elif 'close chrome' in query:
            CloseAPPS()

        elif 'music' in query:
            Music()

        elif 'close telegram' in query:
            CloseAPPS()

        elif 'close discord' in query:
            CloseAPPS()

        elif 'close spotify' in query:
            CloseAPPS()

        elif 'close team' in query:
            CloseAPPS()

        elif 'close instagram' in query:
            CloseAPPS()

        elif 'close facebook' in query:
            CloseAPPS()

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'next' in query:
            keyboard.press_and_release('shift + n')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            automaticyoutube()

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl +h')

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'on instagram' in query:
            instamsg()
            Speak('message send sir')

        elif 'joke' in query:
            joke= pyjokes.get_joke()
            Speak(joke)

        elif ' the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {strTime}")

        elif ' the date ' in query:
            date=datetime.datetime.now().date()
            Speak(f"Sir, today is {date}")
        
        elif 'the day' in query:
            Speak(f"Sir, today is {date.day}")

        elif 'the month' in query:
            Speak(f"Sir,the  running month  is {date.month}")

        elif 'year' in query:
            Speak(f"Sir, the year  s {date.year}")
                
            
        elif 'repeat my word' in query:
            Speak("Speak Sir!")
            jj = takecommand()
            Speak(f"You Said : {jj}")

        elif 'my location' in query:
            Speak("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/@23.0199968,72.2995501,10z')



TaskExe()


if __name__ == '__main__':
    while True :
        cmd=takecommand()
        if 'wake up' and 'start' in cmd:
            TaskExe()
        elif 'close' in cmd:
            Speak('THANKS FOR USING ME')
            sys.exit()