"""
Tkinter - Codemy.com #161 : On/Off Button Switch - Python Tkinter GUI Tutorial #161
Lien : https://www.youtube.com/watch?v=n1ucrkly2nc

Dans ce programme on apprend à afficher un bouton interrupteur 'on' / 'off'. Pour cela, on a recours au booléen.

Éditeur : Laurent REYNAUD
Date : 12-01-21
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x300')

"""Assignation d'un booléen pour le bouton lorsqu'il est sur 'on'"""
global is_on
is_on = True  # à l'origine, le bouton 'on' est 'True'


def switch():
    """Fonction permettant de changer l'interrupteur on / off"""

    global is_on

    """Déterminé si c'est sur 'on' ou sur 'off'"""
    if is_on:  # si c'est sur 'on'
        on_button.config(image=off)  # en appuyant sur le bouton celui-ci est sur 'off'
        is_on = False  # cette fois-ci le bouton 'on' est 'False'
        my_label.config(text='Interrupteur éteint !', fg='grey')  # on change le texte
    else:
        on_button.config(image=on)  # sinon le bouton est sur 'on'
        is_on = True  # cette fois-ci le bouton 'on' est 'True'
        my_label.config(text='Interrupteur allumé !', fg='green')  # on change le texte


""""Configuration de l'étiquette"""
my_label = Label(root, text="L'interrupteur allumé !", fg='green', font='Helvetica 32')
my_label.pack(pady=20)

"""Configuration de l'image"""
on = PhotoImage(file='images/on.png')
off = PhotoImage(file='images/off.png')

"""Configuration du bouton"""
on_button = Button(root, image=on, bd=0, command=switch)
on_button.pack(pady=50)

root.mainloop()
