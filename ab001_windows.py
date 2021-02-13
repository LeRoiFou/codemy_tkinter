""""
Les bases de tkinter

Dans ce programme on apprend à :
-> diminuer la fenêtre principale,
-> cacher la fenêtre principale,
-> réafficher la fenêtre principale
-> quitter toutes les fenêtres d'un seul coup

Éditeur : Laurent REYNAUD
Date : 06-01-2021
"""

from tkinter import *

"""Configuration de la fenêtre principale"""
root = Tk()
root.title('Titre !')
root.geometry('400x400')


def open_window():
    """Fonction permettant d'ouvrir une nouvelle fenêtre"""

    """Configuration de la nouvelle fenêtre"""
    new = Toplevel()
    new.title('Nouvelle fenêtre !')
    new.geometry('300x200')

    """Texte affiché dans cette deuxième fenêtre"""
    my_label = Label(new, text="C'est une nouvelle fenêtre !")
    my_label.pack()

    """Bouton permettant de fermer la 2ème fenêtre"""
    destroy_button = Button(new, text='Quitter', command=new.destroy)
    destroy_button.pack()

    """Bouton permettant de diminuer la fenêtre principale"""
    hide_button = Button(new, text='Diminuer la fenêtre principale', command=root.iconify)
    hide_button.pack()

    """Bouton permettant de cacher la fenêtre principale"""
    hide_button = Button(new, text='Cacher la fenêtre principale', command=root.withdraw)
    hide_button.pack()

    """Bouton permettant de réafficher la fenêtre principale"""
    show_button = Button(new, text='Réafficher la fenêtre principale', command=root.deiconify)
    show_button.pack()

    """Bouton permettant de quitter toutes les fenêtres"""
    destroy_button = Button(new, text='Quitter tout', command=root.destroy)
    destroy_button.pack()

    new.mainloop()


"""Bouton d'exécution pour afficher une nouvelle fenêtre"""
my_button = Button(root, text='Ouvrir une 2ème fenêtre', command=open_window)
my_button.pack(pady=20)

root.mainloop()
