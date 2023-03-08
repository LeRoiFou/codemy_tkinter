"""
Titre : Progress Bars with TTKBootstrap - Tkinter TTKBootstrap 13
Lien : https://www.youtube.com/watch?v=HrsglgYFNgE

Dans ce cours on insére une barre de progresssion

Date : 08-03-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import time

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Progress Bar!")
        root.geometry('500x250')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Progress bar
        self.my_progress = tb.Progressbar(
            root, bootstyle='danger striped', 
            maximum=100, 
            mode='determinate',
            length=300,
            value=0)
        self.my_progress.pack(pady=40)
        
        # Frame
        my_frame = tb.Frame(root)
        my_frame.pack(pady=20)
        
        # Buttons
        my_button1 = tb.Button(
            my_frame, text='Increment 20', bootstyle='info', command=self.increment)
        my_button1.grid(column=0, row=0, padx=10)
        
        my_button2 = tb.Button(
            my_frame, text='Start', bootstyle='info', command=self.start)
        my_button2.grid(column=1, row=0, padx=10)
        
        my_button3 = tb.Button(
            my_frame, text='Stop', bootstyle='info', command=self.stop)
        my_button3.grid(column=2, row=0, padx=10)
        
        my_button4 = tb.Button(
            my_frame, text='Auto', bootstyle='info', command=self.auto)
        my_button4.grid(column=3, row=0, padx=10)
        
        # Label
        self.my_label = tb.Label(root, text='', font='Helvetica 18')
        self.my_label.pack(pady=20)
       
    def increment(self):
        
        # Incrémentation de 20 selon deux méthodes :
        # self.my_progress.step(20)
        self.my_progress['value'] += 20
        
        # Get current value
        self.my_label.config(text=self.my_progress['value'])
        
    def start(self):
        
        # Départ du lancement !!!
        self.my_progress.start(10)
        
    def stop(self):
        
        # Réinitialisation
        self.my_progress.stop()
        
    def auto(self):
        
        for x in range(5):
            self.my_progress['value'] += 20
            self.my_label.config(text=self.my_progress['value'])
            # Mise à jour de la fenêtre
            root.update_idletasks()
            # Incrémentation par seconde
            time.sleep(1)

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    