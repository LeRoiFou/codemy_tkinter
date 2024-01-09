"""
Titre : Object Oriented CustomTkinter - Tkinter CustomTkinter 22
Lien : https://www.youtube.com/watch?v=GPcCLiOYVe4


Date : 09-01-24
"""

import customtkinter as ctk
import tkinter as tk

class App(ctk.CTk):
    
    def __init__(self):
        
        super().__init__()
        
        # Configuration de la fenêtre principale
        self.title("POO!")
        self.geometry('700x450')  
        
        # Texte
        self.my_text = ctk.CTkTextbox(self, width=600, height=300)
        self.my_text.pack(pady=20)

        # Bouton d'exécution
        self.my_button = ctk.CTkButton(self, text="Clear Box", command=self.clear)
        self.my_button.pack(pady=20)  
    
    # Bouton d'exécution : texte effacé
    def clear(self):
        
        self.my_text.delete('0.0', tk.END)

if __name__ == '__main__':
    
    # Apparence du GUI
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('dark-blue')
    
    # Instanciation de la classe ci-avant et lancement de l'application
    app = App()        
    app.mainloop()
