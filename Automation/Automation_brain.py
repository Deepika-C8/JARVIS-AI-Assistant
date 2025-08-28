from Automation.open_app import open_App
from Automation.WEB_open import openweb
import pyautogui as gui
from Automation.play_YT import play_on_yt
from Texttospeech import Fast_TTS    
from Automation.play_music_spty import play_music_on_spotify
from Automation.battery import check_percentage
import time
from Automation.tab_automation import perform_browser_operation
from Automation.youtube_playback import perform_youtube_operation
import pywhatkit
from Automation.scroll_system import perform_scroll_action
import threading
from Texttospeech.Fast_TTS import speak


def close():
    gui.hotkey('alt','f4')

def search(text):
    gui.press("/")
    time.sleep(0.5)
    gui.write(text)

def search_google(text):
    pywhatkit.search(text)

def Open_Brain(text):
    if "website" in text:
        text = text.replace("open","").strip()
        text = text.replace("website","").strip()
        text = text.replace("open website named","").strip()
        t1 = threading.Thread(target=speak,args=(f"yes Deepu!! navigating to {text} website",))
        t2 = threading.Thread(target=openweb,args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    else:
        text = text.replace("open","").strip()
        text = text.replace("app","").strip()
        t1 = threading.Thread(target=speak,args=(f"yes Deepu!! navigating to {text} application",))
        t2 = threading.Thread(target=open_App,args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

def clear_file():
    with open("input.txt","w") as file:
        file.truncate(0)

def Auto_main_brain(text):
    if text.startswith("open"):
        Open_Brain(text)
    elif "close" in text:
        close()
    elif "play on youtube" in text:
        Fast_TTS.speak("Deepuu what do you want me to play?:")
        clear_file()
        output_text = ""
        while True:
            with open("input.txt","r") as file:
                input_text = file.read().lower()
            if input_text != output_text:
                output_text = input_text
                if output_text:
                    play_on_yt(output_text)
                    break
            else:
                pass        
    elif "play music on spotify" in text:
        Fast_TTS.speak("Deepuu which song do you want me to play?:")
        output_text = ""
        while True:
            with open("input.txt","r") as file:
                input_text = file.read().lower()
            if input_text != output_text:
                output_text = input_text
                if output_text.endswith("song"):
                    play_music_on_spotify(output_text)
    elif "check battery percentage" in text or "current battery" in text:
        check_percentage()
    elif text.startswith("search"):
        text = text.replace("search","")
        text = text.strip()
        t1 = threading.Thread(target=speak,args=(f"yaa Deepu searching about {text} ",))
        t2 = threading.Thread(target=search,args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        time.sleep(0.5)
        gui.press("enter")
    elif "google about" in text:
        text = text.replace("google about","")
        t1 = threading.Thread(target=speak,args=(f"done Deepu googling about {text} ",))
        t2 = threading.Thread(target=search_google,args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        
    else:
        perform_browser_operation(text)
        perform_youtube_operation(text)
        perform_scroll_action(text)
        
    
