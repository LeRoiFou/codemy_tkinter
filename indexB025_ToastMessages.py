"""
Titre : Toast Messages with TTKBootstrap - Tkinter TTKBootstrap 24
Lien : https://www.youtube.com/watch?v=-HdGHOkgCak

Un message qui apparaît succintement mais qui est au top !!!

Date : 13-06-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.toast import ToastNotification # Message toasté !

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Toast Messages with TTKBootstrap!")
        root.geometry('300x200')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.toast = ToastNotification(
            title="My Toast Title",
            message="This is a Toast Message!! WOOHOO!!",
            duration=3_000,
            alert=True,
            position=(700, 700, 'sw'),)
        
        my_button = tb.Button(
            root, text='Click Me!', command=self.clicker)
        my_button.pack(pady=40)
        
    def clicker(self):
        
        self.toast.show_toast()
        

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    