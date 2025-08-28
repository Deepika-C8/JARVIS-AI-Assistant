import pywhatkit

def play_on_yt(song_name):
    try:
       pywhatkit.playonyt(song_name)
    except Exception as e:
        print(e)



