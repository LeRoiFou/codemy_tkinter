"""
Titre : ComboBoxes and Bindings - Tkinter TTKBootstrap 5
Lien : https://www.youtube.com/watch?v=EiRWAfqGkow



Date : 12-01-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Comboxes!")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Create label
        self.my_label = tb.Label(
            root, text="Hello World!", font='Helvetica 18')
        self.my_label.pack(pady=30)
        
        # Create dropdown options
        days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi',
                'Vendredi', 'Samedi', 'Dimanche']
        
        # Create combobox
        self.my_combo = tb.Combobox(
            root, bootstyle='success', value=days)
        self.my_combo.pack(pady=20)
        
        # Set combo default
        self.my_combo.current(6)
        
        # Create button
        my_button = tb.Button(
            root, text="Click Me!", command=self.clicker,
            bootstyle='danger')
        my_button.pack(pady=20)
        
        # Bind combobox
        self.my_combo.bind(
            '<<ComboboxSelected>>', self.click_bind)
        
    def clicker(self):
        "Sélection à partir du bouton"
        
        self.my_label.config(
            text=f"Tu as cliqué sur {self.my_combo.get()}")
        
    def click_bind(self, e):
        "Sélection à partir du menu déroulant"
        
        self.my_label.config(
            text=f"Tu as cliqué sur {self.my_combo.get()}")

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    