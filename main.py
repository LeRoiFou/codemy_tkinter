"""
Titre : 
Lien : 



Date : 
"""

import customtkinter as ctk
import tkinter as tk

class App(ctk.Ctk) :
    
    def __init__(self):
        "Constructeur de la classe"
        
        super().__init__()
        
        # Configuration de la fenêtre principale
        self.title("Titre!")
        self.geometry('700x300')

        

if __name__ == '__main__':
    
    # Apparence de l'interface graphique
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('dark-blue')
    
    # Intanciation de la classe App et lancement de l'application
    app =  App()
    app.mainloop()
