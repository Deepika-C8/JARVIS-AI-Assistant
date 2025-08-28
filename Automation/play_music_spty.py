import webbrowser
import pyautogui as ui
import time


def play_music_on_spotify(song_name):
    webbrowser.open("https://open.spotify.com/")
    time.sleep(10)
    ui.leftClick(1000,200)
    time.sleep(6)
    ui.write(song_name)
    time.sleep(9)
    ui.leftClick(550,640)
    

