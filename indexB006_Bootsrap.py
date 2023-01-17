"""
Titre : Entry Widgets With TTKBootstrap - Tkinter TTKBootstrap 6
Lien : https://www.youtube.com/watch?v=6KRuZVXMnq8

Diverses fonctionnalités avec le widget Entry

Date : 17-01-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("TTKBootstrap!")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Create entry widget
        self.my_entry = tb.Entry(
            root, bootstyle='success', font='Helvetica 18', foreground='green',
            width=15, show='😎')
        self.my_entry.pack(pady=50)
            
        # Create Button
        my_button = tb.Button(
            root, bootstyle='danger outline', text='Click Me!', 
            command=self.speak)
        my_button.pack(pady=20)
        
        # Create label
        self.my_label = tb.Label(root, text='')
        self.my_label.pack(pady=20)
        
    def speak(self):
        
        self.my_label.config(
            text=f"You typed: {self.my_entry.get()}")
        

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    