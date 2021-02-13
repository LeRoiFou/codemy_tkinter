"""
Tkinter - Codemy.com #144 : Rock Paper Scissors Game - Python Tkinter GUI Tutorial #144
Lien : https://www.youtube.com/watch?v=ZDiPqfFF7pw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=144

Dans ce programme on apprend à faire le jeu 'Pierre feuille ciseaux' :D

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

from tkinter import *
from random import randint
from tkinter import ttk

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('600x600')
root.config(bg='white')


def spin():
    """Fonction permettant de changer d'image à chaque fois qu'on appuye sur le bouton 'Changer !'"""

    """Image choisie au hasard"""
    pick_number = randint(0, 2)  # nombre au hasard entre 0 et 2 (indices de la liste image_list)
    image_label.config(image=image_list[pick_number])  # image affichée au hasard

    """Conversion de la liste du menu déroulant en nombre"""
    if user_choice.get() == 'Pierre':
        user_choice_value = 0
    elif user_choice.get() == 'Papier':
        user_choice_value = 1
    elif user_choice.get() == 'Ciseaux':
        user_choice_value = 2

    """Comparaison entre le nombre du menu déroulant converti (user_choice) avec le nombre au hasard (pick_number)"""

    """Si la pierre est choisie"""
    if user_choice_value == 0:
        if pick_number == 0:  # la pierre est sortie
            win_lose_label.config(text='Ex-aequo !')
        elif pick_number == 1:  # le papier est sorti
            win_lose_label.config(text='Le papier couvre la pierre ! Tu as donc perdu...')
        elif pick_number == 2:  # les ciseaux sont sortis
            win_lose_label.config(text='La pierre fracasse les ciseaux ! Tu as donc gagné !')

    """Si le papier est choisi"""
    if user_choice_value == 1:
        if pick_number == 0:  # la pierre est sortie
            win_lose_label.config(text='Le papier couvre la pierre ! Tu as donc gagné !')
        elif pick_number == 1:  # le papier est sorti
            win_lose_label.config(text='Ex-aequo !')
        elif pick_number == 2:  # ciseaux sortie
            win_lose_label.config(text='Les ciseaux cisaillent le papier ! Tu as donc perdu...')

    """Si les ciseaux sont choisis"""
    if user_choice_value == 2:
        if pick_number == 0:  # la pierre est sortie
            win_lose_label.config(text='La pierre fracasse les ciseaux ! Tu as donc perdu...')
        elif pick_number == 1:  # le papier est sorti
            win_lose_label.config(text='Les ciseaux cisaillent le papier ! Tu as donc gagné !')
        elif pick_number == 2:  # les ciseaux sont sortis
            win_lose_label.config(text='Ex-aequo !')


"""Chargement des images"""
rock = PhotoImage(file='images/rock.png')
paper = PhotoImage(file='images/paper.png')
scissors = PhotoImage(file='images/scissors.png')

"""Ajout des images dans une liste"""
image_list = [rock, paper, scissors]

"""Choisir un nombre au hasard entre 0 et 2 (n° des indices de la liste image_list)"""
pick_number = randint(0, 2)

"""Affichage au hasard de l'image sous la forme d'une étiquette"""
image_label = Label(root, image=image_list[pick_number])
image_label.pack(pady=20)

"""Bouton permettant de changer au hasard l'image affichée"""
spin_button = Button(root, text='Changer ! ', command=spin)
spin_button.pack(pady=20)

"""Liste déroulante pour faire son choix"""
user_choice = ttk.Combobox(root, value=('Pierre', 'Papier', 'Ciseaux'), justify='center')
user_choice.current(0)  # affichage par défaut : 'Pierre'
user_choice.pack(pady=20)

"""Message affichant si on a gagné ou si on a perdu"""
win_lose_label = Label(root, text='', font='Helvetica 18', bg='white')
win_lose_label.pack(pady=50)

root.mainloop()
