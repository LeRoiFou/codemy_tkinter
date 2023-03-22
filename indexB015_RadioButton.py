"""
Titre : Radio Buttons with TTKBootstrap - Tkinter TTKBootstrap 14
Lien : https://www.youtube.com/watch?v=-5Tu6dRsvuU



Date : 22-03-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("RadioButton!")
        root.geometry('500x550')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Create radio button list
        toppings = ['Pepperoni', 'Cheese', 'Veggie']
        
        # Create a tkinter variable to keep track everything
        self.my_topping = tk.StringVar()
        
        # Loop thru the list and create radio buttons
        for topping in toppings :
            tb.Radiobutton(
                root, bootstyle='danger', variable=self.my_topping, 
                text=topping, value=topping, command=self.clicker).pack(pady=20)
            
        # Create button
        my_button = tb.Button(root, text='Click Me!', command=self.clicker)
        my_button.pack(pady=20)
        
        # Create a label
        self.my_label = tb.Label(root, text='You selected: ')
        self.my_label.pack(pady=20)
        
        # Create actual radio button buttons
        rb1 = tb.Radiobutton(
            root, bootstyle='info toolbutton', variable=self.my_topping,
            text='Radio Button 1', value='Radio Button 11', command=self.clicker)
        rb1.pack(pady=20)
        
        rb2 = tb.Radiobutton(
            root, bootstyle='info toolbutton outline', variable=self.my_topping,
            text='Radio Button 2', value='Radio Button 22', command=self.clicker)
        rb2.pack(pady=20)
        
    def clicker(self):
        
        self.my_label.config(text=f'You selected: {self.my_topping.get()}')

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    