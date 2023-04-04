"""
Titre : Scrollbars with TTKBootstrap - Tkinter TTKBootstrap 16
Lien : https://www.youtube.com/watch?v=wxuejyQeZgc


Date : 04-04-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Scrollbar!")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Frame
        my_frame = tb.Frame(root)
        my_frame.pack(pady=20)
        
        # Create a scrollbar
        my_scroll = tb.Scrollbar(
            my_frame, orient='vertical', bootstyle='danger round')
        my_scroll.pack(side='right', fill='y')
        
        # Create a text widget
        my_text = tk.Text(
            my_frame, width=30, height=25, yscrollcommand=my_scroll.set,
            wrap='none', font='Helvetica 18')
        my_text.pack()
        
        # Config the scrollbar
        my_scroll.config(command=my_text.yview)

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    