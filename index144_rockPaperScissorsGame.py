"""
Tkinter - Codemy.com #144 : 
Rock Paper Scissors Game - Python Tkinter GUI Tutorial #144
Lien : https://www.youtube.com/watch?v=ZDiPqfFF7pw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=144

Dans ce programme on apprend à faire le jeu 'Pierre feuille ciseaux' :D

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

import tkinter
from tkinter import ttk
from random import randint

class Gui:
    
    def __init__(self, root):
        "Constructeur de la classe"
        
        # Configuration de la fenêtre principale
        root.iconbitmap('images/Logo.ico')
        root.title('Titre !')
        root.geometry('600x600')
        root.config(bg='white')
        
        self.widgets()
        
    def widgets(self):
        "Configuration des widgets"
        
        """Chargement des images"""
        rock = tkinter.PhotoImage(file='images/rock.png')
        paper = tkinter.PhotoImage(file='images/paper.png')
        scissors = tkinter.PhotoImage(file='images/scissors.png')

        """Ajout des images dans une liste"""
        self.image_list = [rock, paper, scissors]

        """Choisir un nombre au hasard entre 0 et 2 
        (n° des indices de la liste self.image_list)"""
        pick_number = randint(0, 2)

        """Affichage au hasard de l'image sous la forme d'une étiquette"""
        self.image_label = tkinter.Label(root, image=self.image_list[pick_number])
        self.image_label.pack(pady=20)

        """Bouton permettant de changer au hasard l'image affichée"""
        spin_button = tkinter.Button(
            root, 
            text='Changer ! ', 
            command=self.spin)
        spin_button.pack(pady=20)

        """Liste déroulante pour faire son choix"""
        self.user_choice = ttk.Combobox(
            root, 
            value=(
                'Pierre', 
                'Papier', 
                'Ciseaux'), 
            justify='center')
        self.user_choice.current(0) # affichage par défaut : 'Pierre'
        self.user_choice.pack(pady=20)

        """Message affichant si on a gagné ou si on a perdu"""
        self.win_lose_label = tkinter.Label(
            root, 
            text='', 
            font='Helvetica 18', 
            bg='white')
        self.win_lose_label.pack(pady=50)
        
    def spin(self):
        """Méthode permettant de changer d'image à chaque fois 
        qu'on appuye sur le bouton 'Changer !'"""

        """Image choisie au hasard"""
        
        # nombre au hasard entre 0 et 2 
        # (indices de la liste self.image_list)
        pick_number = randint(0, 2)  
        
         # image affichée au hasard
        self.image_label.config(image=self.image_list[pick_number]) 

        """Conversion de la liste du menu déroulant en nombre"""
        if self.user_choice.get() == 'Pierre':
            self.user_choice_value = 0
        elif self.user_choice.get() == 'Papier':
            self.user_choice_value = 1
        elif self.user_choice.get() == 'Ciseaux':
            self.user_choice_value = 2

        """Comparaison entre le nombre du menu déroulant converti 
        (self.user_choice) avec le nombre au hasard (pick_number)"""

        """Si la pierre est choisie"""
        if self.user_choice_value == 0:
            if pick_number == 0:  # la pierre est sortie
                self.win_lose_label.config(
                    text='Ex-aequo !')
            elif pick_number == 1:  # le papier est sorti
                self.win_lose_label.config(
                    text='Le papier couvre la pierre ! \
Tu as donc perdu...')
            elif pick_number == 2:  # les ciseaux sont sortis
                self.win_lose_label.config(
                    text='La pierre fracasse les ciseaux ! \
Tu as donc gagné !')

        """Si le papier est choisi"""
        if self.user_choice_value == 1:
            if pick_number == 0:  # la pierre est sortie
                self.win_lose_label.config(
                    text='Le papier couvre la pierre ! \
Tu as donc gagné !')
            elif pick_number == 1:  # le papier est sorti
                self.win_lose_label.config(
                    text='Ex-aequo !')
            elif pick_number == 2:  # ciseaux sortie
                self.win_lose_label.config(
                    text='Les ciseaux cisaillent le papier ! \
Tu as donc perdu...')

        """Si les ciseaux sont choisis"""
        if self.user_choice_value == 2:
            if pick_number == 0:  # la pierre est sortie
                self.win_lose_label.config(
                    text='La pierre fracasse les ciseaux ! \
Tu as donc perdu...')
            elif pick_number == 1:  # le papier est sorti
                self.win_lose_label.config(
                    text='Les ciseaux cisaillent le papier ! \
Tu as donc gagné !')
            elif pick_number == 2:  # les ciseaux sont sortis
                self.win_lose_label.config(text='Ex-aequo !')

        
if __name__ == '__main__':
    root = tkinter.Tk()
    gui = Gui(root)
    root.mainloop()
