import threading
from Internet_check import is_Online
from ALERT import Alert
from Data.DLG_data import offline_dlg,online_dlg
import random
from co_brain import Jarvis
from Texttospeech.Fast_TTS import speak
from Automation.battery import check_plug
from Time_operations.Brain import input_manage
from Time_operations.throw_alert import check_schedule,check_alarm

file_path = r'A:\Jarvis\schedule.txt'
alarm_path = r'A:\Jarvis\Alarm_data.txt'

ran_online_dlg = random.choice(online_dlg)          
ran_offline_dlg = random.choice(offline_dlg)

def wish():
   t1 = threading.Thread(target=speak,args=(ran_online_dlg,))
   t2 = threading.Thread(target=Alert,args=(ran_online_dlg,))
   t1.start()
   t2.start()
   t1.join()
   t2.join()
   

def main():
      print("hello")
      if is_Online():
        wish()
        t3 = threading.Thread(target=check_plug)
        t4 = threading.Thread(target=check_schedule,args=(file_path,))
        t5 = threading.Thread(target=Jarvis)
        t6 = threading.Thread(target=check_alarm,args=(alarm_path,))
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
      else:
        Alert(ran_offline_dlg)
main() 