import pyttsx3 
import datetime         
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import os.path
import smtplib
import cv2
from requests import get
import socket
import pywhatkit as w
import sys
import pyjokes
import news_module
import function
import train
import newspaper
import requests
from bs4 import BeautifulSoup #weather forecast
import email_to
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import instaloader
from time import ctime
import time
import pyautogui
import mimetypes
import PyPDF2
import condition
import math
import operator #for calculation using voice
import gtts
import shutil
import pywikihow
from pywikihow import search_wikihow
import psutil
import speedtest
from twilio.rest import Client
import MyAlarm


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)
# engine.setProperty("rate", 200)

# text to speech

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to wish

def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<12:
        speak(f"good morning sir ! it's {tt}")
    
    elif hour>=12 and hour<18:
        speak(f"good afternoon sir ! it's {tt}")

    else:
        speak(f"good evening sir ! it's {tt}")
        
    speak("i am your desktop assistant. please tell me how may i help you")
    

def takeCommand():
    # it takes microphone input from the user and retures string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        # print("say that again please...")
        return "none"
    query = query.lower()
    return query

def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=b5276f7d31c74984aef91ea1fd57182e"
    
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day=["first","second","third","fouth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is : {head[i]}")

def pdf_reader():
    book = open("E:\\project\\hcl.pdf","rb")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

def search_wikihow(query, max_results=10, lang="en"):
    return list(WikiHow.search(query, max_results, lang))

def abs(a, b):
    "same as abs(a)."
    return a + b

def add(a, b):
    "same as a + b."
    return a + b

def and_(a, b):
    "same as a & b."
    return a & b

def floordiv(a, b):
    "same as a // b."
    return a // b

def index(a):
    "same as a.__index__()."
    return a.__index__()

def inv(a):
    "same as ~a."
    return ~a
    invert = inv

def lshift(a, b):
    "same as a << b."
    return a << b

def mod(a,b):
    "same as a % b."
    return a % b

def mul(a, b):
    "same as a * b."
    return a * b


if __name__ == "__main__":
    wishMe()
    # usrname()
    

    while True:
    # if 1:
        query = takeCommand().lower()

# using wikipedia find the information

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            print(results)
            speak(results)
# youtube

        elif 'open youtube' in query or "youtube" in query:
            speak("here you go to youtube")
            webbrowser.open("https://www.youtube.com/")

        elif "play songs on youtube" in query:
            kit.playonyt("see you again")

# google

        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            webbrowser.open("https://www.google.com/")

# open websites

        elif 'open email' in query:
            webbrowser.open("https://mail.google.com/mail")

        elif 'open twitter' in query:
            webbrowser.open("https://twitter.com/")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
    
        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")

        elif 'open amazon' in query:
            webbrowser.open("https://amazon.com")

        elif 'open github' in query:
            webbrowser.open("https://github.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")       

# play music

        elif 'play music' in query or "music" in query:
            music_dir = "E:\\project\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

# open notepad

        elif 'open notepad' in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

# open cmd

        elif 'open command prompt' in query or "cmd" in query:
            os.system("start cmd")

# open camera

        elif 'open camera' in query or "camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

# find the ip address

        elif 'ip address' in query:
            hostname = socket.gethostname()
            ip = get("https://api.ipify.org").text
            print("Your IP Address is : " + ip)
            print("Your Computer Name is : " + hostname)
            speak(f"your IP address is {ip}") 
            speak(f"and your computer name is {hostname}")
            
# time 

        elif "what time is it" in query or "time" in query:
            speak(ctime())

# note
        elif "note" in query:
            speak("what you want")
            note = takeCommand()
            file = open("nitesh.py.txt", "w")
            speak("friend")
            snfm = takeCommand()
            if "hello" in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

# open visual studio

        elif 'open code' in query:
            codepath = "C:\\Users\\Nites\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

  
# find the temperature         
        elif "temperature" in query:
            search = "remperature in mumbai"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

# activate the mode

        elif "activate how to do mode" in query or "activate" in query:
            speak("how to do mode is activated")
            while True:
                speak("please tell me what you want to know")
                how = takeCommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("ok sir, how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this")

# battery percetange

        elif "how much power left" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentange = battery.percent
            speak(f"sir our system have {percentange} percent battery")
            if percentange>75:
                speak("we have enough power to continue our work")
            elif percentange>=40 and percentange<=75:
                speak("we should connect our system to charging point to cahrge our battery")
            elif percentange<=15 and percentange<=30:
                speak("we don't have enough power to work, please connect to charging")
            elif percentange<=15:
                speak("we have very low power, please connect to charging the system will shutdown very soon")

# internet speed
        elif "internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

            try:
                os.system('cmd /k "speedtest"')
            except:
                speak("there is no internet connection")

# laptop shutdown, restart, sleep the system

        elif "shutdown the system" in query or "shutdown" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query or "restart" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query or "sleep" in query:
            os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")

# valume control

        elif "volume up" in query or "up" in query:
            pyautogui.press("volumeup") 

        elif "volume down" in query or "down" in query:
            pyautogui.press("volumedown")

        elif "volume mute" in query or "mute" in query:
            pyautogui.press("volumemute")

# find the joke

        elif "tell me a joke" in query or "joke" in query:
            joke = pyjokes.get_joke()
            print("the joke is :" + joke)
            speak(joke)

# set the alarm

        elif "set alarm" in query or "alarm" in query:
            speak("sir please tell me the set alarm time, for example set alarm to 10:12 am")
            tt = takeCommand()
            tt = tt.replace("set alarm to ", "")
            tt = tt.replace(".","")
            tt = tt.upper()
            MyAlarm.alarm(tt)
            
# the latest news 
       
        elif "tell me news" in query or "news" in query:
            speak("please wait sir, i will the find latest news")
            news()

# switch the window

        elif "switch the window" in query or "window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.KeyUp("alt")

# find the location

        elif "where i am" in query or "where we are" in query:
            speak("hold on sir, let me check")
            try:
                ipAdd = requests.get("https://api.ipify.org").text
                print(ipAdd)
                url = "https://get.geojs.io/v1/ip/geo/"+ipAdd+".json"
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data["city"]
                country = geo_data["country"]
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, Due to network issue i am not able to find where we are.")
                pass

# to check a instagram profile
        
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please enter the user name correctly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            # time.sleep(2)
            speak("sir would you like to download profile picture of this account.")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder. now i am ready for next command")
            else:
                pass

# take screenshot

        elif "take screenshot" in query or "screenshot" in query:
            speak("sir, please tell me the name")
            name = takeCommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")

# read pdf

        elif "read pdf" in query or "pdf" in query:
            pdf_reader()

# hide files and folder

        elif "hide all files" in query or "hide" in query:
            speak("sir please tell me you want to hide this folder")
            condition = takeCommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("sir, all the files in this folder are now hidden.")
        
        elif "visible all files" in query or "visible" in query:
            condition = takeCommand().lower()
            if "visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir, all the files in this folder are now visible to everyone.")

        elif "leave it" in query or "leave" in query:
            speak("ok sir!")

# calculator

        elif "can you calculate" in query or "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Say what you want to calculate, example: 2 plus 2")
                print("listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    "+" : operator.add,
                    "-" : operator.sub,
                    "*" : operator.mul,
                    "divided" : operator.__truediv__,
                    }[op]
            def eval_binary_expr(op1,oper,op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1,op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))
            
            speak("thanks for using me sir, have a good day.")
            sys.exit()

# talk

        elif "i love you" in query or "love" in query:
            speak("it's hard to understand")

        elif "how are you" in query:
            speak("i'm fine, glad you me that")
            speak("what about you sir?")
        
        elif "fine" in query or "good" in query:
            speak("it's good to know that you are fine")

        elif "what is your name" in query:
            speak("my friends call me assistant")

        elif "exit" in query:
            speak("thanks for giving me your time")
            exit()

        elif "who made you" in query:
            speak("i have been created by internet")

        elif "who i am" in query:
            speak("if you talk then definately you are human.")

        elif "who are you" in query:
            speak("i am your desktop assistant.")

        elif "will you be my gf" in query or "will you be my bf" in query or "gf" in query:
            speak("i'm not sure about, may be you should give me some time")

        elif "good morning" in query or "morning" in query:
            speak(" a warm " +query)

        elif "no thanks" in query or "thanks" in query:
            speak("thanks for using me sir, have a great day.")
            sys.exit()

        speak("sir, do you have any other work")

