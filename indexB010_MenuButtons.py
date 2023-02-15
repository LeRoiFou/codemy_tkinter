"""
Titre : Menu Buttons with TTKBootstrap - Tkinter TTKBootstrap 10
Lien : https://www.youtube.com/watch?v=7rBiJbdsm2M



Date : 15-02-23
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Menu Buttons!")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_menu = tb.Menubutton(
            root, bootstyle='warning', text='Things!')
        self.my_menu.pack(pady=50)
        
        # Create basic menu
        inside_menu = tb.Menu(self.my_menu)
        
        # Add items to our inside menu
        item_var = tk.StringVar()
        for x in ['primary', 'secondary', 'danger',
                  'info', 'outline primary', 
                  'outline secondary', 'outline danger',
                  'outline info']:
            inside_menu.add_radiobutton(
                label=x, variable=item_var, 
                command=lambda x=x:self.stuff(x))
            
        # Associate the inside menu with the menubutton
        self.my_menu['menu'] = inside_menu
        
        # Create label
        self.my_label = tb.Label(root, text='')
        self.my_label.pack(pady=40)
        
    def stuff(self, x):
        
        self.my_menu.config(bootstyle=x)
        self.my_label.config(text=f'You selected {x}!')
        

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    