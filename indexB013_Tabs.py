"""
Titre : Notebook Tabs with TTKBootstrap - Tkinter TTKBootstrap 12
Lien : https://www.youtube.com/watch?v=Vd2ehuL-1RE



Date : 01-03-2023
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Tabs!")
        root.geometry('500x500')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_notebook = tb.Notebook(root, bootstyle='dark')
        my_notebook.pack(pady=20)
        
        tab1 = tb.Frame(my_notebook)
        tab2 = tb.Frame(my_notebook)
        
        my_label1 = tk.Label(tab1, text='My awesome label!', font='Helvetica 18')
        my_label1.pack(pady=20)
        
        my_text = tk.Text(tab1, width=70, height=10)
        my_text.pack(pady=10, padx=10)
        
        my_button = tb.Button(tab1, text='Click Me!', bootstyle='danger online')
        my_button.pack(pady=20)
        
        my_label2 = tk.Label(tab2, text='This is tab two', font='Helvetica 18')
        my_label2.pack(pady=20)
        
        # Add our frames to the notebook
        my_notebook.add(tab1, text='Tab One')
        my_notebook.add(tab2, text='Tab Two')

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    