"""
Tkinter - Codemy.com #189 : Software Registration Key Generator
Lien : https://www.youtube.com/watch?v=Iwaek1UDV8s

Dans ce programme on génère une clé de format aaaa-bbbb-cccc-dddd-1111 qui a :
-> en 3ème caractère, un caractère qui se retrouve encore 2 fois dans la clé
-> un chiffre qui se retrouve 3 fois dans la clé
-> un score compris entre 1700 et 1800

L'objet de cette 'codification' permet de ne pas créer une base de données
afin de copier la clé générée et de faire un comparable entre la clé saisie
et la clé figurant dans la base de données

Dans cette première partie on affiche les widgets et on génère une clé
au hasard

Éditeur : Laurent REYNAUD
Date : 01-09-21
"""

import tkinter as tk
import random

class Gui :
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        self.root = root
        root.title('Clé génératrice')
        root.geometry('500x500')
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        # Bouton d'exécution
        generate_button = tk.Button(
            root, 
            text='Générer une clé', 
            font=('Helvetica', 32), 
            command=self.generate)
        generate_button.pack(pady=50)
        
        # Clé dans un champ de saisi masqué
        self.key_label = tk.Entry(
            root, 
            font=('Helvetica', 24), 
            bd=0, 
            bg='systembuttonface', 
            width=25)
        self.key_label.pack(pady=10, padx=50)
        
        # Titre
        self.verify_label = tk.Label(
            root, 
            text='En attente...', 
            font=('Helvetica', 32))
        self.verify_label.pack(pady=10)
        
        # Titre
        score_label = tk.Label(
            root, 
            text="Score : ", 
            font=('Helvetica', 32))
        score_label.pack(pady=10)
        
    def generate(self):
        "Générer une clé"
        
        # Réinitialisation des données
        self.key_label.delete(0, 'end')
        self.verify_label.config(text='')
        
        # Assignation des variables
        key = ''
        section = '' # aaaa ou bbbb ou cccc ou dddd ou 1111
        check_digit_count = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
        
        # Clé : aaaa-bbbb-cccc-dddd-1111 soit 24 caractères    
        while len(key) < 25:
            # Générer un caractère au hasard de la variable 'alphabet'
            char = random.choice(alphabet)
            # Ajout de ce caractère dans la variable key
            key += char
            # Ajout de ce caractère également dans la variable section
            section += char
            # Si le nombre de caractères dans une section  est = à 4
            if len(section) == 4:
                # Ajout du trait d'union
                key += '-'
                # Réinitialisation de la variable section
                section = ''
        
        # Tous les composants sauf le '-' en dernier caractère de la str
        key = key[:-1]
        
        # Affichage de la clé dans le champ de saisi masqué
        self.key_label.insert(0, key)
        

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
