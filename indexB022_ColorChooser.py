"""
Titre : Color Chooser for TTKBootstrap - Tkinter TTKBootstrap 21
Lien : https://www.youtube.com/watch?v=Ukn8Su-SVW4

Dans ce programme on apprend à choisir des couleurs

Date : 16-05-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Color Chooser!")
        root.geometry('700x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_button = tb.Button(
            root, text='Click Me!', bootstyle='danger', command=self.cc)
        my_button.pack(pady=40)
        
        self.my_label = tb.Label(root, text='', font='Helvetica 18')
        self.my_label.pack(pady=10)
        
    def cc(self):
        
        # Create color chooser
        my_color = ColorChooserDialog()
        
        # Show color chooser
        my_color.show()
        
        # Return color chooser
        colors = my_color.result
        
        # Output to the label (.hex .hsl .rgb)
        self.my_label.config(text=colors.hex)
        
        # Change the bg color of our app to chosen color
        root.configure(background=colors.hex)
        

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    