"""
Tkinter - Codemy.com #194 : Unicode Dice Roller
Lien : https://www.youtube.com/watch?v=nDV7a9_SATg

Dans ce programme on apprend à créer le jeu de lancer de dés

Éditeur : Laurent REYNAUD
Date : 05-10-21
"""

import tkinter as tk
import random

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.title('Jeu de dés')
        root.geometry('500x500')
        
        # Configuration des widgets
        self.widgets()
        
        # Affichage des dés lors du lancement du jeu
        self.roll_dice() 
        
    def widgets(self):
        "Configuration des widgets"
        
        # Création d'une liste des chiffres du dé
        self.my_dice = [
            '\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        
        # Cadre
        my_frame = tk.Frame(root)
        my_frame.pack(pady=20)
        
        # Affichage des dés
        self.dice_label1 = tk.Label(
            my_frame, 
            text='', 
            font='Helevetica 100',
            fg='blue')
        self.dice_label1.grid(row=0, column=0, padx=5)
        self.dice_label2 = tk.Label(
            my_frame, 
            text='', 
            font='Helevetica 100',
            fg='red')
        self.dice_label2.grid(row=0, column=1, padx=5)
        
        # Affichage des résultats des dés
        self.sub_dice_label1 = tk.Label(
            my_frame, 
            text='')
        self.sub_dice_label1.grid(row=1, column=0, padx=5)
        self.sub_dice_label2 = tk.Label(
            my_frame, 
            text='')
        self.sub_dice_label2.grid(row=1, column=1, padx=5)
        
        # Bouton
        my_button = tk.Button(
            root, 
            text="Lancer les dés", 
            font='Helvetica 24',
            command=self.roll_dice) 
        my_button.pack(pady=20)
        
        # Total du résultat obtenu
        self.total_label = tk.Label(
            root, 
            text='', 
            font='Helvetica 24', 
            fg='grey')
        self.total_label.pack(pady=40)
        
    def roll_dice(self):
        "Mise à jour du résultat des dés lancés"
        
        # Chiffre du dé au hasard
        d1 = random.choice(self.my_dice)
        d2 = random.choice(self.my_dice)
        
        # Chiffre relatif au dé sorti (voir méthode ci-après)
        sd1 = self.get_number(d1)
        sd2 = self.get_number(d2)
        
        # Mise à jour de l'affichage des dés
        self.dice_label1.config(text=f"{d1}")
        self.dice_label2.config(text=f"{d2}")
        
        # Mise à jour de l'affichage des résultats des dés
        self.sub_dice_label1.config(text=sd1)
        self.sub_dice_label2.config(text=sd2)
        
        # Mise à jour du total des dés affichés
        self.total_label.config(text=f'Total : {sd1 + sd2}')
        
    def get_number(self, x):
        "'Transcription' en chiffre du dé sorti"

        if x == '\u2680':
            return 1
        elif x == '\u2681':
            return 2
        elif x == '\u2682':
            return 3
        elif x == '\u2683':
            return 4
        elif x == '\u2684':
            return 5
        elif x == '\u2685':
            return 6
        

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
