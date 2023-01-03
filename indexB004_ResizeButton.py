"""
Titre : How To Resize Buttons in TTKBootstrap - Tkinter TTKBootstrap 4
Lien : https://www.youtube.com/watch?v=Awl-wlRJIIM

Dans ce programme on apprend à agrandir un bouton

Date : 03-01-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Resize Buttons!")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Style
        my_style = tb.Style()
        my_style.configure('success.Outline.TButton', font='Helvetica 18')
        
        my_button = tb.Button(
            root, text="Hellow World!", bootstyle='success', 
            style='success.Outline.TButton', width=20)
        my_button.pack(pady=40)

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    