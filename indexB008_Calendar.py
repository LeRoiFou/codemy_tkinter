"""
Titre : DateEntry Calendar Widget - Tkinter TTKBootstrap 8
Lien : https://www.youtube.com/watch?v=jACXHXaGLqQ



Date : 31-01-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap.dialogs import Querybox

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Calendar!")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_date = tb.DateEntry(
            root, bootstyle='danger', 
            startdate=date(2023, 2, 14), # Date par défaut du calendrier
            firstweekday=0 # affichage du lundi 1er jour de la semaine
            )
        self.my_date.pack(pady=50)
        
        my_button = tb.Button(
            root, text="Get Date", bootstyle='danger outline', command=self.datey)
        my_button.pack(pady=20)
        
        my_button2 = tb.Button(
            root, text="Get Calendar", bootstyle='success outline', 
            command=self.thing)
        my_button2.pack(pady=20)
        
        self.my_label=tb.Label(root, text='You picked:')
        self.my_label.pack(pady=20)
        
    def datey(self):
        
        # Grab the date
        self.my_label.config(text=f"You picked : {self.my_date.entry.get()}")
        
    def thing(self):
        "Récupération directement à partir d'un calendrier... pas fan 🙁"
        
        cal = Querybox()
        self.my_label.config(text=f"You picked : {cal.get_date()}")

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    