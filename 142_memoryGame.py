"""
Tkinter - Codemy.com #142 : Finishing Our Tile Matching Game - Python Tkinter GUI Tutorial #142
Lien : https://www.youtube.com/watch?v=tW8Bzokv8CQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=142

Dans ce programme on créé un jeu de mémory (plusieurs cartes cachées : il faut retrouver deux images identiques)
En complément du précédent tuto, on finalise le jeu avec un menu, des couleurs aux boutons, une réinitialisation du jeu
et un message informant que l'on a gagné

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('460x460')

"""Assignation d'une variable globale informant si on a gagné"""
global winner
winner = 0

"""Assignation de variables à utiliser pour la fonction button_click()"""
count = 0  # décompte du nombre de fois que l'on sélectionne un bouton
answer_list = []  # alimentation des chiffres affichés dans une liste
answer_dict = {}  # alimentation des chiffres affichés dans un dictionnaire

"""Assignation d'une liste d'entiers à afficher dans le jeu de memory qui se compose de 12 cases"""
matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]  # constitue les 12 composants du jeu de memory

"""Mélange des chifres listés ci-avant avec la méthode prédef shuffle (mélanger) du module random"""
random.shuffle(matches)


def win():
    """Fonction permettant de voir si on a gagné"""

    my_label.config(text='Félicitations, tu as gagné !')  # affichage du message informant que le jeu est fini

    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]  # assignation liste des boutons

    """Parcours des boutons et changement des couleurs dès que tous les chiffres ont été trouvés"""
    for button in button_list:
        button.config(bg='yellow')


def button_click(b, number):
    """Fonction permettant d'afficher un chiffre en cliquant sur le bouton concerné"""

    global count, answer_list, answer_dict, winner

    if b['text'] == ' ' and count < 2:
        """Si la case est vide et que c'est le première séléction : 
        Affichage du nombre attribué au bouton sélectionné selon un chiffre au hasard : dans l'instruction ci-dessous 
        par principe le bouton à l'indice 0 (b[0]) affichera le chiffre 1 (matches[0] = 1), mais comme on a déclaré 
        l'instruction suivante : random.shuffle(matches), le nombre affiché sera compris entre 1 et 6"""
        b['text'] = matches[number]
        """Conservation du chiffre affiché dans une liste et dans un dictionnaire"""
        answer_list.append(number)
        answer_dict[b] = matches[number]
        """Incrémentation du compteur"""
        count += 1

    if len(answer_list) == 2:
        """S'il y a deux composants dans la liste..."""
        if matches[answer_list[0]] == matches[answer_list[1]]:
            """et si le chiffre à l'indice 0 de la liste est égal au chiffre à l'indice 1 de la liste..."""
            my_label.config(text='Trouvé !')  # affichage du résultat que les deux chiffres trouvés sont identiques
            for key in answer_dict:
                key['state'] = 'disabled'  # les boutons des chiffres identiques sont désactivés
            count = 0  # réinitialisation du compteur pour revenir à la précédente condition ci-avant
            answer_list = []  # réinitialisation de la liste pour revenir à la précédente condition ci-avant
            answer_dict = {}  # réinitialisation du dictionnaire pour revenir à la précédente condition ci-avant
            winner += 1  # incrémentation du compteur du jeu gagné
            if winner == 6:
                win()
        else:
            """et si les deux chiffres sélectionnés ne sont pas identiques..."""
            # my_label.config(text='No !')  # affichage d'un message
            count = 0  # réinitialisation du compteur pour revenir à la précédente condition ci-avant
            answer_list = []  # réinitialisation de la liste pour revenir à la précédente condition ci-avant
            messagebox.showinfo('Incorrect !', 'Incorrect !')  # affichage d'une boîte de message
            for key in answer_dict:  # réinitialisation des chiffres affichés sur les boutons
                key['text'] = ' '
            answer_dict = {}  # réinitialisation du dictionnaire pour revenir à la précédente condition ci-avant


def reset():
    """Fonction permettant de réinitialiser le jeu"""

    global matches, winner

    """Réintialisation du compteur du jeu gagné"""
    winner = 0

    """Assignation d'une liste d'entiers à afficher dans le jeu de memory qui se compose de 12 cases"""
    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]  # constitue les 12 composants du jeu de memory

    """Mélange des chifres listés ci-avant avec la méthode prédef shuffle (mélanger) du module random"""
    random.shuffle(matches)

    """Réinitialisation de l'affichage du résultat"""
    my_label.config(text='')

    """Réinitialisation des chiffres affichés"""
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]  # assignation liste des boutons

    """Réinitialisation de la couleur des boutons par défaut"""
    for button in button_list:
        button.config(text=' ', bg='SystemButtonFace', state='normal')


"""Cadre pour les boutons"""
my_frame = Frame(root)
my_frame.pack(pady=10)

"""Configuration des boutons"""
b0 = Button(my_frame, text=' ', font='Helvetica 20', height=3, width=6, command=lambda: button_click(b0, 0),
            relief='groove')
b1 = Button(my_frame, text=' ', font='Helvetica 20', height=3, width=6, command=lambda: button_click(b1, 1),
            relief='groove')
b2 = Button(my_frame, text=' ', font='Helvetica 20', height=3, width=6, command=lambda: button_click(b2, 2),
            relief='groove')
b3 = Button(my_frame, text=' ', font='Helvetica 20', height=3, width=6, command=lambda: button_click(b3, 3),
            relief='groove')

b4 = Button(my_frame, text=' ', font='Helvetica 20', height=3, width=6, command=lambda: button_click(b4, 4),
            relief='groove')
b5 = Button(my_frame, text=' ', font='Helvetica 20', height=3, width=6, command=lambda: button_click(b5, 5),
            relief='groove')
b6 = Button(my_frame, text=' ', font='Helvetica 20', height=3, width=6, command=lambda: button_click(b6, 6),
            relief='groove')
b7 = Button(my_frame, text=' ', font='Helvetica 20', height=3, width=6, command=lambda: button_click(b7, 7),
            relief='groove')

b8 = Button(my_frame, text=' ', font='Helvetica 20', height=3, width=6, command=lambda: button_click(b8, 8),
            relief='groove')
b9 = Button(my_frame, text=' ', font='Helvetica 20', height=3, width=6, command=lambda: button_click(b9, 9),
            relief='groove')
b10 = Button(my_frame, text=' ', font='Helvetica 20', height=3, width=6, command=lambda: button_click(b10, 10),
             relief='groove')
b11 = Button(my_frame, text=' ', font='Helvetica 20', height=3, width=6, command=lambda: button_click(b11, 11),
             relief='groove')

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
my_label = Label(root, text='')
my_label.pack(pady=20)

"""Création d'une barre de menu"""
my_menu = Menu(root)
root.config(menu=my_menu)

"""Menu options"""
option_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Options', menu=option_menu)
option_menu.add_command(label='Réinitialiser le jeu', command=reset)
option_menu.add_separator()
option_menu.add_command(label='Quitter le jeu', command=root.quit)

root.mainloop()
