"""
Titre : Meters with TTKBootstrap - Tkinter TTKBootstrap 11
Lien : https://www.youtube.com/watch?v=ccImuAgANrQ

Dans ce programme on apprend sur un nouveau widget

Date : 22-02-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Title!")
        root.geometry('500x700')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_meter = tb.Meter(
            root, bootstyle='danger', 
            subtext='Tkinter Learned', # sous-texte
            interactive=True, # activation du cercle
            textright="%", # texte à droite
            # textleft="$", # texte à gauche
            metertype='full', # demi-cercle : 'semi
            stripethickness=10, # gradients
            metersize=200, # taille du cercle
            padding=50, # écart par rapport au cadre
            amountused=0, # valeur par défaut
            amounttotal=100, # valeur totale
            subtextstyle='light' # thème du sous-texte
            )
        self.my_meter.pack(pady=50)
        
        self.my_button = tb.Button(
            root, text='Click Me 5', command=self.clicker)
        self.my_button.pack(pady=20)
        
        self.my_button2 = tb.Button(
            root, text='Step Up', command=self.up)
        self.my_button2.pack(pady=20)
        
        self.my_button3 = tb.Button(
            root, text='Step Down', command=self.down)
        self.my_button3.pack(pady=20)
        
        # Assignation d'un compteur
        self.counter = 20
        
    def clicker(self):
        
        if self.counter <= 100:
            self.my_meter.configure(amountused=self.counter)
            self.counter += 5
            self.my_button.configure(
                text=f"Click me {self.my_meter.amountusedvar.get()}")
            
    def up(self):
        
        self.my_meter.step(10)
        
    def down(self):
        
        self.my_meter.step(-10)
        

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    