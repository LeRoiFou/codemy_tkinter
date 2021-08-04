"""
Tkinter - Codemy.com #185 : Limit The Number Of New Windows To Open
Lien : https://www.youtube.com/watch?v=H_zZiIlnB8M

Dans ce programme on apprend à limiter le nombre de nouvelles
fenêtres à ouvrir

Éditeur : Laurent REYNAUD
Date : 04-08-21
"""

import tkinter as tk
from tkinter import messagebox

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.title('Limiter le nombre de nouvelles fenêtres')
        root.geometry('300x200')
        
        # Attribution d'un compteur pour limiter le nbre de fenêtres
        self.counter = 1
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_button = tk.Button(
            root, 
            text='Ouvrir une fenêtre', 
            command=self.open)
        my_button.pack(pady=50, padx=50)
        
    def open(self):
        "Ouverture d'une nouvelle fenêtre"
        
        # Si le nombre de fenêtres ouvertes < à...
        if self.counter < 4:
            
            # Nouvelle fenêtre
            top = tk.Toplevel()
            top.title('Nouvelle fenêtre')
            top.geometry('300x200')
            
            # Titre
            my_label = tk.Label(
                top, 
                text="Nouvelle fenêtre !",
                font="Helvetica, 16")
            my_label.pack(pady=50, padx=50)
            
            # Incrémentation du nombre de fenêtres ouvertes
            self.counter += 1
        
        # Si on insiste à appuyer de nouveau sur le bouton...
        else:
            messagebox.showinfo(
                "Erreur", 
                "Hé ! Tu as déjà ouvert une nouvelle fenêtre !")
     

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
