"""
Titre : Scrolled Frame Widget! - Tkinter TTKBootstrap 23
Lien : https://www.youtube.com/watch?v=V1i3EyfRQa0



Date : 07-06-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame # Barre de défilement fenêtre

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        root.title("Scrolled Frame!")
        root.geometry('700x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Lets create a scrolled frame
        my_frame = ScrolledFrame(root, bootstyle='dark')
        my_frame.pack(pady=15, padx=15, fill=tb.BOTH, expand=tb.YES)
        
        # Create some buttons
        for x in range(21):
            tb.Button(my_frame, bootstyle='info', text=f"Click Me {x}!").pack(pady=10)

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    