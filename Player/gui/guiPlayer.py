import vlc
import tkinter as tk
import threading
from sys import platform



class GuiPlaylistClass():
    
    def __init__(self, sources : list):
        self.sources = sources
        self.current = -1
    
    def next_source(self) -> str:
        self.current = self.current + 1
        if self.current > len(self.sources) - 1:
            self.current = 0
        return self.sources[self.current]


class GuiPlayerClass(tk.Frame):

    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, bg='black')
        self.root = root
        # Creating VLC player
        self.instance : vlc.Instance = vlc.Instance("--no-xlib")
        self.player : vlc.MediaPlayer = vlc.MediaPlayer()
        if platform == "linux" or platform == "linux2":
            from ctypes import CDLL
            from ctypes.util import find_library
            x11 = CDLL(find_library('X11'))
            x11.XInitThreads()
            self.player.set_xwindow(self.winfo_id())
        elif platform == "win32":
            self.player.set_hwnd(self.winfo_id())
        self.player_manager = self.player.event_manager()
        self.player_manager.event_attach(vlc.EventType.MediaPlayerStopped,
                self.callback_media_stopped, self.player)
        self.player_manager.event_attach(vlc.EventType.MediaPlayerPaused,
                self.callback_media_paused, self.player)
        self.player_manager.event_attach(vlc.EventType.MediaPlayerPlaying,
                self.callback_media_playing, self.player)
        self.player_manager.event_attach(vlc.EventType.MediaPlayerEndReached,
            self.callback_media_ended, self.player)
        self.media : vlc.Media = None
        self.playlist : GuiPlaylistClass = None
        self.is_playlist = False
        

    def get_frame_id(self):
        # Getting frame ID
        return self.winfo_id()
    
    def play_media(self, source : str):
        print("Play Media : ", source)
        self.media = vlc.Media(source)
        self.player.set_media(self.media)
        self.player.play()
        
    def pause_media_list(self):
        print("Pause Media List: ")
        self.player.pause()
        
    def replay_media_list(self):
        print("Replay Media List: ")
        self.player.pause()
     
    def play_media_list(self, sources : list):
        # Function to start player from given sources
        self.playlist = GuiPlaylistClass(sources)
        self.is_playlist = True
        self.play_media(self.playlist.next_source())
        
    def stop_playlist(self):
        self.player.stop()
        self.playlist = None
        self.is_playlist = False
        
    def callback_media_stopped(self, event : vlc.EventType, player : vlc.MediaPlayer):
        print("Media Stopped")
             
    def callback_media_paused(self, event : vlc.EventType, player : vlc.MediaPlayer):
        print("Media Paused")
        
    def callback_media_playing(self, event : vlc.EventType, player : vlc.MediaPlayer):
        print("Media Playing")
        
    def callback_media_ended(self, event : vlc.EventType, player : vlc.MediaPlayer):
        print("Media Ended")
        if self.is_playlist:
            next_source = self.playlist.next_source()
            threading.Timer(0, self.play_media, args=(next_source,)).start()