"""
Titre : Treeviews with TTKBootstrap - Tkinter TTKBootstrap 19
Lien : https://www.youtube.com/watch?v=X0YF6kBvSgk

Date : 25-04-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Treeview!")
        root.geometry('700x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
 
        # Define Columns
        columns = ("first_name", "last_name", "email")
        
        # Create Treeview
        my_tree = tb.Treeview(
            root, bootstyle='primary', columns=columns, show='headings')
        my_tree.pack(pady=20)
        
        # Define headings
        my_tree.heading('first_name', text='First Name')
        my_tree.heading('last_name', text='Last Name')
        my_tree.heading('email', text='Email Address')
        
        # Create Sample Data
        contacts = []
        for n in range(1,20):
            contacts.append((f'First {n}', f'Last {n}', f'email{n}@address.com'))
        
        # Add Data to Treeview
        for contact in contacts:
            my_tree.insert('', END, values=contact)

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    