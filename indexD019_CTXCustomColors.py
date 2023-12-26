"""
Titre : Custom Color Themes - Tkinter CustomTkinter 20
Lien : https://www.youtube.com/watch?v=mMyZD8qcYtA

Suite du précédent cours sur la configuration des couleurs de la page principale

Récupération des thèmes de couleurs :
https://github.com/TomSchimansky/CustomTkinter/tree/master/customtkinter/assets/themes
et copie du fichier JSON : green.json
Dans ce fichier JSON, nous avons toute la configuration des couleurs des composants
Le fichier JSON se trouve dans le répertoire "assets"

Date : 26-12-2023
"""

import customtkinter as ctk
import tkinter as tk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        ctk.set_appearance_mode('dark')
        
        # Chargement du fichier JSON
        ctk.set_default_color_theme('assets/indexD019_CTXCustomColors.json')
        
        self.root = root
        root.title("Titre!")
        root.geometry('700x550')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        self.my_text = ctk.CTkTextbox(root, width=600, height=300)
        self.my_text.insert(tk.END, "This is Dark Mode...")
        self.my_text.pack(pady=20)
        
        my_button = ctk.CTkButton(
            root, text="Change Light/Dark", command=self.change)
        my_button.pack(pady=20)
        
        self.mode = 'dark'
        
        colors = ['blue' ,'dark-blue', 'green']
        my_option = ctk.CTkOptionMenu(
            root, values=colors, command=self.change_colors)
        my_option.pack(pady=10)
        
        my_progress = ctk.CTkProgressBar(root, orientation='horizontal')
        my_progress.pack(pady=20)
        
    def change(self):
        
        if self.mode == 'dark' :
            ctk.set_appearance_mode('light')
            self.mode = 'light'
            self.my_text.delete(0.0, tk.END)
            self.my_text.insert(tk.END, "This is Light Mode...")
        else:
            ctk.set_appearance_mode('dark')
            self.mode = 'dark'
            self.my_text.delete(0.0, tk.END)
            self.my_text.insert(tk.END, "This is Dark Mode...")
            
    def change_colors(self, choice):
        ctk.set_default_color_theme(choice)
        
if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()
