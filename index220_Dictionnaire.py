"""
Tkinter - Codemy.com #220 : Modernize Our Dictionary App With CustomTkinter
Lien : https://www.youtube.com/watch?v=Ew9dsDDy7pk

Même cours que l'index 215 mais cette fois-ci on a recours au CustomTkinter

Éditeur : Laurent REYNAUD
Date : 11-05-2022
"""

import tkinter as tk
import customtkinter as ctk
from PyDictionary import PyDictionary

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration des widgets customtkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        self.root = root
        root.title("Dictionnaire")
        root.geometry('620x470')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"

        my_labelFrame = ctk.CTkFrame(root, corner_radius=10)
        my_labelFrame.pack(pady=20)

        self.my_entry = ctk.CTkEntry(
            my_labelFrame, widt=50, justify='center', height=40, border_width=1,
            placeholder_text='Entrer un mot', text_color='silver')
        self.my_entry.grid(row=0, column=0, padx=10, pady=10)

        my_button = ctk.CTkButton(
            my_labelFrame, text="Rechercher", command=self.lookup)
        my_button.grid(row=0, column=1, padx=10)
        
        text_frame = ctk.CTkFrame(root, corner_radius=10)
        text_frame.pack(pady=10)
        
        self.my_text= tk.Text(text_frame, height=20, width=67, wrap=tk.WORD,
                              bd=0, bg='#292929', fg='silver')
        self.my_text.pack(pady=10, padx=10)
        
    def lookup(self):
        "Bouton d'exécution 'Rechercher'"
        
        # Réinitialisation du texte
        self.my_text.delete(1.0, 'end')
        
        # Rechercher la définition du mot saisi
        dictionary = PyDictionary()
        definition = dictionary.meaning(self.my_entry.get())
        
        # Ajouter la définition dans la zone de text
        # self.my_text.insert('end', definition)    
        
        # Distinguer les != définitions d'un mot
        for key, value in definition.items():
            # Insertion du mot à définir
            self.my_text.insert('end', key + '\n\n') 
            
            # Définitions du mot recherché
            for values in value:
                   self.my_text.insert('end', f'- {values}\n\n') 

if __name__ == '__main__':
    root = ctk.CTk()
    gui =  Gui(root)
    root.mainloop()