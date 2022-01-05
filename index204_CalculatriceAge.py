"""
Tkinter - Codemy.com #204 : Build An Age Calculator 
Lien : https://www.youtube.com/watch?v=5IHpLjKLDFI

Dans ce programme on créé une calculatrice qui détermine l'âge 
à partir de l'année de naissance

Éditeur : Laurent REYNAUD
Date : 05-01-22
"""

import tkinter as tk
from datetime import datetime
from tkinter import messagebox

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title("Calculatrice âge")
        root.geometry('500x300')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        my_label = tk.Label(
            root, 
            text='Entrer votre année de naissance', 
            font='Helvetica 24')
        my_label.pack(pady=20)
        
        self.my_entry = tk.Entry(
            root,
            justify='center',
            width=30,
            font='Helvetica 18')
        self.my_entry.pack(pady=20)
        
        my_button = tk.Button(
            root,
            text="Calculer l'âge !",
            font='Helvetica 18',
            command=self.age)
        my_button.pack(pady=20)
        
    
    def age(self):
        "Méthode de calcul de l'âge"
        
        if self.my_entry.get():
            # Année actuelle
            current_year = datetime.now().year
            # Calcul de l'âge
            your_age = current_year - int(self.my_entry.get())
            # Affichage de l'âge
            messagebox.showinfo("Votre âge",
                                f"Votre âge est {your_age} ans")
        else:
            # Absence de saisie de l'année de naissance
            messagebox.showerror(
                "Erreur",
                "Vous avez oublié de saisir l'année de naissance")

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
