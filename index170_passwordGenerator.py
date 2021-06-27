"""
Tkinter - Codemy.com #170 : 
Build A Strong Password Generator App - Python Tkinter GUI Tutorial #170
Lien : https://www.youtube.com/watch?v=XaVp2l6Z_Dc

Dans ce programme on apprend à générer un mot de passe 'difficile' 
en donnant uniquement le nombre de caractères souhaités

Pour cela, on va recourir au module random pour générer des entiers 
au hasard et pour chaque entier généré est affecté un caractère selon 
la table ASCII détaillée ci-après : https://www.asciitable.com/,
à partir du code décimal n° 33 qui pour ce code, 
génère comme caractère le '!', jusqu'au code décimal n° 126 
qui pour ce code, génère comme caractère le '~'

Éditeur : Laurent REYNAUD
Date : 11-03-21
"""

import tkinter
from random import randint

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.title('Mega-mot de passe !!!')
        root.geometry('500x300')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Champ de saisi pour saisir le nombre de caractère
        du mot de passe à générer et son cadre"""
        
        # cadre
        lf = tkinter.LabelFrame(root, text='Combien de caractères ?')
        lf.pack(pady=20)
        
         # champ de saisi
        self.my_entry = tkinter.Entry(
            lf, 
            font='Helvetica 24', 
            justify='center')
        self.my_entry.pack(pady=20, padx=20)

        """Champ de saisi 'déguisé' en étiquette pour afficher
        le mot de passe généré et pour qu'on puisse le copier"""
        
        # champ de saisi
        self.pw_entry = tkinter.Entry(
            root, 
            text='', 
            font='Helvetica 24', 
            justify='center', 
            bd=0,
            bg="systembuttonface")  
        self.pw_entry.pack(pady=20)

        """Les boutons et son cadre"""
        
        # cadre
        my_frame = tkinter.Frame(root)  
        my_frame.pack(pady=20)
        
        # bouton
        my_button = tkinter.Button(
            my_frame, 
            text='Générer un MDP', 
            command=self.new_rand)  
        my_button.grid(row=0, column=0, padx=10)
        
         # bouton
        clip_button = tkinter.Button(
            my_frame, 
            text='Copier le MDP', 
            command=self.clipper) 
        clip_button.grid(row=0, column=1, padx=10)

    def new_rand(self):
        """Méthode permettant de générer un mot de passe au hasard"""

        """Données saisies effacées"""
        self.pw_entry.delete(0, 'end')

        """Chiffre saisi dans le champ de saisi converti en entier"""
        pw_length = int(self.my_entry.get())

        """Assignation d'une str"""
        my_password = ''

        """Boucle for in range"""
        for x in range(pw_length):
            """Incrémentation des nombres au hasard compris entre 
            l'entier 33 et l'entier 126 converti en caractères"""
            my_password += chr(randint(33, 126))

        """Insertion du mot de passe généré dans le champ de saisi"""
        self.pw_entry.insert(0, my_password)

    def clipper(self):
        """Méthode permettant de copier dans le presse-papier 
        le mot de passe généré"""

        """Effacement des données présentes dans le presse-papier"""
        root.clipboard_clear()

        """Alimentation dans le presse-papier des données copiées"""
        root.clipboard_append(self.pw_entry.get())
      

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
