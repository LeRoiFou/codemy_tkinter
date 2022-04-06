"""
Tkinter - Codemy.com #215 : Build A Word Dictionary
Lien : https://www.youtube.com/watch?v=PXec_LxI8Sk

Module installé : PyDictionary
Définition des mots en anglais...

Éditeur : Laurent REYNAUD
Date : 06-04-22
"""

import tkinter as tk
from PyDictionary import PyDictionary

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Dictionnaire")
        root.geometry('570x500')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"

        my_labelFrame = tk.LabelFrame(root, text='Entrer un mot')
        my_labelFrame.pack(pady=20)

        self.my_entry = tk.Entry(
            my_labelFrame, font='Helevetica 20', justify='center')
        self.my_entry.grid(row=0, column=0, padx=10, pady=10)

        my_button = tk.Button(
            my_labelFrame, text="Rechercher", command=self.lookup)
        my_button.grid(row=0, column=1, padx=10)
        
        self.my_text= tk.Text(root, height=20, width=65, wrap=tk.WORD)
        self.my_text.pack(pady=10)
        
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
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
