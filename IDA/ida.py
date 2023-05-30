import ctypes
import webbrowser
import PyPDF2
import cv2
import psutil
import pywhatkit as kit
import pyttsx3
import speedtest
import winshell
from pywikihow import search_wikihow
from IDA import IdaAssistant
import re
import os
import random
import pprint
import datetime
import requests
from requests import get
import sys
import pyjokes
import time
import pyautogui
import pywhatkit
import wolframalpha
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from IDA.config import config
from UI.ui_ida import Ui_IdaWindow


engine = pyttsx3.init('sapi5')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('volume', 300)
engine.setProperty('rate', 180)

# text-to-speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

obj = IdaAssistant()

# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello, hello ida", "ida", "wake up ida", "you there ida", "time to work ida", "hey ida",
             "ok ida", "are you there, baby"]
GREETINGS_RES = ["always there for you ma'am", "i am ready ma'am",
                 "your wish my command", "how can i help you ma'am?", "i am online and ready ma'am"]

EMAIL_DIC = {
    'myself': 'shaund.souza@yahoo.com',
    'my official email': 'riyamourya2017@gmail.com',
    'my second email': 'riyamourya2017@gmail.com',
    'my official mail': 'riyamymourya2017@gmail.com',
    'my second mail': 'riyamourya2017@gmail.com'
}

CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]


# =======================================================================================================================================================


def speak(text):
    obj.tts(text)

app_id = '2JK5R7-G9Q9E5LTXK'

def pdf_reader():
    book = open('AWT and Event Handling.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in the book {pages}")
    speak("ma'am please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry ma'am I couldn't fetch your question's answer. Please try again ")
        return None


def startup():
    speak("Initializing Ida")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Calibrating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment ma'am")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning Ma'am")
    elif hour > 12 and hour < 18:
        speak("Good afternoon Ma'am")
    else:
        speak("Good evening Ma'am")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am Ida. Online and ready ma'am. Please tell me how may I help you")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        #startup()
        wish()
        while True:
            if 1:
                command = obj.mic_input()

                if re.search('date', command):
                    date = obj.tell_me_date()
                    print(date)
                    speak(date)

                elif "time" in command:
                    time_c = obj.tell_time()
                    print(time_c)
                    speak(f"ma'am the time is {time_c}")

                elif "alarm" in command:
                    speak("okay ma'am, please tell me the time to set alarm, for example, set alarm to 5:30 a.m.")
                    tt = obj.mic_input()
                    tt = tt.replace("set alarm to", "")
                    tt = tt.replace(".", "")
                    tt = tt.upper()
                    from IDA.features import MyAlarm
                    MyAlarm.alarm(tt)

                elif re.search('launch', command):
                    npath = "C:\\Program Files\\Notepad++\\notepad++.exe"
                    dict_app = {
                        'chrome': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
                        #'command prompt': os.system("start cmd"),
                        'powerpoint': 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe',
                        #'notepad': os.startfile(npath)
                    }

                    app = command.split(' ', 1)[1]
                    path = dict_app.get(app)

                    if path is None:
                        speak('Application path not found')
                        print('Application path not found')

                    else:
                        speak("Launching: " + app + "for you ma'am!")
                        obj.launch_any_app(path_of_app=path)

                elif command in GREETINGS:
                    speak(random.choice(GREETINGS_RES))

                elif "click" in command:
                    speak("ok ma'am, camera is right here")
                    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(50)
                        if k == 10:
                            break
                    cap.release()
                    cv2.destroyAllWindows()

                elif re.search('open', command):
                    domain = command.split(' ')[-1]
                    open_result = obj.website_opener(domain)
                    speak(f"Alright ma'am !! Opening {domain}")
                    print(open_result)

                elif re.search('weather', command):
                    city = command.split(' ')[-1]
                    weather_res = obj.weather(city=city)
                    print(weather_res)
                    speak(weather_res)

                elif re.search('tell me about', command):
                    topic = command.split(' ')[-1]
                    if topic:
                        wiki_res = obj.tell_me(topic)
                        print(wiki_res)
                        speak(wiki_res)
                    else:
                        speak(
                            "Sorry ma'am. I couldn't load your query from my database. Please try again")

                elif "buzzing" in command or "news" in command or "headlines" in command:
                    news_res = obj.news()
                    speak('Source: The Times Of India')
                    speak('Todays Headlines are..')
                    for index, articles in enumerate(news_res):
                        pprint.pprint(articles['title'])
                        speak(articles['title'])
                        if index == len(news_res) - 2:
                            break
                    speak("These were the top headlines, Have a nice day Ma'am!!..")

                elif "volume up" in command or "increase" in command:

                    pyautogui.press("volumeup")

                elif "volume down" in command or "decrease" in command:
                    pyautogui.press("volumedown")

                elif "volume mute" in command or "mute" in command:
                    pyautogui.press("volumemute")

                elif "search in google" in command:
                    speak("Ma'am, what should i search on google")
                    cm = obj.mic_input().lower()
                    webbrowser.open(f"https://www.google.com/search?q={cm}")

                elif "play music" in command or "hit some music" in command:
                    speak("Which song should i play, tell me your mood")
                    wmtp = obj.mic_input()
                    if "sad" in wmtp:
                        speak("playing sad songs")
                        music_dir = "C:\\Users\\riyam\\Music\\Sad\\"
                        songs = os.listdir(music_dir)
                        rd = random.choice(songs)
                        for song in songs:
                            if song.endswith('.mp3'):
                                os.startfile(os.path.join(music_dir, rd))
                    elif "happy" in wmtp:
                        speak("playing happy songs")
                        music_dir = "C:\\Users\\riyam\\Music\\Happy\\"
                        songs = os.listdir(music_dir)
                        rd = random.choice(songs)
                        for song in songs:
                            if song.endswith('.mp3'):
                                os.startfile(os.path.join(music_dir, rd))

                    elif "angry" in wmtp:
                        speak("playing angry songs")
                        music_dir = "C:\\Users\\riyam\\Music\\Angry\\"
                        songs = os.listdir(music_dir)
                        rd = random.choice(songs)
                        for song in songs:
                            if song.endswith('.mp3'):
                                os.startfile(os.path.join(music_dir, rd))

                    elif "relax" in wmtp:
                        speak("playing relax songs")
                        music_dir = "C:\\Users\\riyam\\Music\\Relax\\"
                        songs = os.listdir(music_dir)
                        rd = random.choice(songs)
                        for song in songs:
                            if song.endswith('.mp3'):
                                os.startfile(os.path.join(music_dir, rd))

                elif 'youtube' in command:
                    video = command.split(' ')[1]
                    speak(f"Okay ma'am, playing {video} on youtube")
                    pywhatkit.playonyt(video)

                elif "recycle bin" in command:
                    winshell.recycle_bin().empty(
                        confirm=True, show_progress=True, sound=True
                    )
                    speak("recycle bin emptied")

                elif "email" in command or "send email" in command:
                    sender_email = config.email
                    sender_password = config.email_password

                    try:
                        speak("Whom do you want to email ma'am ?")
                        recipient = input()
                        receiver_email = EMAIL_DIC.get(recipient)
                        if receiver_email:

                            speak("What is the subject ma'am ?")
                            subject = obj.mic_input()
                            speak("What should I say?")
                            message = obj.mic_input()
                            msg = 'Subject: {}\n\n{}'.format(subject, message)
                            obj.send_mail(sender_email, sender_password,
                                          receiver_email, msg)
                            speak("Email has been successfully sent")
                            time.sleep(2)

                        else:
                            speak(
                                "I coudn't find the requested person's email in my database. Please try again with a different name")

                    except:
                        speak("Sorry ma'am. Couldn't send your mail. Please try again")

                elif "calculate" in command:
                    question = command
                    answer = computational_intelligence(question)
                    speak(answer)



                elif "what is" in command or "who is" in command:
                    question = command
                    answer = computational_intelligence(question)
                    speak(answer)

                #elif "what do i have" in command or "do i have plans" or "am i busy" in command:
                 #   obj.google_calendar_events(command)

                elif "make a note" in command or "write this down" in command or "remember this" in command:
                    speak("What do you want me to write down")
                    note_text = input()
                    obj.take_note(note_text)
                    speak("I've made a note of that")

                elif "close the note" in command or "close notepad" in command:
                    speak("Okay ma'am, closing notepad")
                    os.system("taskkill /f /im notepad++.exe")

                elif "joke" in command:
                    joke = pyjokes.get_joke()
                    print(joke)
                    speak(joke)

                elif "system" in command:
                    sys_info = obj.system_info()
                    print(sys_info)
                    speak(sys_info)

                elif "where is" in command:
                    place = command.split('where is ', 1)[1]
                    current_loc, target_loc, distance = obj.location(place)
                    city = target_loc.get('city', '')
                    state = target_loc.get('state', '')
                    country = target_loc.get('country', '')
                    time.sleep(1)
                    try:

                        if city:
                            res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                            print(res)
                            speak(res)

                        else:
                            res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                            print(res)
                            speak(res)

                    except:
                        res = "Sorry ma'am, I couldn't get the co-ordinates of the location you requested. Please try again"
                        speak(res)




                elif "shut down the laptop" in command:
                    speak("shutting down the laptop ma'am")
                    os.system("shutdown /s /t 5")

                elif "restart the laptop" in command:
                    speak("restarting the laptop ma'am")
                    os.system("shutdown /r /t 5")

                elif "sleep the laptop" in command:
                    speak("laptop is going in a sleep mode ma'am")
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


                elif "switch the window" in command or "switch window" in command:
                    speak("Okay ma'am, Switching the window")
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")


                elif "where i am" in command or "current location" in command or "where am i" in command:
                   speak("ok maam, wait a second")
                   webbrowser.open('https://www.google.co.in/maps/@19.0514787,72.8869927,15z')

                elif "take screenshot" in command or "take a screenshot" in command or "capture the screen" in command:
                    speak("By what name do you want to save the screenshot?")
                    name = obj.mic_input()
                    speak("Alright ma'am, taking the screenshot")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    name = (f"{name}.png")
                    img.save(name)
                    speak("The screenshot has been succesfully captured")

                elif "show me the screenshot" in command:
                    try:
                        img = Image.open('C:\\Users\\riyam\\PycharmProjects\\MajorProject\\IDA\\' + name)
                        img.show(img)
                        speak("Here it is ma'am")
                        time.sleep(2)

                    except IOError:
                        speak("Sorry ma'am, I am unable to display the screenshot")

                elif "hide all files" in command or "hide this folder" in command:
                    os.system("attrib +s +h +r")
                    speak("Ma'am, all the files in this folder are now hidden")

                elif "visible" in command or "make files visible" in command:
                    os.system("attrib -s -h -r")
                    speak("Ma'am, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

                elif "internet speed" in command:
                    speak("sure ma'am, please wait i am checking the internet speed")
                    st = speedtest.SpeedTest
                    dl = st.download()
                    up = st.upload()
                    speak(f"ma'am we have{dl} bit per second downloading speed and {up} bit per second uploading speed")

                elif "how much power left" in command or "how much power we have" in command or "battery" in command:
                    battery = psutil.sensors_battery()
                    percentage = battery.percent
                    speak(f"ma'am our system have {percentage} percent battery")
                    if percentage >= 75:
                        speak("we have enough power to continue our work")
                    elif percentage >= 40 and percentage <= 75:
                        speak("we should connect system to charging point to charge our battery")
                    elif percentage <= 15 and percentage <= 30:
                        speak("we don't have enough power to work, please connect to charging")
                    elif percentage <= 15:
                        speak("we have very low power, please connect to charging the system will shutdown very soon")

                if "read pdf" in command:
                    pdf_reader()

                elif "hello" in command or "hey" in command:
                    speak("hello ma'am, may i help you with something.")

                elif "how are you" in command:
                    speak("i am fine ma'am, what about you.")

                elif 'change background' in command or "wallpaper" in command:
                    ctypes.windll.user32.SystemParametersInfoW(20, 0,
                                                               "C:\\Users\\riyam\\PycharmProjects\\MajorProject\\IDA\Background\\bg6.jpg",
                                                               0)
                    speak("Background changed succesfully")

                elif "i am also good" in command or "fine" in command or "i am fine" in command:
                    speak("that's great to hear from you.")

                elif "thank you" in command or "thanks" in command:
                    speak("it's my pleasure ma'am.")

                elif "goodbye" in command or "offline" in command or "bye" in command:
                    speak("Alright ma'am, going offline. It was nice working with you")
                    sys.exit()

                '''

                elif "ip address" or "ip" in command:
                    ip = requests.get("https://api.ipify.org").text
                    print({ip})
                    speak(f"Your IP address is {ip}")
                
                '''





startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_IdaWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_run.clicked.connect(self.startTask)
        self.ui.pushButton_exit.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\gif\\gui8-unscreen.gif")
        self.ui.label_codegif.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\gif\\source.gif")
        self.ui.label_sound.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\gif\\1_9I6EIL5NG20A8se5afVmOg.gif")
        self.ui.label_robot.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
ida = Main()
ida.show()
exit(app.exec_())
