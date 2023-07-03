import tkinter as tk
from monitor import *
from guiPlayer import GuiPlayerClass
from guiWelcome import GuiWelcomeClass
from guiClient import GuiClientClass
import os, json
from sys import platform


if platform == "linux" or platform == "linux2":
    os.environ["GUI_DIR"] = "/home/pi/standard_display/Player/gui/"
    os.environ["BACKEND_DIR"] = "/home/pi/standard_display/Player/backend/"
elif platform == "win32":
    os.environ["GUI_DIR"] = "C:/Users/Dev1/Desktop/standard_display/Player/gui/"
    os.environ["BACKEND_DIR"] = "C:/Users/Dev1/Desktop/standard_display/Player/backend/"


########################################################################


def is_player_activate() -> bool:
    path = os.getenv('BACKEND_DIR') + "config/player.json"
    if os.path.exists(path):
        try :
            with open(path, "r") as file:
                data = json.load(file)
                if data["player"]["uuid"] != "" and data["player"]["activated"] == True:
                    return True
            return False
        except:
            return False
    else :
        return False


########################################################################        
    

if __name__ == '__main__':
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    
    if is_player_activate() :
        guiPlayer = GuiPlayerClass(root)
        monitor : screeninfo.Monitor = get_primary_monitor()
        guiPlayer.place(x=0, y=0, width=monitor.width, height=monitor.height)
        guiClient = GuiClientClass(guiPlayer=guiPlayer)
    else :
        print("Welcome Page")
        guiWelcome = GuiWelcomeClass(root)
        guiClient = GuiClientClass(guiWelcome=guiWelcome)
        #root.bind("<Configure>", guiWelcome.resize_label)
        guiWelcome.pack(fill='both', expand=True)
    guiClient.run() 
    root.mainloop()