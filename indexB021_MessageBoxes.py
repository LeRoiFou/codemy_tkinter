"""
Titre : Message Boxes with TTKBootstrap - Tkinter TTKBootstrap 20
Lien : https://www.youtube.com/watch?v=6CmkK9hBg0Q



Date : 09-05-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Message Box!")
        root.geometry('700x350')
        
        # Main App Icon
        root.iconbitmap('images/homer.ico')
        
        # Message Box Icon
        root.iconbitmap(default='images/homer.ico')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_button = tb.Button(
            root, text='Click Me!', bootstyle='danger', command=self.clicker)
        my_button.pack(pady=40)
        
        self.my_label = tb.Label(root, text='', font='Helvetica 18')
        self.my_label.pack(pady=20)
        
    def clicker(self):
        
        # Create a dialog
        
        # yes/no
        # mb = Messagebox.yesno("Display some message here", "Here is the title")
        
        # ok
        # mb = Messagebox.ok("Display some message here", "Here is the title")
        
        # ok/cancel
        # mb = Messagebox.okcancel("Display some message here", "Here is the title")
        
        # show_info
        # mb = Messagebox.show_info("Display some message here", "Here is the title")
        
        # show_error
        # mb = Messagebox.show_error("Display some message here", 
        # "Here is the title")
        
        # show_warning
        # mb = Messagebox.show_warning("Display some message here", 
        # "Here is the title")
        
        # show_question
        # mb = Messagebox.show_question("Display some message here", 
        # "Here is the title")
        
        # show_warning
        # mb = Messagebox.show_warning("Display some message here", 
        #                              "Here is the title")
        
        # yesnocancel
        # mb = Messagebox.yesnocancel("Display some message here", 
        #                              "Here is the title")
        
        # retrycancel
        mb = Messagebox.retrycancel("Display some message here", 
                                     "Here is the title")
        
        # Display button click
        self.my_label.config(text=f"You Clicked '{mb}'")

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    