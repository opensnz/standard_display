import tkinter as tk
from PIL import Image, ImageTk
import urllib.request
import os

class GuiWelcomeClass(tk.Frame):
    def __init__(self, root : tk.Tk, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root 
        self.fullScreenState = False
        self.root.bind("<F11>", self.toggleFullScreen)
        self.root.bind("<Escape>", self.quitFullScreen)

        self.image = Image.open(os.environ["GUI_DIR"]+"media/icon.jpg")
        self.image = self.image.resize((50, 50))
        self.photo = ImageTk.PhotoImage(self.image)
        
        self.center_frame = tk.Frame(self.root)
        self.center_frame.pack(expand=True)

        self.image_label = tk.Label(self.center_frame, image=self.photo)
        self.image_label.pack(side=tk.LEFT, padx=10)
        
        self.title_label = tk.Label(self.center_frame, text="OpenSignage", font=("Arial", 15, 'bold'))
        self.title_label.pack(side=tk.LEFT, padx=10)

        self.label2 = tk.Label(self.root, text="", font=("Arial", 20, 'bold'))
        self.label2.place(relx=0.5, rely=0.5, anchor='center')
        
        self.label3_text = tk.StringVar()
        self.label3 = tk.Label(self.root, textvariable=self.label3_text, font=("Arial", 15, 'bold'))
        self.label3.place(relx=0.5, rely=0.9, anchor='center')
        
        self.display_network_state(self.check_internet())
        
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.root.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.root.attributes("-fullscreen", False)
        
    def display_network_state(self, state:bool):
        if state :
            self.label2.config(text="Réseau connecté", font=("Arial", 18, 'bold'), foreground='green') 
            self.label2.pack(fill=tk.BOTH, expand=True)
        else:
            self.label2.config(text="Réseau non connecté", font=("Arial", 18, 'bold'), foreground='red')
            
            self.label3_text.set("Veuillez-vous connecter à Internet")

    def display_passcode(self, passcode:int):
        self.label2.config(text="Allez sur la plateforme et utilisez le code ci-dessous pour ajouter cet écran",
                           font=("Arial", 15), foreground='black') 
        self.label2.place(relx=0.5, rely=0.4, anchor='center')
        self.label3_text.set(str(passcode))
        self.label3.place(relx=0.5, rely=0.5, anchor='center')
        
    def display_activation(self):
        self.label2.config(text="Cet écran a été bien ajouté. Diffusion des contenus en cours",
                           font=("Arial", 15), foreground='black') 
        self.label2.place(relx=0.5, rely=0.4, anchor='center')
        
        self.label3_text.set("Synchronisation")
        self.label3.place(relx=0.5, rely=0.5, anchor='center') 
    def check_internet(self):
        try :
            urllib.request.urlopen('https://www.google.com', timeout=1)
            return True
        except :
            return False
    
    def destroy(self) -> None:
        self.center_frame.destroy()
        self.label2.destroy()
        self.label3.destroy()
        return super().destroy()   
        





