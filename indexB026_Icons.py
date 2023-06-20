"""
Titre : Icons with TTKBootstrap - Tkinter TTKBootstrap 25
Lien : https://www.youtube.com/watch?v=0CxPjddnSiU



Date : 20-06-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.icons import Icon

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Icons!")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Icons : warning, icon, error, question, info
        # self.img = tk.PhotoImage(data=Icon.warning)
        # self.img = tk.PhotoImage(data=Icon.icon)
        # self.img = tk.PhotoImage(data=Icon.error)
        # self.img = tk.PhotoImage(data=Icon.question)
        self.img = tk.PhotoImage(data=Icon.info)
        
        # Label 
        my_label = tb.Label(image=self.img)
        my_label.pack(pady=50)

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    