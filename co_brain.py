from Automation.Automation_brain import Auto_main_brain,clear_file
from NetHyTech_STT import listen
from Texttospeech.Fast_TTS import speak
import threading
from Automation.battery import battery_Alert
from Internet_check import is_Online
from ALERT import Alert
from Data.DLG_data import online_dlg,offline_dlg
from Time_operations.Brain import input_manage,input_manage_alarm
from Features.check_internet_speed import get_internet_speed
from BRAIN.brain import huggingfacemodel
from Features.create_file import create_File
from whatsapp_automation.wa import send_msg_wa
from Device_info.info import get_info


numbers = ["1:","2:","3:","4:","5:","6:","7:","8:","9:"]

def check_inputs():
    output_text = ""
    while True:
        with open("input.txt","r") as file:
            input_text = file.read().lower()
        if input_text != output_text:
            output_text = input_text
            if output_text.startswith("tell me"):
                output_text = output_text.replace(" a.m.","AM")
                output_text = output_text.replace(" p.m.","PM")
                if "11:" in output_text or"10:" in output_text or "12:" in output_text:
                    input_manage(output_text)
                    clear_file()
                else:
                    for number in numbers:
                        if number in output_text:
                           output_text = output_text.replace(number,f"0{number}")
                           input_manage(output_text)
                           clear_file()
            elif output_text.startswith("set alarm"):
                output_text = output_text.replace(" a.m.","AM")
                output_text = output_text.replace(" p.m.","PM")
                if "11:" in output_text or"10:" in output_text or "12:" in output_text:
                    input_manage_alarm(output_text)
                    clear_file()
                else:
                    for number in numbers:
                        if number in output_text:
                           output_text = output_text.replace(number,f"0{number}")
                           input_manage_alarm(output_text)
                           clear_file()
            elif "check internet speed" in output_text:
                speak("  checking  internet speed")
                speed = get_internet_speed()
                speak(f"  Deepu it is {speed} MBPS")
            elif output_text.startswith("create"):
                if "file" in output_text:
                    create_File(output_text)
                speak("Deepu the file has been created")
            elif "send message on whatsapp" in output_text:
                send_msg_wa()
            elif "jarvis" in output_text:
                response = huggingfacemodel(output_text)
                print(response)
                speak(response)
            else:
                Auto_main_brain(output_text)
                get_info(output_text)
                

def Jarvis():
    clear_file()
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=check_inputs)
    t1.start()
    t2.start()
    t1.join()
    t2.join()



