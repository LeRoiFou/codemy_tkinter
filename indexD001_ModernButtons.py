"""
Titre : Modern Buttons In CustomTkinter - Tkinter CustomTkinter 2
Lien : https://www.youtube.com/watch?v=WE1IuPOICxE



Date : 16-08-23
"""

import customtkinter as ctk
import tkinter as tk


class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Custom tkinter Buttons!")
        root.geometry('600x350')
        
        # Customisation de la fenêtre avec customtkinter
        ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_button = ctk.CTkButton(
            root, 
            text='Hello World!', 
            height=100,
            width=200,
            font=('Helvetica', 24),
            text_color='black',
            fg_color='red',
            hover_color='green', # passage de la souris sur le bouton
            corner_radius=50,
            bg_color='white',
            border_width=10, # épaisseur du contour du bouton
            border_color='yellow',
            state='normal',
            command=self.hello)
        self.my_button.pack(pady=80)
        
        self.my_label = ctk.CTkLabel(root, text='')
        self.my_label.pack(pady=20)
        
    def hello(self):
        
        # Récupération du texte mentionné sur le bouton
        self.my_label.configure(text=self.my_button.cget('text'))

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
    