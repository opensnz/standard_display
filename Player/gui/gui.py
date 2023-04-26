import tkinter as tk
import vlc
import screeninfo
import threading
from guiPlayer import GuiPlayerClass
from guiClient import GuiClientClass

def get_primary_monitor() -> screeninfo.Monitor:
    monitors = screeninfo.get_monitors()
    for monitor in monitors:
        if monitor.is_primary == True:
            return monitor
    return screeninfo.Monitor(0,0,0,0)





########################################################################        
    

video1 = r"C:/Users/Dev1/Desktop/standard_display/Player/frontend/gui/video1.mp4"
video2 = r"C:/Users/Dev1/Desktop/standard_display/Player/frontend/gui/video2.mp4"




if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("600x400+0+0")
    #root.attributes('-fullscreen', True)
    guiPlayer = GuiPlayerClass(root)
    monitor : screeninfo.Monitor = get_primary_monitor()
    guiPlayer.place(x=0, y=0, width=monitor.width/4, height=monitor.height/4)
    #guiPlayer.play_media_list([video2, video1])
    # screen.play_media(video1)
    # screen.play_media(video2)
    guiClient = GuiClientClass(guiPlayer)
    guiClient.run()
    root.mainloop()