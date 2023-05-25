import tkinter as tk
import vlc

class Screen(tk.Frame):

    '''
    Screen widget: Embedded video player from local or youtube
    '''

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, bg='black')
        self.parent = parent
        # Creating VLC player
        self.instance = vlc.Instance()
        self.player : vlc.MediaPlayer = self.instance.media_player_new()

    def GetHandle(self):
        # Getting frame ID
        return self.winfo_id()

    def play(self, _source):
        # Function to start player from given source
        Media = self.instance.media_new(_source)
        Media.get_mrl()
        self.player.set_media(Media)

        self.player.set_xwindow(self.winfo_id())
        self.player.play()         

########################################################################        

def start (): 
    screen.play(url)

def pause (): 
    screen.player.pause()

def resume (): 
    screen.player.play()

def stop (): 
    screen.player.stop()

def close (): pass  

########################################################################        

url = r"./video1.mp4"    # changeable

root = tk.Tk()
root.geometry("600x600+100+100")
screen = Screen(root)
screen.place(x=0, y=0, width=600, height=400)
screen.play(url)

framed2 = tk.Frame(root)  

k = tk.Button(framed2, text='Play', command=start)
k.grid(row=0,column=1)

l = tk.Button(framed2, text='Pause', command=pause)
l.grid(row=0,column=2)

m = tk.Button(framed2, text='Stop', command=stop)
m.grid(row=0,column=3)

n = tk.Button(framed2, text='Quit', command=root.destroy)
n.grid(row=0,column=5)

framed2.pack(padx=5, pady=4)

root.mainloop()        

