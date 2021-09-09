"""
Tkinter - Codemy.com #190 : Validate Software Registration Key
Lien : https://www.youtube.com/watch?v=XWj-5CBmbGg

Dans ce programme on génère une clé de format aaaa-bbbb-cccc-dddd-1111 qui a :
-> en 3ème caractère, un caractère qui se retrouve encore 2 fois dans la clé
-> un chiffre qui se retrouve 3 fois dans la clé
-> un score compris entre 1700 et 1800

L'objet de cette 'codification' permet de ne pas créer une base de données
afin de copier la clé générée et de faire un comparable entre la clé saisie
et la clé figurant dans la base de données

Suite du cours précédent : dans cette partie on applique les règles définies
ci-dessus

On a recours à des boucles infinies avec la condition if/else et True/False,
ainsi que le rappel du méthode dans une méthode (ici generate())

Éditeur : Laurent REYNAUD
Date : 09-09-21
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
        self.score_label = tk.Label(
            root, 
            text="Score : ", 
            font=('Helvetica', 32))
        self.score_label.pack(pady=10)
 
    def verify(self, key):
        "Vérification que la clé à générer est valide"
        
        self.score = 0
        
        # Définir notre chiffre de contrôle
        check_digit = self.key[2] # caractère à la position 3
        check_digit_count = 0
        
        # Séparation de la clé à partir des tirets sous forme d'une liste
        chunks = key.split('-')
        
        # Pour chaque composant (qui a chacun d'eux 4 caractères)
        # de la liste 'chunks'
        for chunk in chunks:
            
            # Si le nombre de caractères dans le composant < 4
            if len(chunk) != 4:
                return False
            
            # Pour chaque caractère de chaque composant de la liste 'chunks'
            for char in chunk:
                # Si le le caractère est le même que celui
                # à la position 3 de la clé
                if char == check_digit:
                    check_digit_count += 1
                # Conversion du caractère en chiffre ascii
                self.score += ord(char)
        
        # Si le score est compris entre... et qu'il y a 3 caractères
        # identiques dans la clé que le caractère à la position 3 de cette clé        
        if self.score > 1700 and self.score < 1800 and check_digit_count == 3:
            return True
        else:
            # Boucle infinie tant qu'on a pas le résultat souhaité
            return False
        
    def generate(self):
        "Générer une clé"
        
        # Réinitialisation des données
        self.key_label.delete(0, 'end')
        self.verify_label.config(text='')
        
        # Assignation des variables
        self.key = '' # aaaa-bbbb-cccc-dddd-1111
        section = '' # aaaa ou bbbb ou cccc ou dddd ou 1111
        check_digit_count = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
        
        # Clé : aaaa-bbbb-cccc-dddd-1111 soit 24 caractères    
        while len(self.key) < 25:
            # Générer un caractère au hasard de la variable 'alphabet'
            char_random = random.choice(alphabet)
            # Ajout de ce caractère dans la variable key
            self.key += char_random
            # Ajout de ce caractère également dans la variable section
            section += char_random
            # Si le nombre de caractères dans une section  est = à 4
            if len(section) == 4:
                # Ajout du trait d'union
                self.key += '-'
                # Réinitialisation de la variable section
                section = ''
        
        # Tous les composants sauf le '-' en dernier caractère de la str
        self.key = self.key[:-1]
        
        # Vérifications
        if self.verify(self.key):
            # La clé est vérifiée : affichage de la clé
            self.key_label.insert(0, self.key)
            self.verify_label.config(text="Valide !")
            self.score_label.config(text=f"Score : {self.score}")
            
        else:
            # La clé n'est pas vérifiée : relancer la méthode
            self.generate()
        

if __name__ == '__main__':
    root = tk.Tk()
    gui =  Gui(root)
    root.mainloop()
