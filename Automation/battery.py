import psutil
import time
from Texttospeech.Fast_TTS import speak
import threading
from ALERT import Alert
        
battery = psutil.sensors_battery()

def battery_Alert():
    while True:
        time.sleep(3)
        percentage = int(battery.percent)
        if percentage == 100:
            t1 = threading.Thread(target=Alert,args=("100% charge",))
            t2 = threading.Thread(target=speak,args=("100% charged. Please unplug it.",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif percentage <= 20:
            t1 = threading.Thread(target=Alert,args=("Battery low",))
            t2 = threading.Thread(target=speak,args=("Deepu! sorry to distrub you but battery is low now,charge the device.",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif percentage <= 10:
            t1 = threading.Thread(target=Alert,args=("Battery low",))
            t2 = threading.Thread(target=speak,args=("Deepu! sorry to distrub you but we are running out of battery,charge the device now",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif percentage <= 5:
            t1 = threading.Thread(target=Alert,args=("Battery low",))
            t2 = threading.Thread(target=speak,args=("Deepu!!! now   you have to charge,battery is too low ",))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        time.sleep(10)



def check_plug():
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged
    while True:
        battery = psutil.sensors_battery() 
        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                t1 = threading.Thread(target=Alert,args=("plugged in",))
                t2 = threading.Thread(target=speak,args=("Deepu!!! charging started",))
                t1.start()
                t2.start()
                t1.join()
                t2.join()    
            else:
                t1 = threading.Thread(target=Alert,args=("unplugged",))
                t2 = threading.Thread(target=speak,args=("Deepu!!! charging is stopped",))
                t1.start()
                t2.start()
                t1.join()
                t2.join()
                       
            previous_state = battery.power_plugged

def check_percentage():
    battery = psutil.sensors_battery() 
    percent = int(battery.percent)
    t1 = threading.Thread(target=Alert,args=(f"Deepu, device is running on {percent}% power",))
    t2 = threading.Thread(target=speak,args=(f"Deepu, device is running on {percent}% power",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
