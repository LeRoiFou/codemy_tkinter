"""
Tkinter - Codemy.com #127 : How To Disable Or Delete A Menu Item - Python Tkinter GUI Tutorial #127
Lien : https://www.youtube.com/watch?v=s1WDk9-jJ6A&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=127

Dans ce programme on apprend à déconnecter ou à supprimer un menu

Éditeur : Laurent REYNAUD
Date : 23-12-20
"""

from tkinter import *

root = Tk()
root.iconbitmap('images/Logo.ico')
root.title('Titre !')
root.geometry('500x500')


def new_file():
    pass


def open_file():
    pass


def disable_new():
    """Fonction permettant de désactiver la commande 'Nouveau' du menu 'Fichier'"""
    file_menu.entryconfig('Nouveau', state=DISABLED)


def enable_new():
    """Fonction permettant d'activer la commande 'Nouveau' du menu 'Fichier'"""
    file_menu.entryconfig('Nouveau', state=ACTIVE)


def delete_new():
    """Fonction permettant de supprimer la commande 'Nouveau' du menu 'Fichier'"""
    file_menu.delete('Nouveau')


"""Barre de menu"""
my_menu = Menu(root)
root.config(menu=my_menu)

"""Menu Fichier"""
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Fichier', menu=file_menu)
file_menu.add_command(label='Nouveau', command=new_file)
file_menu.add_command(label='Ouvrir', command=open_file)

"""Boutons"""
disable_button = Button(root, text="Désactiver la commande 'Nouveau'", command=disable_new)
disable_button.pack(pady=50)
enable_button = Button(root, text="Activer la commande 'Nouveau'", command=enable_new)
enable_button.pack(pady=10)
delete_button = Button(root, text="Supprimer la commande 'Nouveau'", command=delete_new)
delete_button.pack(pady=20)

root.mainloop()
