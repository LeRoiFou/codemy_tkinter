"""
Tkinter - Codemy.com : Style And Theme Your App The Easy Way - Tkinter Projects 4
Lien : https://www.youtube.com/watch?v=fOVmMiyezMU

Dans ce programme on apprend à insérer un menu pour le style et le thème
Module installé : ttkthemes

Éditeur : Laurent REYNAUD
Date : 14-09-22
"""

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"

        self.root = root
        root.title("Styles and Themes")
        root.geometry('500x350')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Define Style
        self.style = ttk.Style(root)
        self.style.theme_use('default')
        
        # See included styles
        # print(ttk.Style().theme_names())
        our_themes = ttk.Style().theme_names()
        our_themes2 = root.get_themes()
        
        # Create a Menu
        my_menu = tk.Menu(root)
        root.config(menu=my_menu)
        theme_menu = tk.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Themes', menu=theme_menu)
        
        # Sub menu
        for t in our_themes2:
            theme_menu.add_command(label=t, command=lambda t=t:self.changer(t))
        
        # Header Label
        self.my_label = ttk.Label(root, text="Login", font='Helvetica 18')
        self.my_label.pack(pady=20)
        
        # Login Frame
        self.my_frame = ttk.Frame(root)
        self.my_frame.pack(pady=20)

        # Username and Password Entry Boxes and Labels
        self.un_label = ttk.Label(self.my_frame, text="User Name: ")
        self.un_label.grid(row=0, column=0, padx=10, pady=(20,5))
        
        self.un_entry = ttk.Entry(self.my_frame)
        self.un_entry.grid(row=0, column=1, padx=10, pady=(20,5))
        
        self.pw_label = ttk.Label(self.my_frame, text="Password: ")
        self.pw_label.grid(row=1, column=0, padx=10, pady=(0,20))
        
        self.pw_entry = ttk.Entry(self.my_frame, show='*')
        self.pw_entry.grid(row=1, column=1, padx=20, pady=(0,20))
        
        # Login Button
        self.my_button = ttk.Button(root, text="Login")
        self.my_button.pack(pady=0)
        
        # Radio Buttons
        self.radio_frame = tk.Frame(root)
        self.radio_frame.pack(pady=20)
        
        var = tk.IntVar()
        self.my_radio1 = ttk.Radiobutton(
            self.radio_frame, text="Remember Me", variable=var)
        self.my_radio1.grid(row=0, column=0, padx=20)
        
        self.my_radio1 = ttk.Radiobutton(
            self.radio_frame, text="Dont't Remember Me", variable=var)
        self.my_radio1.grid(row=0, column=1)
        
    def changer(self, theme):
        "Change style"

        self.style.theme_use(theme)
        self.my_label.config(text=f"Login - {theme}")


if __name__ == '__main__':
    root = ThemedTk()
    gui =  Gui(root)
    root.mainloop()
