"""
Tkinter - Codemy.com #113 : Tic Tac Toe Game
Lien : https://www.youtube.com/watch?v=xx0qmpuA-vM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=113

Jeu du morpion !

Éditeur : Laurent REYNAUD
Date : 20-12-20
"""

from tkinter import *
from tkinter import messagebox  # pour les boîtes de message (information, avertissement...)

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Jeu du morpion !')
# root.geometry('1200x710')  # pas nécessaire car les dimensions s'adaptent automatiquement avec la mise en place des
# boutons

clicked = True  # assignation d'une variable = vrai
count = 0  # assignation d'un compteur qui ne doit pas dépasser 9 coups à jouer


def disable_all_buttons():
    """Fonction permettant de désactiver toutes les autres cases dès qu'un joueur a gagné avant les 9 coups"""
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def checkifwon():
    """Fonction permettant de vérifier si quelqu'un a gagné"""

    global winner  # assignation d'une variable globale
    winner = False  # pas de gagnant

    """Les 3 'X' sont alignées"""
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        b1.config(bg='blue')
        b2.config(bg='blue')
        b3.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'X' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        b4.config(bg='blue')
        b5.config(bg='blue')
        b6.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'X' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées
    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
        b7.config(bg='blue')
        b8.config(bg='blue')
        b9.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'X' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées
    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        b1.config(bg='blue')
        b4.config(bg='blue')
        b7.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'X' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées
    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        b2.config(bg='blue')
        b5.config(bg='blue')
        b8.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'X' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées
    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        b3.config(bg='blue')
        b6.config(bg='blue')
        b9.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'X' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées
    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        b1.config(bg='blue')
        b5.config(bg='blue')
        b9.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'X' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées
    elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        b3.config(bg='blue')
        b5.config(bg='blue')
        b7.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'X' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées

        """Les 3 'O' sont alignées"""
    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        b1.config(bg='blue')
        b2.config(bg='blue')
        b3.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'O' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        b4.config(bg='blue')
        b5.config(bg='blue')
        b6.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'O' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        b7.config(bg='blue')
        b8.config(bg='blue')
        b9.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'O' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        b1.config(bg='blue')
        b4.config(bg='blue')
        b7.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'O' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        b2.config(bg='blue')
        b5.config(bg='blue')
        b8.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'O' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        b3.config(bg='blue')
        b6.config(bg='blue')
        b9.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'O' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées
    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        b1.config(bg='blue')
        b5.config(bg='blue')
        b9.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'O' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées
    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
        b3.config(bg='blue')
        b5.config(bg='blue')
        b7.config(bg='blue')
        winner = True
        messagebox.showinfo('Jeu du morpion !', "Les 'O' ont gagné !\nFélicitations !")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées


def b_click(b):
    """Fonction permettant de sélectionner une case
    L'instruction ci-dessous du bouton :
    b['text'] = ' '
    équivaut à l'instruction ci-dessous d'une étiquette :
    l.config(text=' ')"""

    global clicked, count  # assignation de variables globales

    if b['text'] == ' ' and clicked == True:
        """Si la case est vide et que l'on clique"""
        b['text'] = 'X'  # le bouton affiche la lettre 'X'
        clicked = False  # arrêt de la condition 'if' : la sélection du bouton suivant n'affichera pas 'X'
        count += 1  # compteur de coup joué (limité à 9 coups)
        checkifwon()  # appel de la fonction permettant de vérifier si un joueur a gagné
    elif b['text'] == ' ' and clicked == False:
        """Si la case est vide et que l'on a pas cliqué"""
        b['text'] = 'O'  # # le bouton affiche la lettre 'O'
        clicked = True  # arrêt de la condition 'elif' : la sélection du bouton suivant n'affichera pas 'O'
        count += 1  # compteur de coup joué (limité à 9 coups)
        checkifwon()  # appel de la fonction permettant de vérifier si un joueur a gagnés
    else:
        """Sinon si la case n'est pas vide et que l'on clique dessus"""
        messagebox.showerror('Jeu du morpion !', 'Hé ! Cette case a déjà été cochée !\nNooob !!!')

    if count == 9 and winner == False:
        """Si on arrive à la case 9 et que personne n'a gagné"""
        messagebox.showinfo('Jeu du morpion !', "Personne n'a gagné !\nNullos !!!")
        disable_all_buttons()  # appel de la fonction permettant de désactiver les autres cases non cochées


def reset():
    """Fonction permettant de réinitiliser le jeu"""

    global b1, b2, b3, b4, b5, b6, b7, b8, b9  # assignation de variables globales des cases du jeu

    """Les 9 cases du jeu construites sous la forme de boutons"""
    b1 = Button(root, text=' ', font='Helevetica 20', height=3, width=6, bg='SystemButtonFace',
                command=lambda: b_click(b1))
    b2 = Button(root, text=' ', font='Helevetica 20', height=3, width=6, bg='SystemButtonFace',
                command=lambda: b_click(b2))
    b3 = Button(root, text=' ', font='Helevetica 20', height=3, width=6, bg='SystemButtonFace',
                command=lambda: b_click(b3))

    b4 = Button(root, text=' ', font='Helevetica 20', height=3, width=6, bg='SystemButtonFace',
                command=lambda: b_click(b4))
    b5 = Button(root, text=' ', font='Helevetica 20', height=3, width=6, bg='SystemButtonFace',
                command=lambda: b_click(b5))
    b6 = Button(root, text=' ', font='Helevetica 20', height=3, width=6, bg='SystemButtonFace',
                command=lambda: b_click(b6))

    b7 = Button(root, text=' ', font='Helevetica 20', height=3, width=6, bg='SystemButtonFace',
                command=lambda: b_click(b7))
    b8 = Button(root, text=' ', font='Helevetica 20', height=3, width=6, bg='SystemButtonFace',
                command=lambda: b_click(b8))
    b9 = Button(root, text=' ', font='Helevetica 20', height=3, width=6, bg='SystemButtonFace',
                command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


"""Configuration d'un menu"""
my_menu = Menu(root)
root.config(menu=my_menu)

"""Création d'un menu Options"""
options_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Options', menu=options_menu)
options_menu.add_command(label='Réinitialiser le jeu', command=reset)

reset()  # appel de la fonction permettant de réinitialiser le jeu

root.mainloop()
