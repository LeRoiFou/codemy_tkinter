"""
Titre : Floodgauge Progress Bar - Tkinter TTKBootstrap 7
Lien : https://www.youtube.com/watch?v=NzQgXFizpuQ



Date : 27-01-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Progress Bar!")
        root.geometry('500x550')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_gauge = tb.Floodgauge(
            root, bootstyle='success', font='Helvetica 18', mask='Pos: {}%',
            maximum=80, orient='horizontal', value=0, mode='determinate')
        self.my_gauge.pack(pady=50, fill='x', padx=20)
        
        start_button = tb.Button(
            root, text='Start', bootstyle='danger outline', command=self.starter)
        start_button.pack(pady=20)
        
        stop_button = tb.Button(
            root, text='Stop', bootstyle='danger outline', command=self.stopper)
        stop_button.pack(pady=20)
        
        increment_button = tb.Button(
            root, text='Increment', bootstyle='danger outline', 
            command=self.incrementer)
        increment_button.pack(pady=20)
        
        self.my_label = tb.Label(root, text='Position:')
        self.my_label.pack(pady=20)
        
    def starter(self):
        
        # Start the gauge
        self.my_gauge.start()
    
    def stopper(self):
        
        # Stop the gauge
        self.my_gauge.stop()
    
    def incrementer(self):
        
        # Increment the gauge
        self.my_gauge.step(10)
        
        self.my_label.config(text=f"Position: {self.my_gauge.variable.get()}")

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    