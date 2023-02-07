"""
Titre : Frames and Labels with TTKBootstrap - Tkinter TTKBootstrap 9
Lien : https://www.youtube.com/watch?v=uMUyS7TuZcA

Date : 07-02-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Frames and Labels!")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_frame = tk.Frame(root)
        my_frame.pack(pady=40)
        
        my_entry = tb.Entry(my_frame, font='Helvetica 18')
        my_entry.pack(pady=20, padx=20)
        
        my_button = tb.Button(
            my_frame, text="CLICK ME!", bootstyle='dark', command=self.thing)
        my_button.pack(pady=20, padx=20)
        
        my_label = tb.Label(
            root, text="Hello There!", font='Helvetica 18', 
            bootstyle='inverse light')
        my_label.pack(pady=20)
        
    def thing(self):
        
        pass

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    