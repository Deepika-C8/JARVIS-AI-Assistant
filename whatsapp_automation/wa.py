import pywhatkit
import datetime
import time
from Texttospeech.Fast_TTS import speak

# Contact list
contacts = {
    "amma": "+919502680693",
    "nanna": "+919581085584",
    "karthik": "+919154607968",
    "geetha": "+917989607410",
    "tejuroy": "+917981872898",
    "shangri": "+918309457797",
    "tehbhai": "+919515830648",
    "jaanu": "+919030326640",
    "krishna": "+919063236776"
}

def send_msg_wa():
    speak("Whom do you want to message, Deepu??")
    output_text = ""

    while True:
        with open("input.txt", "r") as file:
            input_text = file.read().lower()

        if input_text != output_text:
            output_text = input_text

            for name, number in contacts.items():
                if name in output_text:  # Check if contact name is mentioned
                    speak(f"What do you want to send to {name}?")
                    
                    while True:
                        with open("input.txt", "r") as file:
                            input_text = file.read().lower()
                            
                        if input_text != output_text:
                            output_text = input_text
                            
                            if output_text.startswith("the text is"):
                                message = output_text.replace("the text is", "")

                                # Get the current time dynamically
                                now = datetime.datetime.now()
                                hour = now.hour
                                minute = now.minute + 2  # Message after 2 mins

                                # Handle overflow
                                if minute >= 60:
                                    minute %= 60
                                    hour = (hour + 1) % 24

                                pywhatkit.sendwhatmsg(number, message, hour, minute)
                                print(f"Carrier owl just took off for {name}, Deepu!")
                                speak(f"Carrier owl just took off for {name}, Deepu!")

                                # Wait to avoid sending messages too quickly
                                time.sleep(60)  # Prevents spam issues
                                return  # Exit after sending one message
