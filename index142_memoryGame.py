"""
Tkinter - Codemy.com #142 : 
Finishing Our Tile Matching Game - Python Tkinter GUI Tutorial #142
Lien : https://www.youtube.com/watch?v=tW8Bzokv8CQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=142

Dans ce programme on créé un jeu de mémory 
(plusieurs cartes cachées : il faut retrouver deux images identiques)
En complément du précédent tuto, on finalise le jeu avec un menu, 
des couleurs aux boutons, une réinitialisation du jeu et un message 
informant que l'on a gagné

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

import tkinter
import random
from tkinter import messagebox

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        self.root = root
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('460x460')
        
        self.my_variables()
        self.widgets()
        
    def my_variables(self):
        "Variables utilisées dans les méthodes ci-après"
        
        # Assignation d'une variable informant si on a gagné
        self.winner = 0

        "Assignation de variables à utiliser pour la fonction button_click()"
        
        # décompte du nombre de fois que l'on sélectionne un bouton
        self.count = 0  
        
        # alimentation des chiffres affichés dans une liste
        self.answer_list = []  
        
        # alimentation des chiffres affichés dans un dictionnaire
        self.answer_dict = {}  

        """Assignation d'une liste d'entiers à afficher dans le jeu de memory
        qui se compose de 12 cases"""
        
        # Les 12 composants du jeu de memory
        self.matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]  

        """Mélange des chifres listés ci-avant avec la méthode prédéfinie
        shuffle (mélanger) du module random"""
        random.shuffle(self.matches)
          
    def widgets(self):
        "Configuration des widgets"
        
        """Cadre pour les boutons"""
        my_frame = tkinter.Frame(root)
        my_frame.pack(pady=10)

        """Configuration des boutons"""
        
        self.b0 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(self.b0, 0),
            relief='groove')
        
        self.b1 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(self.b1, 1),
            relief='groove')
        
        self.b2 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(self.b2, 2),
            relief='groove')
        
        self.b3 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(self.b3, 3),
            relief='groove')

        self.b4 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(self.b4, 4),
            relief='groove')
        
        self.b5 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(self.b5, 5),
            relief='groove')
        
        self.b6 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(self.b6, 6),
            relief='groove')
        
        self.b7 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(self.b7, 7),
            relief='groove')

        self.b8 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(self.b8, 8),
            relief='groove')
        
        self.b9 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(self.b9, 9),
            relief='groove')
        
        self.b10 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(self.b10, 10),
            relief='groove')
        
        self.b11 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(self.b11, 11),
            relief='groove')

        """Affichage des boutons"""
        self.b0.grid(row=0, column=0)
        self.b1.grid(row=0, column=1)
        self.b2.grid(row=0, column=2)
        self.b3.grid(row=0, column=3)

        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)
        self.b7.grid(row=1, column=3)

        self.b8.grid(row=2, column=0)
        self.b9.grid(row=2, column=1)
        self.b10.grid(row=2, column=2)
        self.b11.grid(row=2, column=3)

        """Affichage du résultat"""
        self.my_label = tkinter.Label(root, text='')
        self.my_label.pack(pady=20)

        """Création d'une barre de menu"""
        my_menu = tkinter.Menu(root)
        root.config(menu=my_menu)

        """Menu options"""
        option_menu = tkinter.Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Options', menu=option_menu)
        option_menu.add_command(
            label='Réinitialiser le jeu', 
            command=self.reset)
        option_menu.add_separator()
        option_menu.add_command(
            label='Quitter le jeu', 
            command=root.quit)
        
    def win(self):
        """Méthode permettant de voir si on a gagné"""

        # affichage du message informant que le jeu est fini
        self.my_label.config(text='Félicitations, tu as gagné !')  

        # assignation liste des boutons
        button_list = [
            self.b0, 
            self.b1, 
            self.b2, 
            self.b3, 
            self.b4, 
            self.b5,
            self.b6, 
            self.b7, 
            self.b8, 
            self.b9, 
            self.b10, 
            self.b11]  

        """Parcours des boutons et changement des couleurs 
        dès que tous les chiffres ont été trouvés"""
        for button in button_list:
            button.config(bg='yellow')

    def button_click(self, b, number):
        """Méthode permettant d'afficher un chiffre 
        en cliquant sur le bouton concerné"""

        if b['text'] == ' ' and self.count < 2:
            """Si la case est vide et que c'est le première séléction : 
            Affichage du nombre attribué au bouton sélectionné selon 
            un chiffre au hasard : dans l'instruction ci-dessous 
            par principe le bouton à l'indice 0 (b[0]) affichera le chiffre 1 
            (matches[0] = 1), mais comme on a déclaré l'instruction suivante :
            random.shuffle(matches), le nombre affiché sera compris 
            entre 1 et 6"""
            
            b['text'] = self.matches[number]
            
            """Conservation du chiffre affiché dans une liste et 
            dans un dictionnaire"""
            self.answer_list.append(number)
            self.answer_dict[b] = self.matches[number]
            
            """Incrémentation du compteur"""
            self.count += 1

        if len(self.answer_list) == 2:
            """S'il y a deux composants dans la liste..."""
            
            if (self.matches[self.answer_list[0]] == 
                self.matches[self.answer_list[1]]):
                """et si le chiffre à l'indice 0 de la liste est égal 
                au chiffre à l'indice 1 de la liste..."""
                
                # affichage du résultat que les deux chiffres 
                # trouvés sont identiques
                self.my_label.config(text='Trouvé !')  
                
                for key in self.answer_dict:
                    # les boutons des chiffres identiques sont désactivés
                    key['state'] = 'disabled'  
                    
                # réinitialisation du compteur pour revenir 
                # à la précédente condition ci-avant    
                self.count = 0  
                
                # réinitialisation de la liste pour revenir à la précédente 
                # condition ci-avant
                self.answer_list = []  
                
                # réinitialisation du dictionnaire pour revenir à la 
                # précédente condition ci-avant
                self.answer_dict = {}  
                
                
                self.winner += 1  # incrémentation du compteur du jeu gagné
                
                if self.winner == 6:
                    self.win()
           
            else:
                """et si les deux chiffres sélectionnés 
                ne sont pas identiques..."""
                
                # self.my_label.config(text='No !')  # affichage d'un message
                
                # réinitialisation du compteur pour revenir 
                # à la précédente condition ci-avant
                self.count = 0  
                
                # réinitialisation de la liste pour revenir 
                # à la précédente condition ci-avant
                self.answer_list = []  
                
                # affichage d'une boîte de message
                messagebox.showinfo('Incorrect !', 'Incorrect !')  
                
                # réinitialisation des chiffres affichés sur les boutons
                for key in self.answer_dict: 
                    key['text'] = ' '
                    
                # réinitialisation du dictionnaire pour revenir 
                # à la précédente condition ci-avant    
                self.answer_dict = {}  

    def reset(self):
        """Méthode permettant de réinitialiser le jeu"""

        """Réintialisation du compteur du jeu gagné"""
        self.winner = 0

        """Assignation d'une liste d'entiers à afficher 
        dans le jeu de memory qui se compose de 12 cases"""
        # Les 12 composants du jeu de memory
        self.matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]  

        """Mélange des chifres listés ci-avant avec la méthode prédéfinie
        shuffle (mélanger) du module random"""
        random.shuffle(self.matches)

        """Réinitialisation de l'affichage du résultat"""
        self.my_label.config(text='')

        """Réinitialisation des chiffres affichés"""
        # assignation liste des boutons
        button_list = [
            self.b0, 
            self.b1, 
            self.b2, 
            self.b3, 
            self.b4, 
            self.b5, 
            self.b6, 
            self.b7, 
            self.b8, 
            self.b9, 
            self.b10, 
            self.b11]  

        """Réinitialisation de la couleur des boutons par défaut"""
        for button in button_list:
            button.config(text=' ', bg='SystemButtonFace', state='normal')


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
  