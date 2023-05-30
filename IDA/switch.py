import ctypes
import os
import sys
import random
import time
import webbrowser

import psutil
import pyautogui

import pyttsx3
import requests
import pyspeedtest
import self
import winshell
from PIL import Image
from pyjokes import pyjokes
from pywikihow import search_wikihow

from IDA import IdaAssistant

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
def speak(text):
    obj.tts(text)

command = obj.mic_input()

if "recycle bin" in command:
    winshell.recycle_bin().empty(
        confirm=True, show_progress=True, sound=True
    )
    speak("recycle bin emptied")