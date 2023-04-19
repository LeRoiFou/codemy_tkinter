"""
Titre : Spinboxes with TTKBootstrap - Tkinter TTKBootstrap 18
Lien : https://www.youtube.com/watch?v=6oVlb6f55fY

Date : 19-04-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("SpinBoxes!")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Spinbox list
        my_list = ["John", "April", "Bob", "Mary"]
        
        # Spinbox!
        self.my_spin = tb.Spinbox(
            root, bootstyle='success', font='Helvettica 18', from_=0, to=10,
            values=my_list, state="readonly", command=self.spinny)
        self.my_spin.pack(pady=20)
        
        # Set spinbox default
        self.my_spin.set('John')
        
        # Button
        my_button = tb.Button(
            root, text='Click Me!', bootstyle='success', command=self.spinny)
        my_button.pack(pady=20)
        
        # Label
        self.my_label = tb.Label(root, text='', font='Helvetica 18')
        self.my_label.pack(pady=20)
        
    def spinny(self):
        
        self.my_label.config(text=self.my_spin.get())

if __name__ == '__main__':
    
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    