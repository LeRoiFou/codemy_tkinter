"""
Tkinter - Codemy.com #131 : Balloon Text Tool Tips With Tkinter - Python Tkinter GUI Tutorial #131
Lien : https://www.youtube.com/watch?v=hkSDx-K-cHM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=131

Dans ce programme on apprend à faire des infos-bulles sur les widgets : ce nouveau widget n'est plus mis à jour depuis
la version 3.6 de python mais il est toujours utilisable.
Changer la couleur de fond de l'info-bulle est extrêmement difficile... elle sera donc toujours de couleur jaune

Éditeur : Laurent REYNAUD
Date : 24-12-20
"""

from tkinter import *
from tkinter.tix import *  # pour les infos-bulles (ce sous-module n'est plus mis à jour depuis la version 3.6)

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x350')

"""Info-bulle"""
tip = Balloon(root)

"""Bouton"""
my_button = Button(root, text='Clique !')
my_button.pack(pady=50)

"""Etiquette"""
my_label = Label(root, text='Machin', font='Helvetica 20')
my_label.pack(pady=20)

"""Bind permettant de relier l'info-bulle au bouton"""
tip.bind_widget(my_button, balloonmsg="C'est une info-bulle !")

"""Bind permettant de relier l'info-bulle à l'étiquette"""
tip.bind_widget(my_label, balloonmsg="C'est encore une putain d'info-bulle !")

root.mainloop()
