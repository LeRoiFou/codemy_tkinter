"""
Tkinter - Codemy.com #46 : Menu Bars With tKinter
Lien : https://www.youtube.com/watch?v=ZS2_v_zsPTg&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=46

Création d'une barre de menus

Éditeur : Laurent REYNAUD
Date : 28-11-2020
"""

from tkinter import *

root = Tk()
root.geometry('400x400')
root.title("Titre !")


def our_command():
    myLabel = Label(root, text='Vous avez cliqué sur un menu déroulant !').pack()


# Configuration de la barre de menus
my_menu = Menu(root)
root.config(menu=my_menu)

# 1er titre de la barre de menus : 'Fichier'
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Fichier', menu=file_menu)

# Ajout des difféntes commandes du menu 'Fichier'
file_menu.add_command(label='Nouveau...', command=our_command)
file_menu.add_separator()
file_menu.add_command(label='Sortie', command=root.quit)

# 2ème titre de la barre de menus : 'Édition'
edit_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Édition', menu=edit_menu)

# Ajout des difféntes commandes du menu 'Édition'
edit_menu.add_command(label='Couper', command=our_command)
edit_menu.add_command(label='Coller', command=our_command)

# 3ème titre de la barre de menus : 'Options'
options_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Options', menu=options_menu)

# Ajout des difféntes commandes du menu 'Options'
options_menu.add_command(label='Rechercher', command=our_command)
options_menu.add_command(label='Annuler', command=our_command)

root.mainloop()
