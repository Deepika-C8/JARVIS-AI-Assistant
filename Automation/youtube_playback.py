import pyautogui

# Functions for YouTube automation
def play_pause():
    pyautogui.press('space')

def mute_unmute():
    pyautogui.press('m')

def volume_up():
    pyautogui.hotkey('shift', 'up')

def volume_down():
    pyautogui.hotkey('shift', 'down')

def skip_forward():
    pyautogui.press('l')

def skip_backward():
    pyautogui.press('j')

def full_screen():
    pyautogui.press('f')

def theater_mode():
    pyautogui.press('t')

def open_settings_menu():
    pyautogui.hotkey('shift', '?')

def next_video():
    pyautogui.hotkey('shift', 'n')

def previous_video():
    pyautogui.hotkey('shift', 'p')

def captions_on_off():
    pyautogui.press('c')

def mini_player():
    pyautogui.press('i')

def seek_to_start():
    pyautogui.press('0')

def seek_to_specific_time(time_in_seconds):
    pyautogui.typewrite(str(time_in_seconds))
    pyautogui.press('enter')

# Function to perform YouTube automation based on input text
def perform_youtube_operation(text):
    if "play" in text or "pause" in text or "stop" in text:
        play_pause()
    elif "mute" in text or "unmute" in text:
        mute_unmute()
    elif "volume up" in text:
        volume_up()
    elif "volume down" in text:
        volume_down()
    elif "skip forward" in text:
        skip_forward()
    elif "skip backward" in text:
        skip_backward()
    elif "full screen" in text:
        full_screen()
    elif "theater mode" in text:
        theater_mode()
    elif "open settings menu" in text:
        open_settings_menu()
    elif "next video" in text:
        next_video()
    elif "previous video" in text:
        previous_video()
    elif "captions on off" in text:
        captions_on_off()
    elif "mini player" in text:
        mini_player()
    elif "seek to start" in text:
        seek_to_start()
    elif "seek to" in text:
        try:
            time_in_seconds = int(text.split("seek to ")[1])
            seek_to_specific_time(time_in_seconds)
        except ValueError:
            print("Invalid time format. Please provide seconds.")
    else:
        pass


