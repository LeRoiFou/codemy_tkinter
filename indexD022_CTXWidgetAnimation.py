"""
Titre : Widget Animation - Tkinter CustomTkinter 23
Lien : https://www.youtube.com/watch?v=cNftEm-Rs6k

Animation d'une zone de texte

Date : 16-01-24
"""

import customtkinter as ctk
import tkinter as tk

class App(ctk.CTk) :
    
    def __init__(self):
        "Constructeur de la classe"
        
        super().__init__()
        
        # Configuration de la fenêtre principale
        self.title("Titre!")
        self.geometry('700x450')

        # Configuration du cadre principal
        my_frame = ctk.CTkFrame(self)
        my_frame.pack(pady=20)
        
        # Boutons d'exécution
        self.up_button = ctk.CTkButton(my_frame, text="Up", command=self.up)
        self.up_button.grid(row=0, column=0, padx=10)
        
        # Boutons d'exécution
        self.down_button = ctk.CTkButton(my_frame, text="Down", command=self.down)
        self.down_button.grid(row=0, column=1, padx=10)
        
        # Coordonnées
        self.my_y = 450/2+350
        
        # Zone de texte
        self.my_text = ctk.CTkTextbox(self, width=400, height=200)
        self.my_text.place(x=700/2, y=self.my_y, anchor='center')
        
    def up(self):
        
        # Remontée de la zone de texte
        self.my_y -= 20
        
        # Limite de la remontée...
        if self.my_y >= 195:
            
            # Montée de la zone de texte
            self.my_text.place(x=700/2, y=self.my_y, anchor='center')

            # Modification du texte du bouton d'exécution
            self.up_button.configure(text=self.my_y)
            
            # Activitaion toutes les x millisecondes
            self.after(5, self.up)
    
    def down(self):
        
        # Descente de la zone de texte
        self.my_y += 20
        
        # Limite de la remontée...
        if self.my_y <= 550:
            
            # Montée de la zone de texte
            self.my_text.place(x=700/2, y=self.my_y, anchor='center')

            # Modification du texte du bouton d'exécution
            self.up_button.configure(text=self.my_y)

            # Activitaion toutes les x millisecondes
            self.after(5, self.down)

if __name__ == '__main__':
    
    # Apparence de l'interface graphique
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('dark-blue')
    
    # Intanciation de la classe App et lancement de l'application
    app =  App()
    app.mainloop()
