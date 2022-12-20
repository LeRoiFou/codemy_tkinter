"""
Titre : Modern Labels and Buttons - Tkinter TTKBootstrap 2
Lien : https://www.youtube.com/watch?v=fZtUNHw02R0

Premiers widgets 😎

Date : 20-12-22
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Labels and Buttons!")
        root.geometry('500x350')
        root.resizable(False, False)
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Colors :
        # Default, primary, secondary, success, info, warning, danger,
        # light, dark
        
        # Create a label
        self.my_label = tb.Label(
            text="Hello World!", font='Helvetica 20', 
            bootstyle=(PRIMARY, INVERSE))
        self.my_label.pack(pady=50)
        
        # Create a button
        my_button = tb.Button(
            text="Click Me!", bootstyle=(DANGER, OUTLINE), command=self.changer)
        my_button.pack(pady=20)
        
        self.counter = 0

    def changer(self):
        
        self.counter += 1
        if self.counter % 2 == 0:
            self.my_label.config(text="Hello World!")
        else:
            self.my_label.config(text="Goodbye World!")
        
    
if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    