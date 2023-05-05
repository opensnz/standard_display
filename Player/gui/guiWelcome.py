# import tkinter as tk
# from PIL import Image, ImageTk
# import urllib.request


# class GuiWelcomeClass(tk.Frame):
#     def __init__(self, root : tk.Tk, *args, **kwargs):
#         tk.Frame.__init__(self, root)
#         self.root = root
#         self.root.attributes('-fullscreen', True)  
#         self.fullScreenState = False
#         self.root.bind("<F11>", self.toggleFullScreen)
#         self.root.bind("<Escape>", self.quitFullScreen)

        
#         # image = Image.open("C:/Users/Dev1/tkinter/icon.jpg  ")
#         # image = image.resize((50, 50))
#         # self.photo = ImageTk.PhotoImage(image)
          
#         # self.image_label = tk.Label(self.root, image=self.photo)
#         # self.image_label.place(x=900, y=100)

#         # self.title_label = tk.Label(self.root, text="OpenSignage", font=("Arial", 20, 'bold'))
#         # self.title_label.place(relx=0.5, rely=0.5, anchor="center")
#         # #self.title_label.place(x=40, y=10,relx=0.1, rely=0.4)
        
#         # self.label2 = tk.Label(self.root, text="", font=("Arial", 20, 'bold'))
#         # self.label2.place(x=960, y=350)
        
#         # self.label3 = tk.Label(self.root, textvariable="", font=("Arial", 20, 'bold'))
#         # self.label3.place(x=960, y=600)
        
#         # self.display_network_state(self.check_internet())
        
#         ########################################
        
        
#         # définir des colonnes et des rangées pour la fenêtre
#         self.root.columnconfigure(0, weight=1)
#         self.root.columnconfigure(1, weight=1)
#         self.root.columnconfigure(2, weight=1)
#         self.root.rowconfigure(0, weight=1)
#         self.root.rowconfigure(1, weight=1)
#         self.root.rowconfigure(2, weight=1)

#         image = Image.open("C:/Users/Dev1/tkinter/icon.jpg  ")
#         image = image.resize((50, 50))
#         self.photo = ImageTk.PhotoImage(image)

#         self.image_label = tk.Label(self.root, image=self.photo)
#         self.image_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")

#         self.title_label = tk.Label(self.root, text="OpenSignage", font=("Arial", 20, 'bold'))
#         self.title_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

#         self.label2 = tk.Label(self.root, text="", font=("Arial", 20, 'bold'))
#         self.label2.grid(row=1, column=1, padx=10, pady=10)

#         self.label3 = tk.Label(self.root, textvariable="", font=("Arial", 20, 'bold'))
#         self.label3.grid(row=2, column=1, padx=10, pady=10)

#         self.display_network_state(self.check_internet())

#     def toggleFullScreen(self, event):
#         self.fullScreenState = not self.fullScreenState
#         self.root.attributes("-fullscreen", self.fullScreenState)

#     def quitFullScreen(self, event):
#         self.fullScreenState = False
#         self.root.attributes("-fullscreen", False)
        
#     def display_network_state(self, state:bool):
#         if state :
#             self.label2.config(text="Réseau connecté", font=("Arial", 15, 'bold'), foreground='green')  
#         else:
#             self.label2.config(text="Réseau non connecté", font=("Arial", 15, 'bold'), foreground='red') 
#             self.label3.config(text="Veuillez-vous connecter à Internet", font=("Arial", 15, 'bold'), foreground='black') 

#     def display_passcode(self, passcode:int):
#         self.label2.config(text="Allez sur la plateforme et utilisez le code ci-dessous pour ajouter cet écran",
#                            font=("Arial", 18), foreground='black') 
#         self.label2.place(x=600, y=350)
#         self.label3.config(text=str(passcode), font=("Arial", 20, 'bold'), foreground='black') 
    
#     def check_internet(self):
#         try :
#             urllib.request.urlopen('https://www.google.com', timeout=1)
#             return True
#         except :
#             return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# import tkinter as tk
# from PIL import Image, ImageTk
# import urllib.request


# class GuiWelcomeClass(tk.Frame):
#     def __init__(self, root : tk.Tk, *args, **kwargs):
#         tk.Frame.__init__(self, root)
#         self.root = root
#         self.root.attributes('-fullscreen', True)  
#         self.fullScreenState = False
#         self.root.bind("<F11>", self.toggleFullScreen)
#         self.root.bind("<Escape>", self.quitFullScreen)

#         self.image = Image.open("C:/Users/Dev1/tkinter/icon.jpg")
#         self.image = self.image.resize((50, 50))
#         self.photo = ImageTk.PhotoImage(self.image)
#         self.image_label = tk.Label(self.root, image=self.photo)
#         self.image_label.place(relx=0.40, rely=0.1, anchor='center')

#         self.title_label = tk.Label(self.root, text="OpenSignage", font=("Arial", 20, 'bold'))
#         self.title_label.place(relx=0.5, rely=0.1, anchor='center')
        
#         self.label2 = tk.Label(self.root, text="", font=("Arial", 20, 'bold'))
#         self.label2.place(relx=0.5, rely=0.5, anchor='center')
        
#         self.label3_text = tk.StringVar()
#         self.label3 = tk.Label(self.root, textvariable=self.label3_text, font=("Arial", 20, 'bold'))
#         self.label3.place(relx=0.5, rely=0.9, anchor='center')
        
#         self.display_network_state(self.check_internet())

#     def toggleFullScreen(self, event):
#         self.fullScreenState = not self.fullScreenState
#         self.root.attributes("-fullscreen", self.fullScreenState)

#     def quitFullScreen(self, event):
#         self.fullScreenState = False
#         self.root.attributes("-fullscreen", False)
        
#     def display_network_state(self, state:bool):
#         if state :
#             self.label2.config(text="Réseau connecté", font=("Arial", 15, 'bold'), foreground='green')  
#         else:
#             self.label2.config(text="Réseau non connecté", font=("Arial", 15, 'bold'), foreground='red') 
#             self.label3_text.set("Veuillez-vous connecter à Internet")

#     def display_passcode(self, passcode:int):
#         self.label2.config(text="Allez sur la plateforme et utilisez le code ci-dessous pour ajouter cet écran",
#                            font=("Arial", 18), foreground='black') 
#         self.label2.place(relx=0.5, rely=0.4, anchor='center')
#         self.label3_text.set(str(passcode))
#         self.label3.place(relx=0.5, rely=0.5, anchor='center')
    
#     def check_internet(self):
#         try :
#             urllib.request.urlopen('https://www.google.com', timeout=1)
#             return True
#         except :
#             return False
        
# root = tk.Tk()
# app = GuiWelcomeClass(root)
# app.pack(fill='both', expand=True)
# root.mainloop()







# import tkinter as tk
# from PIL import ImageTk, Image
# import urllib.request

# class GuiWelcomeClass(tk.Frame):
#     def __init__(self, root: tk.Tk, *args, **kwargs):
#         tk.Frame.__init__(self, root)
#         self.root = root
#         self.root.attributes('-fullscreen', True)  
#         self.fullScreenState = False
#         self.root.bind("<F11>", self.toggleFullScreen)
#         self.root.bind("<Escape>", self.quitFullScreen)

#         self.image = Image.open("C:/Users/Dev1/tkinter/icon.jpg")
#         self.image = self.image.resize((50, 50))
#         self.photo = ImageTk.PhotoImage(self.image)
#         self.image_label = tk.Label(self.root, image=self.photo)
#         self.image_label.place(relx=0.4, rely=0.1, anchor='w')

#         self.title_label = tk.Label(self.root, text="OpenSignage", font=("Arial", 20, 'bold'))
#         self.title_label.place(relx=0.5, rely=0.1, anchor='n')
        
#         self.label2 = tk.Label(self.root, text="", font=("Arial", 20, 'bold'))
#         self.label2.place(relx=0.5, rely=0.5, anchor='center')
        
#         self.label3_text = tk.StringVar()
#         self.label3 = tk.Label(self.root, textvariable=self.label3_text, font=("Arial", 20, 'bold'))
#         self.label3.place(relx=0.5, rely=0.9, anchor='s')
        
#         self.display_network_state(self.check_internet())

       
#         self.root.bind("<Configure>", self.on_resize)

#     def on_resize(self, event):
       
#         width = event.width
#         height = event.height

       
#         self.title_label.place(relx=0.5, rely=0.15, anchor='n')
#         self.image_label.place(relx=0.40, rely=0.1, anchor='w')

#         self.label2.place(relx=0.5, rely=0.5, anchor='center')
#         self.label3.place(relx=0.5, rely=0.9, anchor='s')

#     def toggleFullScreen(self, event):
#         self.fullScreenState = not self.fullScreenState
#         self.root.attributes("-fullscreen", self.fullScreenState)

#     def quitFullScreen(self, event):
#         self.fullScreenState = False
#         self.root.attributes("-fullscreen", False)
        
#     def display_network_state(self, state:bool):
#         if state :
#             self.label2.config(text="Réseau connecté", font=("Arial", 15, 'bold'), foreground='green')  
#         else:
#             self.label2.config(text="Réseau non connecté", font=("Arial", 15, 'bold'), foreground='red') 
#             self.label3_text.set("Veuillez-vous connecter à Internet")

#     def display_passcode(self, passcode:int):
#         self.label2.config(text="Allez sur la plateforme et utilisez le code ci-dessous pour ajouter cet écran",
#                            font=("Arial", 18), foreground='black') 
#         self.label2.place(relx=0.5, rely=0.4, anchor='center')
#         self.label3_text.set(str(passcode))
#         self.label3.place(relx=0.5, rely=0.5, anchor='center')
    
#     def check_internet(self):
#         try :
#             urllib.request.urlopen('https://www.google.com', timeout=1)
#             return True
#         except :
#             return False
        
# root = tk.Tk()
# app = GuiWelcomeClass(root)
# app.pack(fill='both', expand=True)
# root.mainloop()




import tkinter as tk
from PIL import ImageTk, Image
import urllib.request


class GuiWelcomeClass(tk.Frame):
    def __init__(self, root : tk.Tk, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root 
        self.fullScreenState = False
        self.root.bind("<F11>", self.toggleFullScreen)
        self.root.bind("<Escape>", self.quitFullScreen)

        self.image = Image.open("C:/Users/Dev1/tkinter/icon.jpg")
        self.image = self.image.resize((50, 50))
        self.photo = ImageTk.PhotoImage(self.image)

        
        self.center_frame = tk.Frame(self.root)
        self.center_frame.pack(expand=True)

        self.image_label = tk.Label(self.center_frame, image=self.photo)
        self.image_label.pack(side=tk.LEFT, padx=10)
        #self.image_label.pack(pady=10, padx=10, anchor=tk.N, side=tk.TOP)
        
        self.title_label = tk.Label(self.center_frame, text="OpenSignage", font=("Arial", 15, 'bold'))
        self.title_label.pack(side=tk.LEFT, padx=10)
        #self.title_label .pack(pady=10, padx=10, anchor=tk.N, side=tk.TOP)

        
        
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
        





