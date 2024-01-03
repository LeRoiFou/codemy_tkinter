"""
Titre : High Definition App Scaling - Tkinter CustomTkinter 21
Lien : https://www.youtube.com/watch?v=m4jeF_Sitf4

Complément du précédent cours : mise à jour de l'application selon le zoom appliqué
sur Windows : avec un zoom plus important (125 %, 150 %...), l'application risque
d'être floutée, pour résoudre ce problème, les explications sont détaillées dans
le lien ci-après :
https://customtkinter.tomschimansky.com/documentation/scaling

Ce cours est notamment destiné aux mal-voyants qui nécessitent d'avoir un zoom
plus important sur la présentation des applications

Date : 03-01-24
"""

import customtkinter as ctk
import tkinter as tk

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
               
        # zoom de 100 % appliqué comme si le zoom appliqué sur windows 
        # était de 100 % (zoom appliqué sur windows de 125 %)
        # ctk.deactivate_automatic_dpi_awareness()
        
        # zoom appliquée sur l'application (pour les mal-voyants)
        ctk.set_widget_scaling(1.5)
        ctk.set_window_scaling(1.5)
        
        # Apparence de l'application
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
