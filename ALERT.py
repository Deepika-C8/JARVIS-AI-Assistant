import os
from winotify import Notification, audio
from os import getcwd

def Alert(text):
    icon_path = r"C:\Users\karth\OneDrive\Desktop\Jarvis\logo.png"

    toast = Notification(
    app_id="🫂👋J.A.R.V.I.S🟢",
    title=text,
    duration="long",
    icon=icon_path
    )

    toast.set_audio(audio.Default, loop=False)

    toast.add_actions(label="Click me", launch="https://www.google.com")
    toast.add_actions(label="Dismiss", launch="https://www.google.com")

    toast.show()



