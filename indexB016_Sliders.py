"""
Titre : Slider / Scales with TTKBootstrap - Tkinter TTKBootstrap 15
Lien : https://www.youtube.com/watch?v=d5jaOLXGqvg



Date : 28-03-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Slider/Scales!")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Create a Scale/Slider
        self.my_scale = tb.Scale(
            root, bootstyle='warning', length=400, orient='horizontal',
            from_=0, to=500, command=self.scaler, state='normal',)
        self.my_scale.pack(pady=50)
        
        # Create a label
        self.my_label = tb.Label(root, text='')
        self.my_label.pack()
        
    def scaler(self, e):
        
        self.my_label.config(text=f'{int(self.my_scale.get())}%', 
                             font='Helvetica 18')
        
        if self.my_scale.get() < 50:
            pass
        else:
            pass

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    