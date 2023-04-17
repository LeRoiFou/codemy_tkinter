"""
Titre : Separators and Sizegrips with TTKBootstrap - Tkinter TTKBootstrap 17
Lien : https://www.youtube.com/watch?v=rN3cT8t-KXA



Date : 17-04-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Separators and Sizegrip!")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self): 
        "Configuration des widgets"
        
        label1 = tb.Label(root, text='Label 1', bootstyle='light')
        label1.pack(pady=40)
        
        # Separator
        my_sep = tb.Separator(root, bootstyle='info')
        my_sep.pack(fill='x', # séparateur sur la largeur de la fenêtre
                    padx=100 # délimitation du séparateur par rapport à la fenêtre
                    ) 
        
        label2 = tb.Label(root, text='Label 2', bootstyle='light')
        label2.pack(pady=40)
        
        # Sizegrip (largeur et longueur de la fenêtre à modifier... bof)
        my_sizegrip = tb.Sizegrip(root, bootstyle='info')
        my_sizegrip.pack(anchor=SE, fill='both', expand=True)

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    