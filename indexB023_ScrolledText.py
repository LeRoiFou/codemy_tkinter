"""
Titre : Scrolled Text Widget!! - Tkinter TTKBootstrap 22
Lien : https://www.youtube.com/watch?v=Z2gt28vryxo

Date : 23-05-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText # Barre de défilement avec le texte

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Scrolled Text Widget!")
        root.geometry('700x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Text Widget
        my_text = ScrolledText(
            root, height=20, width=110, wrap=WORD, autohide=False, 
            bootstyle='danger', hbar=True)
        my_text.pack(pady=15)

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    