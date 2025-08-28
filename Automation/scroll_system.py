import pyautogui

# Functions for scrolling actions
def scroll_up():
    pyautogui.scroll(500)  # Scroll up by 500 units

def scroll_down():
    pyautogui.scroll(-500)  # Scroll down by 500 units

def scroll_to_top():
    pyautogui.hotkey('home')  # Scroll to the top of the page

def scroll_to_bottom():
    pyautogui.hotkey('end')  # Scroll to the bottom of the page

# Function to perform scrolling based on input text
def perform_scroll_action(text):
    if text == "scroll up":
        scroll_up()
    elif text == "scroll down":
        scroll_down()
    elif text == "scroll to top":
        scroll_to_top()
    elif text == "scroll to bottom":
        scroll_to_bottom()
    else:
        pass


