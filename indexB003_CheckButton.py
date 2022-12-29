"""
Titre : Modern Checkbuttons, Toolbuttons, and Togglebuttons - Tkinter TTKBootstrap 3
Lien : https://www.youtube.com/watch?v=qhFm_0j_zsc

Autre widget : checkbutton 🙀

Date : 29-12-22
"""

import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Widgets 2!")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Label
        self.my_label = tb.Label(
            root, text="Click the checkbutton below", font='Helvetica 18')
        self.my_label.pack(pady=(40, 10))
        
        # CheckButton
        self.var1 = tk.IntVar()
        my_check = tb.Checkbutton(
            root, bootstyle='primary', text="Check Me Out!", 
            variable=self.var1, onvalue=1, offvalue=0, command=self.checker)
        my_check.pack(pady=10)
        
        # ToolButton
        self.var2 = tk.IntVar()
        my_check2 = tb.Checkbutton(
            root, bootstyle='danger, toolbutton', text="ToolButton!",
            variable=self.var2, onvalue=1, offvalue=0, command=self.checker)
        my_check2.pack(pady=10)
        
        # Outline Toggle Button
        self.var3 = tk.IntVar()
        my_check3 = tb.Checkbutton(
            root, bootstyle='danger, toolbutton, outline', 
            text="Outlined ToolButton!",
            variable=self.var3, onvalue=1, offvalue=0, command=self.checker)
        my_check3.pack(pady=10)
        
        # Round Toggle Button
        self.var4 = tk.IntVar()
        my_check4 = tb.Checkbutton(
            root, bootstyle='success, round-toggle', 
            text="Round Toggle!",
            variable=self.var4, onvalue=1, offvalue=0, command=self.checker)
        my_check4.pack(pady=10)
        
        # Square Toggle Button
        self.var5 = tk.IntVar()
        my_check5 = tb.Checkbutton(
            root, bootstyle='success, square-toggle', 
            text="Square Toggle!",
            variable=self.var5, onvalue=1, offvalue=0, command=self.checker)
        my_check5.pack(pady=10)
        
    def checker(self):
        
        if self.var1.get() == 1:
            self.my_label.config(text="Checked!")
        else:
            self.my_label.config(text="Unchecked!")

if __name__ == '__main__':
    root = tb.Window(themename="superhero")
    gui =  Gui(root)
    root.mainloop()
    