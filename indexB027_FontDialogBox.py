"""
Titre : Select Fonts With Font Dialog Box - Tkinter TTKBootstrap 26
Lien : https://www.youtube.com/watch?v=pIm7jY4Z1Sw


Date : 12-07-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs.dialogs import FontDialog

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Font Dialog Box!")
        root.geometry('300x200')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Create a label and button
        my_button = tb.Button(
            root, text='Open Font Dialog', command=self.open_font)
        my_button.pack(pady=40)
        
        self.my_label = tb.Label(root, text='Hello World!')
        self.my_label.pack(pady=10)
        
    def open_font(self):
        
        # Define Font Dialog
        fd = FontDialog()
        
        # Show the box
        fd.show()
        
        # Capture the result and update label
        self.my_label.config(font=fd.result)

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    