"""
Tkinter - Codemy.com #141 : 
Tile Matching Game - Python Tkinter GUI Tutorial #141
Lien : https://www.youtube.com/watch?v=tlMPVGSEEDw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=141

Dans ce programme on créé un jeu de mémory 
(plusieurs cartes cachées : il faut retrouver deux images identiques)

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
        root.geometry('500x550')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Assignation de variables à utiliser 
        pour la fonction button_click()"""
        
        # décompte du nombre de fois que l'on sélectionne un bouton
        self.count = 0  
        
        # alimentation des chiffres affichés dans une liste
        self.answer_list = []  
        
        # alimentation des chiffres affichés dans un dictionnaire
        self.answer_dict = {}  

        """Assignation d'une liste d'entiers à afficher 
        dans le jeu de memory qui se compose de 12 cases"""
        
        # constitue les 12 composants du jeu de memory
        self.matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]  

        """Mélange des chifres listés ci-avant avec la méthode 
        prédefinie shuffle (mélanger) du module random"""
        random.shuffle(self.matches)
        
        """Cadre pour les boutons"""
        my_frame = tkinter.Frame(root)
        my_frame.pack(pady=10)

        """Configuration des boutons"""
        
        b0 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(b0, 0))
        
        b1 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(b1, 1))
        
        b2 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(b2, 2))
        
        b3 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(b3, 3))

        b4 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(b4, 4))
        
        b5 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(b5, 5))
        
        b6 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(b6, 6))
        
        b7 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(b7, 7))

        b8 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(b8, 8))
        
        b9 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(b9, 9))
        
        b10 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(b10, 10))
        
        b11 = tkinter.Button(
            my_frame, 
            text=' ', 
            font='Helvetica 20', 
            height=3, 
            width=6, 
            command=lambda: self.button_click(b11, 11))

        """Affichage des boutons"""
        b0.grid(row=0, column=0)
        b1.grid(row=0, column=1)
        b2.grid(row=0, column=2)
        b3.grid(row=0, column=3)

        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)
        b7.grid(row=1, column=3)

        b8.grid(row=2, column=0)
        b9.grid(row=2, column=1)
        b10.grid(row=2, column=2)
        b11.grid(row=2, column=3)

        """Affichage du résultat"""
        self.my_label = tkinter.Label(root, text='')
        self.my_label.pack(pady=20)
        
    def button_click(self, b, number):
        """Méthode permettant d'afficher un chiffre
        en cliquant sur le bouton concerné"""

        if b['text'] == ' ' and self.count < 2:
            """Si la case est vide et que c'est le première séléction : 
            Affichage du nombre attribué au bouton sélectionné 
            selon un chiffre au hasard : dans l'instruction ci-dessous 
            par principe le bouton à l'indice 0 (b[0]) affichera 
            le chiffre 1 (self.matches[0] = 1), mais comme on a déclaré 
            l'instruction suivante : random.shuffle(self.matches), 
            le nombre affiché sera compris entre 1 et 6"""
            
            b['text'] = self.matches[number]
            
            """Conservation du chiffre affiché dans une liste 
            et dans un dictionnaire"""
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
                
                # réinitialisation de la liste pour revenir 
                # à la précédente condition ci-avant
                self.answer_list = []  
                
                # réinitialisation du dictionnaire pour revenir 
                # à la précédente condition ci-avant
                self.answer_dict = {}  
                
            else:
                """et si les deux chiffres sélectionnés 
                ne sont pas identiques..."""
                
                # affichage d'un message
                self.my_label.config(text='No !')  
                
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


if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
