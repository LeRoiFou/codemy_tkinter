"""
Tkinter - Codemy.com #146 : How To Dynamically Resize Button Text - Python Tkinter GUI Tutorial #146
Lien : https://www.youtube.com/watch?v=m4Oo1crYZTM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=146

Dans ce programme en plus de changer dynamiquement les dimensions d'un bouton par rapport aux dimensions de la fenêtre,
on change également de manière dynamique le texte du bouton

Éditeur : Laurent REYNAUD
Date : 26-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x500')


def resize(e):
    """Fonction permettant de lier les dimensions du texte avec le bouton associé"""

    """Taille de la fenêtre divisé par 10 pixels"""
    size = e.width / 10

    """Changement de la taille de l'écriture du bouton"""
    button_1.config(font=('Helvetica', int(size)))


"""Configuration du bouton avec la méthode grid()"""
Grid.rowconfigure(root, index=0, weight=1)  # configuration de la ligne 0
Grid.columnconfigure(root, index=0, weight=1)  # configuration de la colonne 0

"""Configuration du bouton"""
button_1 = Button(root, text='Bouton n° 1 !')
button_1.grid(row=0, column=0, sticky='nsew')

"""Liaison avec l'application"""
root.bind('<Configure>', resize)  # 'configure' permet de prendre en compte les dimensions du widget

root.mainloop()
