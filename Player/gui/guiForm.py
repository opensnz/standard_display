import tkinter as tk
import threading
from tkinter import ttk
from typing import Tuple
from monitor import *
from constants import *
from typing import Dict



class GuiFormClass(tk.Frame):
    def __init__(self, root : tk.Tk, form:dict=None, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root
        self.inputs : Dict[ttk.Entry] = {}
        self.__form = form
        self.__callback_submit__ = None
        self.__callback_ok__ = None
        self.__callback_cancel__ = None
        self.__auto_cancel : threading.Timer = None
        # Apply a themed style with 'equilux' theme
        style = ttk.Style(self.root)
        style.theme_use('clam')
        # Set the background color for entry fields to white
        style.configure("TEntry", fieldbackground="white")
        
    def display_form(self, callback_submit:None):
        monitor = get_primary_monitor()
        self.__callback_submit__ = callback_submit
        self.place(x=0, y=0, width=monitor.width, height=monitor.height)
        parameters = {
            "row" : 1,
            "padx" : 20,
            "pady" : 20
        }
        label = ttk.Label(self, text="Veuillez remplir ce formulaire")
        label.grid(row=0, columnspan=2, padx=20, pady=20)
        for field in self.__form[TYPE.FORM]:
            parameters["text"] = field["label"]
            (label, entry) = self.__add_label_and_entry__(parameters)
            self.inputs[field["label"]] = entry
            parameters["row"] = parameters["row"] + 1
        parameters = {
            "text" : "Envoyer",
            "callback":self.__submit__,
            "row" : parameters["row"] + 1
        }
        self.__add_button__(parameters)
        self.lift()
        
    def display_confirm(self, callback_ok:None, callback_cancel:None):
        monitor = get_primary_monitor()
        self.__callback_ok__ = callback_ok
        self.__callback_cancel__ = callback_cancel
        
        self.place(x=3*monitor.width/8, y=3*monitor.height/8, width=monitor.width/4, height=monitor.height/4)
        self.label = ttk.Label(self, text="Notre produit vous intêresse-t-il ?")
        self.label.place(relx=0.5, rely=0.1, anchor='center')
        button_width1 = 10  
        button_height1 = 2 
        style_cancel = ttk.Style()
        style_cancel.configure("Cancel.TButton", foreground="white", background="red", font=('Helvetica', 12), width=button_width1, height=button_height1)
        self.button_cancel = ttk.Button(self, text="Cancel", command=self.__cancel__, style="Cancel.TButton")
        self.button_cancel.pack(side=tk.LEFT, padx=70)
        button_width = 10  
        button_height = 2  
        style_ok = ttk.Style()
        style_ok.configure("OK.TButton", foreground="white", background="blue", font=('Helvetica', 12), width=button_width, height=button_height)
        self.button_ok = ttk.Button(self, text="OK", command=self.__ok__, style="OK.TButton")
        self.button_ok.pack(side=tk.RIGHT, padx=70)
    

        self.lift()
        self.__auto_cancel = threading.Timer(15, self.__cancel__)
        self.__auto_cancel.start()
        
        
    def __submit__(self):
        if self.__callback_submit__ is not None:
            self.__callback_submit__()
        
    
    def __ok__(self):
        self.__auto_cancel.cancel()
        self.label.destroy()
        self.button_cancel.destroy()
        self.button_ok.destroy()
        if self.__callback_ok__ is not None:
            self.__callback_ok__()
    
    def __cancel__(self):
        if self.__callback_cancel__ is not None:
            self.__callback_cancel__()
    

    def __add_label_and_entry__(self, parameters: dict) -> Tuple[ttk.Label, ttk.Entry]:
        label = ttk.Label(self, text=parameters["text"])
        label.grid(row=parameters["row"], column=0, padx=parameters["padx"], pady=parameters["pady"], sticky="e")
        entry = ttk.Entry(self, style="Rounded.TEntry")
        entry.grid(row=parameters["row"], column=1, padx=parameters["padx"], pady=parameters["pady"], sticky="w")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        return (label, entry)

  
    def __add_button__(self, parameters:dict)->ttk.Button:
        # Create button
        button = ttk.Button(self, text=parameters["text"], command=parameters["callback"])
        button.grid(row=parameters["row"], columnspan=2, padx=10, pady=10)
        button.place(relx=0.5, rely=0.25, anchor='center')
        return button